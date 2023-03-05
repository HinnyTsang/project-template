#!/usr/bin/env python
"""
Logger template for the project
"""
import logging
import logging.config
import yaml


# Read the config file
with open("src/logging/config.yaml", "r", encoding="utf-8") as stream:
    config = yaml.safe_load(stream)

# Apply the configuration
logging.config.dictConfig(config)

# Create a logger instance
logger = logging.getLogger("project-logger")
