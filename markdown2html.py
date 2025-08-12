#!/usr/bin/python3

import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

name = sys.argv[0]
path_readme = Path(sys.argv[1])
path_html = Path(sys.argv[2])

if not path_readme.exists():
    print("Missing README.md")
    exit(1)

if not path_html.exists():
    print("Missing README.html")
    exit(1)

exit(0)