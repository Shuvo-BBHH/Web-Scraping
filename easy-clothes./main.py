from mahdix import *
clear()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import requests,csv,csv
from concurrent.futures import ThreadPoolExecutor as ThreadPool
driver=webdriver.Chrome()
driver.get('https://easy-clothes.com/en/38-necklace')
sleep(10)
source=driver.page_source
sop=bs(source,'html.parser')
find_a=sop.find_all('a',class_='product-miniature__thumb-link')
def h_text(test):
    sop3=bs(test,'html.parser')
    return sop3
def gather_data(url_p):
    try:

        get_data_product=requests.get(url_p).text
        sopx=h_text(get_data_product)
        price=sopx.find('span',class_='price').text.strip()
        titel_product=re.search('"item_name":"(.*?)"', str(sopx)).group(1)
        description=sopx.find('div',class_='product-description')
        description = sopx.find('div', {'class': 'description-content'}).get_text(strip=False).replace(' ','')
        pattern = r'"image":\s*\[([^\]]*)\]'
        matches = re.search(pattern, get_data_product)
        if matches:
            matched_content = matches.group(1)
            image_urls = re.findall(r'"([^"]*)"', matched_content)
        else:
            print("No matches found.")
        input_elements = sopx.find_all('input', {'class': 'input-radio'})
        titles = [input_element['title'] for input_element in input_elements]
        # Print the result
        print(titles)
        print(f'Name : {titel_product}   price {price}')
        print(f'URl : {url_p}')
        print(image_urls)
        print(mahdilinx())
        breadcrumb_ul = sopx.find('div', class_='breadcrumb')
        if breadcrumb_ul:
            breadcrumb_text = '/'.join([text.strip() for text in breadcrumb_ul.stripped_strings])
            print(breadcrumb_text)
        else:
            print("No element with class 'breadcrumb' found.")

        Google_chatagory='Accueil/Sacs & Accessoires/Colliers'
        Category='SACS & ACCESSOIRES'
        with open(csv_filename, mode='a', encoding='utf-8', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([titel_product, price, url_p, image_urls, description, titles,breadcrumb_text,Category,
                                 ])
    except:pass
csv_filename='data.csv'
with open(csv_filename, mode='a', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
'Handle',
'Title',
'Product category',
'Type',
'Variant price',
'Image src',
'Seo Title',
'Seo description',
'Google shopping/product category',

    ])
for link in set(find_a):
    url_p=link['href']
    with ThreadPool(max_workers=100) as ahare:
        ahare.submit(gather_data,url_p)
    # open('link.txt','a',encoding='utf-8').write(f'{str(url_p)}\n')

