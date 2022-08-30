.PHONY: api


_envs/key_features: about/key_features-requirements.txt
	python -m venv $@
	pip install -r @<

_freeze/about/key_features: about/key_features.qmd _envs/key_features
	source _envs/key_features/bin/activate
	quarto render @<

api:
	cd _api && mkdocs build -d ../api

build: api
	quarto render
