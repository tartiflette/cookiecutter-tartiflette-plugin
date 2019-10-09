# Cookiecutter Tartiflette Plugin

[Cookiecutter](https://github.com/audreyr/cookiecutter) template to bootsrap a Tartiflette plugin.

## Features

* [`gazr`](https://gazr.io) specification
* Testing setup with [`pytest`](https://github.com/pytest-dev/pytest)
* Docker support using [`docker-compose`](https://github.com/docker/compose) for development

## Usage

Install the latest [Cookiecutter](https://github.com/audreyr/cookiecutter) if you haven't installed it yet:
```
$ pip install -U cookiecutter
```

Generate a Tartiflette plugin project with the following command:
```
$ cookiecutter https://github.com/tartiflette/cookiecutter-tartiflette-plugin.git
```

You'll be prompted for some values. Fill them to create your Tartiflette plugin project.

Once your Tartiflette plugin project created, enter it:
```
$ cd <your-directory>
$ git init
$ git add .
$ git commit -m "Initial commit"
$ git remote add origin <your-github-repository>
$ git push -u origin master
```

If you didn't choose to use the `Docker` support, don't forget to create a
dedicated virtual environment and to install all the development dependencies
(if you chose the to use the `Docker` support this step isn't mandatory):
```
$ pip install -e ".[test]"
```

Now, you can work on your plugin and use all of the pre-defined `Makefile` targets:
```
$ make clean
$ make format
$ make style
$ make complexity
$ make test
$ make security-sast
```

## TODO

* Pre-configured version bumping with a single command through [`bump2version`](https://github.com/c4urself/bump2version)
* Setup a default [`Travis-CI`](https://travis-ci.org) configuration
* Auto-release to [`PyPI`](https://pypi.python.org/pypi) when you push a new tag to master (optional)
* Setup an optional project example using the plugin
* Setup a default configuration for [`dependabot`](https://github.com/marketplace/dependabot-preview)
* Improve the default `README.md` with an "How to use" example
