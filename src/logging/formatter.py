#!/usr/bin/env python
"""
Formatter template for the project
"""
import logging


class ColoredFormatter(logging.Formatter):
    """ColoredFormatter Custom color formatter for the project

    :param logging:
    :type logging:
    """

    def __init__(self, fmt=None, datefmt=None, style='%', colors=None):
        super().__init__(fmt, datefmt, style)
        self.colors = colors or {}

    def format(self, record):
        levelname = record.levelname
        if levelname in self.colors:
            record.levelname = f"\033[{self.colors[levelname]}m{levelname}\033[0m"
        return super().format(record)
