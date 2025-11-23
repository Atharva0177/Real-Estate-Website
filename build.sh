#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p static/uploads/images
mkdir -p static/uploads/videos
mkdir -p static/uploads/documents

# Initialize database and seed data
python seed_data.py