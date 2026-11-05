"""Run inside ai-dev to check PyTorch, service DNS, and mounted storage."""

import json
from pathlib import Path
from urllib.request import urlopen

import torch

assert torch.__version__.startswith("2.6.0"), torch.__version__
print(f"PyTorch: {torch.__version__}; CUDA available: {torch.cuda.is_available()}")

for url in ("http://qdrant:6333/collections", "http://api:5000/health"):
    with urlopen(url, timeout=10) as response:
        result = json.load(response)
    assert result["status"] == "ok", result
    print(f"{url}: {json.dumps(result)}")

for directory in ("/models", "/data"):
    marker = Path(directory) / "lesson07-persistence.txt"
    if marker.exists():
        assert marker.read_text() == "Lesson 7 persistent storage\n"
        print(f"Existing marker survived: {marker}")
    else:
        marker.write_text("Lesson 7 persistent storage\n")
        print(f"Created marker: {marker}")
