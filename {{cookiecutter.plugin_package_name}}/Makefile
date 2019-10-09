{% if cookiecutter.use_docker != "y" -%}
.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info


.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -frv {} +
	find . -name '*~' -exec rm -f {} +


.PHONY: clean
clean: clean-build clean-pyc
{%- else -%}
COMPOSE = docker-compose -p {{ cookiecutter.plugin_slug }}


.PHONY: clean
clean:
	$(COMPOSE) down --volumes --rmi=local
{%- endif %}


.PHONY: format-imports
format-imports:
{%- if cookiecutter.use_docker != "y" %}
	isort -rc {{ cookiecutter.plugin_slug }}/. tests/. setup.py
{%- else %}
	$(COMPOSE) build format-imports
	$(COMPOSE) run format-imports
{%- endif %}


.PHONY: format
format: format-imports
{%- if cookiecutter.use_docker != "y" %}
	black -l 79 --target-version py36 {{ cookiecutter.plugin_slug }} tests setup.py
{%- else %}
	$(COMPOSE) build format
	$(COMPOSE) run format
{%- endif %}


.PHONY: check-imports
check-imports:
{%- if cookiecutter.use_docker != "y" %}
	isort --check-only -rc {{ cookiecutter.plugin_slug }}/. tests/. setup.py
{%- else %}
	$(COMPOSE) build check-imports
	$(COMPOSE) run check-imports
{%- endif %}


.PHONY: check-format
check-format:
{%- if cookiecutter.use_docker != "y" %}
	black -l 79 --target-version py36 --check {{ cookiecutter.plugin_slug }} tests setup.py
{%- else %}
	$(COMPOSE) build check-format
	$(COMPOSE) run check-format
{%- endif %}


.PHONY: style
style: check-imports check-format
{%- if cookiecutter.use_docker != "y" %}
	pylint --reports=n --rcfile=pylintrc {{ cookiecutter.plugin_slug }} tests setup.py
{%- else %}
	$(COMPOSE) build style
	$(COMPOSE) run style
{%- endif %}


.PHONY: complexity
complexity:
{%- if cookiecutter.use_docker != "y" %}
	xenon --max-absolute B --max-modules B --max-average A {{ cookiecutter.plugin_slug }},setup.py
{%- else %}
	$(COMPOSE) build complexity
	$(COMPOSE) run complexity
{%- endif %}


.PHONY: test-unit
test-unit:{%- if cookiecutter.use_docker != "y" %} clean-pyc{% endif %}
{%- if cookiecutter.use_docker != "y" %}
	mkdir -p reports
	py.test -s tests/unit -vvvvvv --junitxml=reports/report_unit_tests.xml --cov . --cov-config .coveragerc --cov-report term-missing --cov-report xml:reports/coverage_unit.xml $(EXTRA_ARGS)
{%- else %}
	$(COMPOSE) build test-unit
	$(COMPOSE) run test-unit
{%- endif %}


.PHONY: test-functional
test-functional:{%- if cookiecutter.use_docker != "y" %} clean-pyc{% endif %}
{%- if cookiecutter.use_docker != "y" %}
	mkdir -p reports
	py.test -s tests/functional -vvvvvv --junitxml=reports/report_func_tests.xml --cov . --cov-config .coveragerc --cov-report term-missing --cov-report xml:reports/coverage_func.xml $(EXTRA_ARGS)
{%- else %}
	$(COMPOSE) build test-functional
	$(COMPOSE) run test-functional
{%- endif %}


.PHONY: test
test: test-unit test-functional


.PHONY: security-sast
security-sast:
{%- if cookiecutter.use_docker != "y" %}
	bandit -r {{ cookiecutter.plugin_slug }} tests setup.py
{%- else %}
	$(COMPOSE) build security-sast
	$(COMPOSE) run security-sast
{%- endif %}
