.PHONY: help install download

help:
	@LC_ALL=C $(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/(^|\n)# Files(\n|$$)/,/(^|\n)# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | grep -E -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	if [ ! -d "~/.virtualenvs/translation" ]; then python -m venv ~/.virtualenvs/translation fi
	. ~/.virtualenvs/translation/bin/activate
	pip install -r requirements.txt

download:
	python src/download.py
