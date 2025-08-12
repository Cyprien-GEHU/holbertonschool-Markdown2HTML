#!/usr/bin/python3

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    path_readme = sys.argv[1]
    path_html = sys.argv[2]

    if not os.path.isfile(path_readme):
        sys.stderr.write(f"Missing {path_readme}\n")
        exit(1)

    exit(0)
