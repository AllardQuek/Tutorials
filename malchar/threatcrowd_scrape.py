"""Web crawling script

Python script to automatically crawl info from 3 recognised open sources
using Beautiful Soup/Scrapy.

"""

from bs4 import BeautifulSoup
import requests

base_url = "https://www.threatcrowd.org"
emotet_page = "https://www.threatcrowd.org/listMalware.php?page=0&antivirus=emotet"

def write_hashes_to_file(links):
    with open('tc_emotet_md5.txt', 'w+') as f:
        for link in links:
            write_data = f.write(link.text + '\n')


page = requests.get(emotet_page)

# Checking if we successfully fetched the URL
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'lxml')

# Alternatively, using regex: {"href" : re.compile('/malware.php?md5=*')}
hash_links = soup.find_all('a', {'href': lambda L: L and L.startswith('/malware.php?')})



write_hashes_to_file(hash_links)


next_page = soup.find('a', {'href': lambda L: L and L.startswith('/listMalware.php?page=')})
if next_page.text == 'Next':
    next_page_url = base_url + next_page['href']
    print("NEXT URL", next_page_url)
else:
    print("NO MORE NEXT PAGES")








# print(hash_links[0]['href'])

# for link in hash_links:

#     link = base_url + link['href']
#     print(link)
#     hash_url = requests.get(link)
#     hash_soup = BeautifulSoup(page.content, 'lxml')
#     print(hash_soup.head.prettify())
