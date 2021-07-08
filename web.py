import requests
from bs4 import BeautifulSoup
import bs4

res = requests.get('https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=remote')
print(res.status_code)
html = res.text
soup = BeautifulSoup(html, "html.parser")
div = soup.find('div', {'id':'TableWithRules'})
tds = div.findAll('td')
# for td in tds :
for td in tds:
    print(td[i].a.string)
    print("-------------")


# headers = div.findAll('header')
# for div in headers:
#     details = div.find('div', {'class': "details"})
#     print(details)

#     # res2 = requests.get(movieUrl)
#     # html = res2.text
#     # soup2 = BeautifulSoup(html, 'html.parser')
#     # info = soup2.find('div', {'class': 'subtext'})

#     # a = info.findAll('a')
#     # print(td.a.string)
#     # print(info.time.string.strip())
#     # print(a[0].string.strip())
#     # print(a[1].string.strip())



