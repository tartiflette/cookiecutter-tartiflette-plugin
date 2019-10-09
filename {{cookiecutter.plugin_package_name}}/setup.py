from setuptools import find_packages, setup

_TESTS_REQUIRE = [
    "bandit==1.6.2",
    "pytest==5.2.1",
    "pytest-cov==2.8.1",
    "pytest-asyncio==0.10.0",
    "pylint==2.4.2",
    "xenon==0.6.0",
    "black==19.3b0",
    "isort==4.3.21",
]

_PLUGIN_VERSION = "{{ cookiecutter.plugin_version }}"

_PACKAGES = find_packages(exclude=["tests*"])


def _read_file(filename: str) -> str:
    """
    Reads and returns the content of the file.
    :param filename: filename to read
    :type filename: str
    :return: content of the file
    :rtype: str
    """
    with open(filename) as file:
        return file.read()


{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
} %}


setup(
    name="{{ cookiecutter.plugin_package_name }}",
    version=_PLUGIN_VERSION,
    description="""{{ cookiecutter.plugin_short_description }}""",
    long_description=_read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.repository_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="graphql protocol api tartiflette",
    packages=_PACKAGES,
    python_requires=">=3.6",
    install_requires=["tartiflette{{ cookiecutter.plugin_tartiflette_version }}"],
    tests_require=_TESTS_REQUIRE,
    extras_require={"test": _TESTS_REQUIRE},
    include_package_data=True,
)
