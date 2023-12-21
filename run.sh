#!/bin/sh

if [ "$1" = "coverage" ]
then
    docker compose run --rm django sh -c 'coverage run manage.py test && coverage report'
else
    docker compose run --rm django python ./manage.py $*
fi
