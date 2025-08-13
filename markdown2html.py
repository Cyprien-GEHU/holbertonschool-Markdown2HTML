#!/usr/bin/python3
""" markdown to html """
import sys
import os


def main():
    """ the main function of the programm"""

    my_html = []
    isList = False
    tag = None

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
                if isList:
                    my_html.append(f"</{tag}>")
                    tag = None
                    isList = False

                num = 0
                while num < len(line) and line[num] == "#":
                    num += 1
                if 1 <= num <= 6 and len(line) > num and line[num] != "#":
                    title = line[num:].strip()
                    my_html.append(f"<h{num}>{title}</h{num}>")

            elif line.startswith('-'):
                content = line[1:].strip()
                if not isList:
                    isList = True
                    my_html.append("<ul>")
                    tag = "ul"
                elif isList and tag != "ul":
                    my_html.append(f"</{tag}>")
                    my_html.append("<ul>")
                    tag = "ul"
                my_html.append(f"\t<li>{content}</li>")

            elif line.startswith('*'):
                content = line[1:].strip()
                if not isList:
                    isList = True
                    my_html.append("<ol>")
                    tag = "ol"
                elif isList and tag != "ol":
                    my_html.append(f"</{tag}>")
                    my_html.append("<ol>")
                    tag = "ol"
                my_html.append(f"\t<li>{content}</li>")

        if isList:
            my_html.append(f"</{tag}>")

        for lh in my_html:
            f_wrote.write(f"{lh}\n")
    exit(0)


if __name__ == "__main__":
    main()
