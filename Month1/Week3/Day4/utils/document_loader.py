"""
Utility functions for loading different document formats.
"""

import json
import os

import pymupdf4llm


def load_txt(file_path):
    """
    Load text from a TXT file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_pdf(file_path):
    """
    Convert PDF into plain text using pymupdf4llm.
    """

    return pymupdf4llm.to_markdown(file_path)


def load_json(file_path):
    """
    Load a JSON file and return it as formatted text.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return json.dumps(data, indent=2)


def load_document(file_path):
    """
    Automatically detect file type and load it.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        return load_txt(file_path)

    if extension == ".pdf":
        return load_pdf(file_path)

    if extension == ".json":
        return load_json(file_path)

    raise ValueError(f"Unsupported file type: {extension}")


if __name__ == "__main__":
    document = load_document("data/sample.txt")
    print(document[:500])