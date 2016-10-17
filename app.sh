#!/bin/sh
python3 -m scrapers.download &
python3 -m server.simple_server
