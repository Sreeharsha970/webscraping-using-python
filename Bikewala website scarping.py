import requests
from bs4 import BeautifulSoup
import csv

#scarping data website link that is url
url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)
#print(page)
#that website page passes into beautifulsoup
soup=BeautifulSoup(page.content,'html.parser') 
#print(soup)                              # this part is text scraping

#image link  scraping (that line is total image div class )

img1=[]
image=soup.findAll('div',class_="o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI")
print(image)
# for i in image:
#     j=i.img['src']
#     img1.append[j]
# print(img1) 

# image down bike discripption links scarping (that link is total bike rate div class)

'''links=[]
link=soup.findAll('div',class_='o-fznVCs o-fHmpzP o-fzptZB')
#print(link)
for i in link:
    j=i.a['href']
    links.append(j)
print(link)'''

#text link scarping (means rates)
'''links=[]
link=soup.findAll('div',class_='o-Hyyko o-bPYcRG o-eqqVmt')
print(link)'''
# for i in link:
#     j=i.a.text
#     links.append(j)
# print(links)

#using csv we have to store the data
# with open('il.csv','w') as csv_file:
#     write=csv.writer(csv_file)
#     write.writerow(image)
#     for i in image:
#         j=i.img['src']
#         img1.append(j)
#     write.writerow(img1)


