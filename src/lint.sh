#!/bin/bash
set -e
flake8 . --exclude=migrations,apps.py,settings,__init__.py,.venv