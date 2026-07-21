"""
Utility functions for splitting documents into overlapping chunks.
"""

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into overlapping character-based chunks.
    """

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size.")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == text_length:
            break

        start = end - overlap

    return chunks