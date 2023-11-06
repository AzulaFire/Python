from pathlib import Path
import urllib.request
import urllib
import imghdr
import posixpath
import re

# headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
           'AppleWebKit/537.11 (KHTML, like Gecko) '
           'Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}


def getImageURL(query):

    # Parse the page source and download pics
    request_url = 'https://www.bing.com/images/async?q=' + urllib.parse.quote_plus(query) \
        + '&first=' + str(1) + '&count='
    request = urllib.request.Request(request_url, None, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf8')
    if html == "":
        print("[%] No more images are available")
    links = re.findall('murl&quot;:&quot;(.*?)&quot;', html)

    for link in links:
        if not 'redd.it' in link:
            path = urllib.parse.urlsplit(link).path
            filename = posixpath.basename(path).split('?')[0]
            file_type = filename.split(".")[-1]
            print(f'IMAGE PATH: {link}')
            print(f'FILE TYPE: {file_type}\n')
            if file_type.lower() in ["jpeg", "png", "jpg"]:
                print(link)
                return link
                break
