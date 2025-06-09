import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import get_text_chunks


def test_get_text_chunks_respects_chunk_size():
    lines = ["a" * 50 for _ in range(100)]
    sample_text = "\n".join(lines)
    chunks = get_text_chunks(sample_text)
    assert chunks, "Expected non-empty list of chunks"
    assert all(len(chunk) <= 1000 for chunk in chunks)
