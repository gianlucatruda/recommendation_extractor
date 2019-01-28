""" This script takes in a list of URLs (extracted by another script)
separated by a newlines and retrieves the title, description, and
nearest URL using requests.
"""

import requests
import extraction
import sys

from requests import RequestException

if __name__ == '__main__':
    args = sys.argv
    if not 1 < len(args) < 4:
        print("Error, incorrect arguments")
        print("$ fetch.py <filepath> [<outfile>]")
        sys.exit(1)
    fname = args[1]
    if len(args) == 3:
        outname = args[2]
    else:
        outname = None

    urls = []
    with open(fname, 'r') as file:
        for line in file:
            urls.append(line[:-1])
    print(f"Exracted {len(urls)} URLs from '{fname}'")

    savefile = False
    if outname is not None:
        file = open(outname, 'w')
        savefile = True

    for i, url in enumerate(urls):
        try:
            print(f"Fetching {i+1} of {len(urls)}: {url} ...")
            r = requests.get(url)
            html_data = r.text
            extracted = extraction.Extractor().extract(html_data)

            title, desc, link = [extracted.title,
                                 extracted.description, extracted.url]
            title = title + "\n" if title is not None else ""
            desc = desc + "\n" if desc is not None else ""
            link = link + f"\n[{url}]\n" if link is not None else f"[{url}]\n"

            print(title)
            if savefile:
                file.write(title + desc + link + "\n")
            else:
                print(desc)
                print(link)
                print("\n")
        except RequestException as e:
            print(f"Ignoring error on {url} and continuing...")
            print(e, end='\n\n')

    file.close()
