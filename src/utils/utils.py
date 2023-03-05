#!/usr/bin/env python
"""
Formatter template for the project
"""
from pathlib import Path


def get_root() -> Path:
    """get_root Get root path of the project

    :return: _description_
    :rtype: Path
    """
    return Path(__file__).parent.parent.parent
