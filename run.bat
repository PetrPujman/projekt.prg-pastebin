@echo off
docker compose run --rm django python manage.py %*
