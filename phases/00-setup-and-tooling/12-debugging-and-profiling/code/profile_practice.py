"""Small standard-library workload for timing, memory and debugger practice."""
import argparse
import math
import tracemalloc
from debug_tools import Timer


def load_data():
    return [float(i) / 100 for i in range(100_000)]


def score_data(values):
    return sum(math.sqrt(value) for value in values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    tracemalloc.start()
    with Timer('data loading'):
        values = load_data()
    with Timer('scoring'):
        score = score_data(values)
    snapshot = tracemalloc.take_snapshot()
    for stat in snapshot.statistics('lineno')[:5]:
        print(stat)
    tracemalloc.stop()
    if args.debug:
        breakpoint()  # Try: p len(values), p score, then c.
    print('Score:', score)


if __name__ == '__main__':
    main()
