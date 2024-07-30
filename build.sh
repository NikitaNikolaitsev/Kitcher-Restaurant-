#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update package list and install system dependencies
apt-get update
apt-get install -y somepackage

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
