##------------------------------------#
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =' MAHDI HASAN'
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =  'MAHDI HASAN'
___V___= 1
__WHATSAPP___=+8801616406924
# YOU Must RUN pip install mahdix Beafore Run THIS 
#-----------------------------------------------------------#
import os
try:
    import requests,re
    from mahdix import *
    from mahdix import html as bs
    from concurrent.futures import ThreadPoolExecutor
    import scrapy
    import re
    import csv
except:
    os.system('pip insatll mahdix')
    os.system('pip insatll requests')
    os.system('pip insatll bs4')
    os.system('pip insatll scrapy')
    os.system('pip insatll csv')

clear()
logo=mahdi_logo
product_total = []
def find_product(url):
    try:
        response = requests.get(url).text
        sop = bs(response, 'html.parser')

        product_title_element = sop.find('h1', {'id': 'pdp_product_title'})
        product_title = product_title_element.text if product_title_element else None

        product_price_element = sop.find('div', {'class': 'product-price'})
        product_price = product_price_element.text if product_price_element else None

        product_sub_title_element = sop.find('h2', {'class': 'headline-5', 'data-test': 'product-sub-title'})
        product_sub_title = product_sub_title_element.text if product_sub_title_element else None

        color_description_element = sop.find('li', {'class': 'description-preview__color-description'})
        color_description = color_description_element.text if color_description_element else None

        reviews_count_match = re.search(r'Reviews \((\d+)\)', str(sop))
        reviews_count = reviews_count_match.group(1) if reviews_count_match else None

        print(f"""[{len(product_total)}] Product Name: {product_title}
{LI_GREEN}Product Price: {LI_YELLOW}{product_price}
{LI_WHITE}Product Type: {product_sub_title}
Color Description: {color_description}
Reviews Count: {reviews_count}
Product URL: {url}
{mahdilinx()}""")

        # Append Product Title to the product_total list
        product_total.append([
            product_title,
            product_price,
            product_sub_title,
            color_description,
            reviews_count,
            url
        ])

    except Exception as e:
        print(f"Error processing link {url}: {e}")

    return product_total

def womens():
    all_url = []
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

    #url = 'https://www.nike.com/w/womens-shoes-5e1x6zy7ok'
    response = requests.get(url).text
    sop = bs(response, 'html.parser')
    # Find all links in the page
    for link in sop.find_all('a', href=True):
        all_link = link['href']
        all_url.append(all_link)
    # Process each unique link
    headers = ['Product Name', 'Product Price', 'Product Type', 'Color Description', 'Reviews Count', 'Product URL']
    

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(headers)
        with ThreadPoolExecutor(max_workers=50) as executor:
            # Use executor.map to apply find_product to all URLs concurrently
            results = executor.map(find_product, [p_link for p_link in set(all_url) if 'https://www.nike.com/t/' in p_link])

            # Flatten the list of lists and write to the CSV file
            csv_writer.writerows([item for sublist in results for item in sublist])
clear()
if __name__ == "__main__":
    womens()
