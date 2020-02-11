"""Web crawling script

Python script to automatically crawl info from 3 recognised open sources
using Beautiful Soup/Scrapy.

"""


from bs4 import BeautifulSoup

from requests import get

url = get("https://www.virustotal.com/gui/search/emotet/comments")

# Another parser could be 'html.parser' which is not as fast (need to install lxml)
soup = BeautifulSoup(url.content, 'html.parser')
# print(soup.prettify())
hash_links = soup.find_all('vt-virustotal-app')

for hash_link in hash_links:
    print(hash_link)
    print(hash_link.contents)

