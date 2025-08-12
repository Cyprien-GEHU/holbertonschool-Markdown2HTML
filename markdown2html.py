#!/usr/bin/python3
""" markdown to html """
import sys
import os

def main():
    """ the main function of the programm"""
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    path_readme = sys.argv[1]
    path_html = sys.argv[2]

    if not os.path.isfile(path_readme):
        sys.stderr.write(f"Missing {path_readme}\n")
        exit(1)

    with open(path_readme, 'r') as f_read, open(path_html, 'w') as f_wrote:
        for line in f_read:
            if line.startswith('#'):
                num = 0
                while num < len(line) and line[num] == "#":
                    num += 1
                if 1 <= num <= 6 and len(line) > num and line[num] != "#":
                    title = line[num:].strip()
                    f_wrote.write(f"<h{num}>{title}</h{num}>\n")
    
    
    exit(0)


if __name__ == "__main__":
    main()
