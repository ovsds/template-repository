#!/usr/bin/env python
import pathlib
import shutil


def remove_folder(folder_path: str) -> None:
    folder = pathlib.Path(folder_path)
    shutil.rmtree(folder)


def remove_file(file_path: str) -> None:
    file = pathlib.Path(file_path)
    file.unlink()


if __name__ == "__main__":
    pass
