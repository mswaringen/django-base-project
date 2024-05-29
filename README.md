# Django Base Project Template

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

License: MIT

## Includes

- Cookiecutter Django
- Tailwind CSS (via django-tailwind) + Preline CSS
- Configured to deploy on Fly.io (PG, Redis, Celery workers, Tigris S3 storage)

## Run locally in Docker

```
export COMPOSE_FILE=docker-compose.local.yml
docker-compose build
docker-compose up -d
```

### Run Tailwind watcher
```
docker-compose run --rm django python manage.py tailwind start
```

## Deploy to Fly.io

### Build production files
```
docker-compose run --rm django python manage.py tailwind build
```

### Copy updated preline.js to static dir
```
docker-compose run --rm django python manage.py copy_preline_js
```


### Launch wizard
```
fly launch
```
```
- YES to copy config to new app
- NO to overwriting Dockerfile
- YES to modifying configuration, click to open setting page, select Postgres, Redis, Tigris
```

### Export secrets to fly
```
cat .envs/.production/.django | fly secrets import
```
### First Deploy
```
fly deploy
```
### Remote consol access
```
fly ssh console
```

### More info
https://sweezy.dev/deploying-cookiecutter-django-on-flyio.html

