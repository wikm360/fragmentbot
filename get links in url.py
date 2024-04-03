import requests
from bs4 import BeautifulSoup as BS
import re
def not_lacie(href):
    return href and not re.compile("lacie").search(href)

url = 'https://soft98.ir'
r = requests.get(url)
content = r.text
soup = BS(content,'html.parser')
elem = list(soup.find_all(href=not_lacie))
count = len(elem)
for i in range(0,count) :
    li = str(elem[i]).split(" ")
    count2 = len(li)
    for j in range(0,count2) : 
        if "href" in li[j] :
            links = str(li[j]).split("=")
            count3 = len(links)
            for z in range(0,count3) :
                if "soft98.ir" in links[z] :
                    final = str(links[z])
                    print(final) 

