##------------------------------------#
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =' MAHDI HASAN'
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =  'MAHDI HASAN'
___V___= 1
__WHATSAPP___=+8801616406924
# YOU Must RUN pip install mahdix Beafore Run THIS 
#-----------------------------------------------------------------#
# Website : https://www.nike.com/
# GET ALL shoes DATA like 'Product Name', 'Product Price', 'Product Type', 'Color Description', 'Reviews Count', 'Product URL' 
# Save as all data  in CSV file 
#-------------------------------------------------------------------#
import os
try:
    import requests,re,csv
    from mahdix import *
    from datetime import datetime
    from mahdix import html as bs
    from concurrent.futures import ThreadPoolExecutor
    from time import sleep as slp
    import scrapy
    import pandas as pd
except:
    os.system('pip insatll mahdix')
    os.system('pip insatll requests')
    os.system('pip insatll bs4')

clear()
logo=mahdi_logo
def main():
    clear()
    print(logo)
product_total=[]



def main():
    all_url=[]
    global csv_file_path
    # url='https://www.nike.com/w/mens-shoes-nik1zy7ok'
    clear()
    print(logo)
    url=input(f'{LI_WHITE}Input Url : ')
    print(mahdilinx())
    save_as = input(f'Name of CSV file: {LI_YELLOW}')
    csv_file_path = 'output.csv' if not save_as else save_as

    if not csv_file_path.endswith('.csv'):
        print('File name should end with ".csv"')
        csv_file_path='output.csv' 
    else:
        # Add your mahdix module functionality here using csv_file_path
        print(f'Processing {csv_file_path}...')
    headers = ['Product Name', 'Product Price', 'Product Type', 'Color Description', 'Reviews Count', 'Product URL']

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(headers)

    def find_product(url):
        responce=requests.get(url).text
        sop=bs(responce,'html.parser')
        for link in sop.find_all('a'):
            all_link=link['href']
            all_url.append(all_link)
        for p_link in set(all_url):
            if 'https://www.nike.com/t/' in p_link:
                responce=requests.get(p_link).text
                sop=bs(responce,'html.parser')

                product_title_element = sop.find('h1', {'id': 'pdp_product_title'})
                product_title = product_title_element.text if product_title_element else None

                # Extract Product Price
                product_price_element = sop.find('div', {'class': 'product-price'})
                product_price = product_price_element.text if product_price_element else None

                # Extract Product Sub Title
                product_sub_title_element = sop.find('h2', {'class': 'headline-5', 'data-test': 'product-sub-title'})
                product_sub_title = product_sub_title_element.text if product_sub_title_element else None

                color_description_element = sop.find('li', {'class': 'description-preview__color-description'})

                # Extract the text content of the element
                color_description = color_description_element.text if color_description_element else None

                reviews_count_match = re.search(r'Reviews \((\d+)\)', str(sop))

                # Extract the number if the match is found
                reviews_count = reviews_count_match.group(1) if reviews_count_match else None
                # Print the results

                print(f"""[{len(product_total)}] Product Name: {product_title}
{LI_GREEN}Product Price: {LI_YELLOW}{product_price}
{LI_WHITE}Product Typs: {product_sub_title}
color description : {color_description}
Reviews : {reviews_count}
Product URL: {p_link}""")
                    # Append Product Title to the product_total list
                product_total.append(product_title)
                write_to_csv([product_title, product_price, product_sub_title, color_description, reviews_count, p_link])
                print(mahdilinx())

            if 'https://www.nike.com/w/' in p_link:
                if 'shoes' in p_link:
                    with ThreadPoolExecutor(max_workers=50) as sub:
                        sub.submit(find_productxx,p_link)
            else:pass
    find_product(url)

def find_productxx(url):
        all_url=[]
        responce=requests.get(url).text
        sop=bs(responce,'html.parser')
        for link in sop.find_all('a'):
            all_link=link['href']
            all_url.append(all_link)
        for p_link in set(all_url):
            try:
                if 'https://www.nike.com/t/' in p_link:
                    responce=requests.get(p_link).text
                    sop=bs(responce,'html.parser')

                    product_title_element = sop.find('h1', {'id': 'pdp_product_title'})
                    product_title = product_title_element.text if product_title_element else None

                    # Extract Product Price
                    product_price_element = sop.find('div', {'class': 'product-price'})
                    product_price = product_price_element.text if product_price_element else None

                    # Extract Product Sub Title
                    product_sub_title_element = sop.find('h2', {'class': 'headline-5', 'data-test': 'product-sub-title'})
                    product_sub_title = product_sub_title_element.text if product_sub_title_element else None

                    color_description_element = sop.find('li', {'class': 'description-preview__color-description'})

                    # Extract the text content of the element
                    color_description = color_description_element.text if color_description_element else None

                    reviews_count_match = re.search(r'Reviews \((\d+)\)', str(sop))

                    # Extract the number if the match is found
                    reviews_count = reviews_count_match.group(1) if reviews_count_match else None
                    # Print the results
                    print(linex())
                    print(f"""[{len(product_total)}] Product Name: {product_title}
{LI_GREEN}Product Price: {LI_YELLOW}{product_price}
{LI_WHITE}Product Typs: {product_sub_title}
color description : {color_description}
Reviews : {reviews_count}
Product URL: {p_link}""")
                    product_total.append(product_title)
                write_to_csv([product_title, product_price, product_sub_title, color_description, reviews_count, p_link])
            except:pass


def write_to_csv(data):
    # csv_file_path = 'output.csv'
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
main()
