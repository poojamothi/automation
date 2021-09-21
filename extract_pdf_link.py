import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup


url = "http://164.100.69.66/jsearch/juddt1page.php?dc=31&fflag=1"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "juddt=20/09/2021&Submit=Submit"


r = requests.post(url, headers=headers, data=data)

content=BeautifulSoup(r.text,'lxml')
all_urls= content.find_all('a')
for url in all_urls:
    try:
        if 'pdf' in url['href']:
            print(url['href'])
    except:
        pass
