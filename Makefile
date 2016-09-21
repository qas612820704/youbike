download:
	python -m scrapers.download

install:
	pip install -r requirements.txt

server:
	python -m server.simple_server

.PHONY: download install server
