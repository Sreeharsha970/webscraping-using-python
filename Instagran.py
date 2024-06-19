from bs4 import BeautifulSoup
import requests
import instaloader 

URL = "https://www.instagram.com/"

def parse_data(s):
    data={}               #data take as dictionary format
    
    s=s.split("-")[0]
    
    s=s.split("")
    
    data['Followers']=s[0]
    data['Following']=s[2]
    data['posts']=s[4]
    return data


#scarping data
def scrape_data(username):
    r=requests.get(URL.format(username))
    s=BeautifulSoup(r.text,"html.parser")
    meta=s.find("meta",property="og:description")   #attributes
    return parse_data(meta.attrs['content'])

if __name__=="__main__":
    print(30*"=", "Instagram",30*"=") 
    username=input("enter the Id:") 
    data=scrape_data(username)         #function call
    print()
    print(username,"having",data["followers"],"followers")
    print(username,"having",data["following"],"following")
    print(username,"having",data["posts"],"posts")
    print(65*"=")
    
harsha=instaloader.Instaloader 

harsha.download_profile(username,profile_pic_only=True) 
        