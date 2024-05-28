#!/usr/bin/env sh

python manage.py tailwind install --no-input
python manage.py tailwind build --no-input
python manage.py copy_preline_js
python manage.py collectstatic --noinput 
python manage.py migrate

# exit 123