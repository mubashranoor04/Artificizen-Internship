import os

import pymupdf4llm



def load_document(file_path):

    extension = (
        os.path.splitext(file_path)[1]
        .lower()
    )


    if extension == ".pdf":

        text = pymupdf4llm.to_markdown(
            file_path
        )

        return text



    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()



    else:

        raise ValueError(
            "Unsupported file format"
        )