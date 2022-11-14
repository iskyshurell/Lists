import os


class File:
    def __init__(self, name: str, mode: str) -> None:
        self._file_name = name
        self._mode = mode

    def __enter__(self):
        if os.path.exists(self._file_name):
            return open(self._file_name, self._mode)

        else:
            return open(self._file_name, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True



with File("doc.txt", "a") as file1:
    file1.write("Hello world")
