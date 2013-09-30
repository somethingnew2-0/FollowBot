#!/usr/bin/env bash

# Install requirements
pip install -r requirements/local.txt
# Copy settings file
cp tweetbot/settings/local-dist.py tweetbot/settings/local.py
# Sync db
python manage.py syncdb
python manage.py migrate
# Blastoff!
python manage.py runserver_plus
