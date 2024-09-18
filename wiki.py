from urllib.error import HTTPError
#from requests.adapters import HTTPAdapter
import requests
from bs4 import BeautifulSoup
import re
import random
import time
from urllib.parse import urljoin
def get_in_link(url):
    r = requests.get(url)
    try:
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        head = soup.find('h1',id="firstHeading")
        inculdes = soup("a", href=re.compile("^(/wiki/)"))
        return head,inculdes
    except HTTPError as H:
        print(H)
        time.sleep(5)
        get_in_link(url)


def getlink(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,'html.parser')
    inculdes=soup("a",href=re.compile("^(/wiki/)"))
    exculdes=soup("a",href=re.compile("^(http|www)"))
    return inculdes,exculdes
def print_link(wkihttps,onther):
    pages = set()
    for wikihttp in wikihttps:
            if 'href' in wikihttp.attrs:
                if wikihttp not in pages:
                    print("in:",wikihttp.attrs['href'])
                    pages.add(wikihttp)
    for wikihttp in onther:
        if 'href' in wikihttp.attrs:
            if wikihttp not in pages:
                print("out:",wikihttp.attrs['href'])
                pages.add(wikihttp)

url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
wikihttps,other = getlink(url)
print_link(wikihttps,other)
random.seed(time.time())
if wikihttps:
    for _ in range(0,10):
        url = urljoin(url, wikihttps[random.randint(0, len(wikihttps) - 1)]['href'])
        h1,h2 = get_in_link(url)
        if h1:
            print(h1.get_text(strip=True),url)
            wikihttps = h2
#if onther:
   # print(getlink(onther[random.randint(0,len(onther)-1)]))
