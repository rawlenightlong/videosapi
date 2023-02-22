#!/usr/bin/env bash

set -o errexit

pip install -r dependencies.txt

python3 manage.py migrate