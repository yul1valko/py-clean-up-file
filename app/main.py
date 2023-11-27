from __future__ import annotations
import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        if self.filename:
            self.file = open(self.filename, "w")
            return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        if self.file:
            self.file.close()
            os.remove(self.filename)
