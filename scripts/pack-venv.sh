#!/bin/bash

# Export the dependencies to a requirements.txt file
poetry export -f requirements.txt --output requirements.txt

# Create a new virtual environment and install the dependencies:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Pack the virtual environment to a zip file
zip -r venv.zip venv/