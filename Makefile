.PHONY: api

requirements.txt: requirements-raw.txt
	pip-compile $< -o $@

_envs/key_features: about/key_features-requirements.txt
	python -m venv $@
	pip install -r @<

_freeze/about/key_features: about/key_features.qmd _envs/key_features
	source _envs/key_features/bin/activate
	quarto render @<

build: api
	python -m quartodoc build --verbose
	quarto render
