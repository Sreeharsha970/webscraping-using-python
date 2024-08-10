import requests
from bs4 import BeautifulSoup
import time
import pandas as pd



# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# # }

# # def fetch_amazon_page(url, retries=5):
# #     for _ in range(retries):
# #         response = requests.get(url, headers=headers)
# #         if response.status_code == 200:
# #             return response
# #         elif response.status_code == 503:
# #             print("Service unavailable. Retrying...")
# #             time.sleep(2)  # Wait for 2 seconds before retrying
# #         else:
# #             print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
# #             return None
# #     return None

# # url = "https://www.amazon.in/s?hidden-keywords=B0894MND8N%7CB09JVCT78G%7CB0B6441RNK%7CB0B1J8SXLC%7CB09V7WS4PP%7CB0B6465WX6%7CB08VNJ5BHN%7CB07SVH63PX%7CB09CYX92NB%7CB07SWMGSSV%7CB09HGSCL9Q%7CB0C595L8YZ%7CB08FB396L1%7CB09NCDDM7T%7CB0D45YS7WK%7CB08FB2H6Y4%7CB0C94C4JG9%7CB0BRKVX9XS%7CB09Y8T1GXF%7CB09HGPKY7Q%7CB0C7H7R86X%7CB07SVHCL7H%7CB07ZQKM13W%7CB0C3VYT6Q6%7CB0CXLDSHSH%7CB08FB36CY4%7CB0BRKXHFLD%7CB0CX5BL4R1%7CB09XBH7SMM%7CB0BRKYK4HQ%7CB08FB3DKJ9%7CB0CX5B4N1N%7CB08T8B4RP1%7CB0CX1NHPMG%7CB0CS6PWVJX%7CB08HRWJ8SZ%7CB0CX5BN16V%7CB0CX1NK999%7CB08VN7GW9J%7CB08HRWKKBB%7CB08HRWSYH6%7CB0BRKXF951%7CB0CX5C6WP3&pf_rd_i=1389365031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=b3ad8f07-85a3-4390-a90c-a10ceaf2877b&pf_rd_r=TGFEHRJSGF2PN4A1CTE0&pf_rd_s=merchandised-search-9&ref=AF_WIN_bub_w_cml_t_2"
# # response = fetch_amazon_page(url)

# # if response:
# #     soup = BeautifulSoup(response.content, 'html.parser')
# #     titles = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
    
# #     if titles:
# #         title = [i.get_text() for i in titles[:20]]
# #         print(title)
# #     else:
# #         print("No titles found. Check the HTML structure or class names.")
# # else:
# #     print("Failed to retrieve the webpage after multiple attempts.")

response=requests.get("https://www.amazon.in/s?hidden-keywords=B09JWL7FKV%7CB0CHYG1DB1%7CB0CGRHHGBH%7CB0D7C1SSV8%7CB0CGRKKR6X%7CB0BVFKWNRK%7CB0B4DKKKF6%7CB01L2CPPH2%7CB09ZJXBB4Z%7CB08FRSB1CM%7CB0755G21GJ%7CB0813WGPH7%7CB092RK7H4C%7CB00F19Q7YI%7CB08SHZ2BL3%7CB01GCKO9Z8&pf_rd_i=1388977031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=ac570985-b127-4219-b095-10904eec97bf&pf_rd_r=W0WJBPPHSM46S6E0WMS8&pf_rd_s=merchandised-search-6&ref=AF_WIN_bub_w_cml_t_5")
#print(response)

soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
    
    if titles:
        title = [i.get_text() for i in titles[:20]]
        #print(title)
    else:
        print("No titles found. Check the HTML structure or class names.")
else:
    print("Failed to retrieve the webpage after multiple attempts.")


if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    prices = soup.find_all('span', class_="a-price-whole")
    
    if prices:
        price = [i.get_text() for i in prices[:20]]
        #print(price)
    else:
        print("No prices found. Check the HTML structure or class names.")
else:
    print("Failed to retrieve the webpage after multiple attempts.")


if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img', class_="s-image")
    
    if images:
        image_urls = [img['src'] for img in images[:20]]
        print(image_urls)
    else:
        print("No images found. Check the HTML structure or class names.")
else:
    print("Failed to retrieve the webpage after multiple attempts.")


