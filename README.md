# Recommendations Extractor

This solves a little problem of my own. If you have the same (or a very similar) problem, this may help you somewhat.

## My Little Problem

I use [IFTTT](https://ifttt.com) to send the URLs of media (podcasts, videos, articles, etc.) to an Evernote doc. Sifting through these ifttt-customised links is a mission, so I wanted a way to extract the original URL, the title, and a description from each URL. 

I can export the Evernote file in HTML format. From there, this Python 3 code makes use of regular expressions, basic string/file processing, and the awesome [requests](https://github.com/requests/requests) library to extract the URLs and retrieve their information — writing the output to a .txt file of the user's choice.

## Example

Input

```html
<div>via Pocket <a href="http://ift.tt/12iIegy">http://ift.tt/12iIegy</a></div>

```

Intermediary

```
http://ift.tt/12iIegy
```

Output

```
Bill Gates’ five favorite books of 2014
For the business-minded bookworm in your life.
https://qz.com/308144/bill-gates-five-favorite-books-of-2014/
[http://ift.tt/12iIegy]

```

## Usage

```python
python3 extract.py <exported_recommendations_html> urls.txt
python3 fetch.py urls.txt <formatted_output_txt>
```
