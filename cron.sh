#!/bin/bash
# This is a Django, Project-specific Cron script.
# Separate Projects would need a copy of this script 
# with appropriate Settings export statments.

PYTHONPATH="${PYTHONPATH}:~/projects/bits/"
export PYTHONPATH
export DJANGO_SETTINGS_MODULE=bits.settings

python ~/projects/bits/bits/cron.py