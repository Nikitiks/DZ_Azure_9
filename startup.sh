#!/bin/bash

python manage.py migrate core

gunicorn --bind=0.0.0.0 --timeout 600 project.wsgi