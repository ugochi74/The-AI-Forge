"""Local solutions to the course exercises; no third-party packages required."""
import ast
import csv
import json
import math
from pathlib import Path
import statistics
import tempfile

from main import (Record, best_time, dot, format_report, load_records,
                  peak_bytes, row_to_record, run_demo)


def median(values):
    ordered = sorted(values)
    if not ordered:
        raise ValueError('median needs at least one value')
    middle = len(ordered) // 2
    return ordered[middle] if len(ordered) % 2 else (ordered[middle - 1] + ordered[middle]) / 2


def stream_records(path):
    with Path(path).open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        names = [name for name in reader.fieldnames if name != 'label']
        for row in reader:
            yield row_to_record(row, names)


def matvec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def main():
    for seed in (7, 8):
        print(f'\nSeed {seed}')
        print(format_report(run_demo(seed=seed)))
    for values in ([3, 1, 2], [4, 1, 3, 2], [-3, -1], [9]):
        assert median(values) == statistics.median(values)
    print('\nMedian agrees with statistics.median on odd, even, negative and singleton inputs.')
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / 'records.csv'
        with path.open('w', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow(['x1', 'x2', 'label'])
            for i in range(200_000):
                writer.writerow([i, i / 2, i % 2])
        assert next(stream_records(path)) == Record((0.0, 0.0), 0)
        print('Streaming 200,000 rows peak bytes:', peak_bytes(lambda: sum(1 for _ in stream_records(path))))
        print('Loading 200,000 rows peak bytes:', peak_bytes(lambda: load_records(path)))
    try:
        import numpy as np
    except ImportError:
        print('SKIP NumPy matvec comparison: NumPy is not installed.')
    else:
        for size in (4, 64, 1024):
            matrix = [[float((i + j) % 7) for j in range(size)] for i in range(size)]
            vector = [float(i % 3) for i in range(size)]
            expected = matvec(matrix, vector)
            array, v = np.array(matrix), np.array(vector)
            assert all(math.isclose(a, b) for a, b in zip(expected, array @ v, strict=True))
            print('matvec size, Python seconds, NumPy seconds:', size,
                  best_time(matvec, matrix, vector), best_time(lambda: array @ v))
    root = Path(__file__).resolve().parents[4]
    files = list((root / 'phases').glob('*/*/code/*.py'))
    counts = {name: 0 for name in ('ListComp', 'Yield', 'With')}
    for path in files:
        nodes = list(ast.walk(ast.parse(path.read_text())))
        for name in counts:
            counts[name] += any(isinstance(node, getattr(ast, name)) for node in nodes)
    print('Local workspace construct counts (subset of upstream course):', json.dumps(counts), 'files:', len(files))


if __name__ == '__main__':
    main()
