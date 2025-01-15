#!/usr/bin/env python
import pathlib
import shutil


def remove_folder(folder_path: str) -> None:
    folder = pathlib.Path(folder_path)
    shutil.rmtree(folder)


def remove_file(file_path: str, missing_ok: bool = False) -> None:
    file = pathlib.Path(file_path)
    file.unlink(missing_ok=missing_ok)


if __name__ == "__main__":
    if "{{ cookiecutter.scripts }}" != "true":
        remove_folder(".scripts")

    if "{{ cookiecutter.with_docker }}" != "true":
        remove_folder("docker")

    if "{{ cookiecutter.with_build }}" != "true":
        remove_file(".github/workflows/release-pr-cleanup.yaml")
        remove_file(".github/workflows/release-pr.yaml")
        remove_file(".github/workflows/release-scan.yaml")
        remove_file(".github/workflows/release.yaml")

    # Remove files from older versions
    remove_file(".husky/.huskyrc", missing_ok=True)
