# flipcart modules 
# Beautifulsoup , Requests , Csv , pandas

#importing modules
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
#scarping the data

response=requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme")
#print(response)
soup = BeautifulSoup(response.content,'html.parser') #Total webpage content will appear,
# the total data is in html , we have to take html parser, parser means it defines class
#print(soup)
# html unstructured data will changes to structured data it means readable format

# 1. First start with title , Scraping the title data ,inspect link have to copy
names = soup.find_all('div',class_="KzDlHZ")
name = []
#print(names)
# the names of the mobiles will not get in structrued format,

for i in names[0:20]:
    d=i.get_text()
    name.append(d)
#print(name)
# Now the data is in reable format

# 2. second start scarping with price
prices = soup.find_all('div',class_="Nx9bqj _4b5DiR")
price = []

for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
#print(price)  

# 3.scraping thr ratings
rates = soup.find_all('div',class_="XQDdHH")
rate = []

for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))
#print(rate)

#4.scraping the images
images = soup.find_all('img',class_="DByuf4")
image = []

for i in images[0:20]:
    d=i['src']          #src is a attribute in image class
    image.append(d)
#print(image)

# 5.scraping links ,links are in a tag means anchor tag
links = soup.find_all('a',class_="CGtC98")
link = []

for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']       #href is a attribute in anchor tag
    link.append(d)
#print(link)


df=pd.DataFrame()     #dataframe contain rows and columns
df["Names"]=name      #title name
df["prices"]=price    #price name
df["Ratings"]=rate    #ratings
df["Images"]=image    #Images
df["Links"]=link      #links

#print(df)
df.to_csv("Mobiles.csv")

#The use of web scraping is collecting all the data amd creating a own website
#Explore about bug bounty, Explore about twillo sms 
#bikewala,imdb,zigwheels.