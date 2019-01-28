""" This script extracts web URLs from HTML-esque files and outputs
a list of unique URLs in a cleaned format .txt file.
"""

import sys
import re


def get_unique(xs):
    seen = set()
    return [x for x in xs if not (x in seen or seen.add(x))]

if __name__ == '__main__':
    args = sys.argv
    if not 1 < len(args) < 4:
        print("Error, incorrect arguments")
        print("$ extract.py <filepath> [<outfile>]")
        sys.exit(1)
    fname = args[1]
    if len(args) == 3:
        outname = args[2]
    else:
        outname = None

    print(f"Extracting URLs from '{fname}'")

    dump = ""
    with open(fname, 'r') as file:
        for line in file:
            dump += line

    data = re.split("[<\"' >]", dump)
    matches = []
    for frag in data:
        match = re.search('[h][t][t][p][s]*[:][/][/]', frag)
        if match is not None:
            matches.append(match.string[match.start():])

    uniques = get_unique(matches)

    if outname is not None:
        print(f"Saving output to '{outname}'")
        with open(outname, 'w') as file:
            for u in uniques:
                file.write(u+"\n")
        print("Done")
        sys.exit()
    else:
        for u in uniques:
            print(u)
        sys.exit()
