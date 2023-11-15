#!/bin/sh

docker compose run --rm django python ./manage.py $*
