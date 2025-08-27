.PHONY: help install download serve

help:
	@LC_ALL=C $(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/(^|\n)# Files(\n|$$)/,/(^|\n)# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | grep -E -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pip install -r requirements/requirements-model.txt
	pip install -r requirements/requirements-server.txt
	pip install -r requirements/requirements-app.txt

download:
	python src/_helpers/download.py

serve:
	docker-compose up -d model_server
