#!/usr/bin/env bash

set -o errexit

#modify
pip install -r requirements.txt


# convert satic assest files
python  manage.py collectstatic --no-input

#
python manage.py migrate