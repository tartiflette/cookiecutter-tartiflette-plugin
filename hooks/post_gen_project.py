#!/usr/bin/env python
import os

from typing import List, Union

_PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def _remove_files(files: Union[List[str], str]) -> None:
    """
    Removes the list of files provided.
    :param files: list of filepath to remove
    :type files: Union[List[str], str]
    """
    if not isinstance(files, list):
        files = [files]

    for filepath in files:
        os.remove(os.path.join(_PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        _remove_files("AUTHORS.md")

    if "{{ cookiecutter.use_docker }}" != "y":
        _remove_files([
            ".dockerignore",
            "docker-compose.override.yml",
            "docker-compose.yml",
            "Dockerfile",
        ])

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        _remove_files("LICENSE")
