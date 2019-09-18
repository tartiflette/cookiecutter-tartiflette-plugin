import os
import subprocess
import sys

from setuptools import find_packages, setup

_TEST_REQUIRE = [
    "pytest==4.5.0",
    "pytest-cov==2.6.1",
    "pytest-asyncio==0.10.0",
    "pylint==2.3.0",
    "xenon==0.5.5",
    "black==18.9b0",
    "isort==4.3.4",
]

_VERSION = "0.0.1"

_PACKAGES = find_packages(exclude=["tests*"])


def _read_file(filename):
    with open(filename) as afile:
        return afile.read()


setup(
    name="tartiflette-plugin-{{cookiecutter.plugin_package_name}}",
    version=_VERSION,
    description="{{cookiecutter.short_description}}",
    long_description=_read_file("README.md"),
    long_description_content_type="text/markdown",
    url="{{cookiecutter.project_url}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    license="{{cookiecutter.license}}",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="graphql protocol api tartiflette",
    packages=_PACKAGES,
    install_requires=["tartiflette>={{cookiecutter.tartiflette_version}}"],
    tests_require=_TEST_REQUIRE,
    extras_require={"test": _TEST_REQUIRE},
    include_package_data=True,
)
