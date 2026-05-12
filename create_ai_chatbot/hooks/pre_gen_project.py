#!/usr/bin/env python3
import re
import sys

project_slug = """{{ cookiecutter.project_slug }}"""

if not re.match(r'^[a-z][a-z0-9-]+$', project_slug):
    print(f"ERROR: '{project_slug}' is not a valid slug. Use lowercase letters, numbers, and hyphens only.")
    sys.exit(1)
