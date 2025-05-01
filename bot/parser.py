import requests
from bs4 import BeautifulSoup

def get_site_data(url):
    response = requests.get(url)
    response.raise_for_status()
        
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find_all('div', class_='section_item item bordered box-shadow')

def fetch_heads_from_site(data):
    objects = []

    for item in data:
        objects.append([item.find('span', class_='font_md').text, [href.get('href') for href in item.find_all('a', class_='muted777')]])
        
    return objects

def prices_from_new_url(url):
    response = requests.get(url)
    response.raise_for_status()
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    prices = []
    ob = soup.find_all('div', class_='inner_wrap TYPE_1')
    is_empty = soup.find_all('div', class_='no_products')
    if len(is_empty) > 0:
        prices.append('-1')
    else:        
        for it in ob:
            pr = it.find('span', class_='price_value')
            a = it.find('a', class_='dark_link js-notice-block__title option-font-bold font_sm')
            name = a.find('span')
            ti = pr.text
            fti = ti.replace("\xa0", "")
            prices.append([name.text, fti])
    return prices

def exe_fun_heads(url):
    data = get_site_data(url)
    heads = fetch_heads_from_site(data)
    return heads

def exe_fun_prices(cuted_url1, cuted_url2):
    new_url = cuted_url1 + cuted_url2
    return prices_from_new_url(new_url)

if __name__ == "__main__":
    url = 'https://s-b-1.ru/catalog/'
    cuted_url = 'https://s-b-1.ru'
    data = get_site_data(url)
    heads = fetch_heads_from_site(data)
    new_url = cuted_url + heads[0][1][4]
    pr_list = prices_from_new_url(new_url)
    print(pr_list)