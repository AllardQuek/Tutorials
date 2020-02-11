"""Web crawling script

Python script to automatically crawl info from 3 recognised open sources
using Beautiful Soup/Scrapy.

"""


from bs4 import BeautifulSoup

from requests import get

url = get("https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware")

# Another parser could be 'html.parser' which is not as fast (need to install lxml)
soup = BeautifulSoup(url.content, 'lxml')

divs = soup.find_all('div', class_='ContainerListTitle1')

for div in divs:
    titles = div.find_all('a')
    # print(titles)
    for title in titles:
        print(title.text)


# if __name__ == "__main__":
#     main()