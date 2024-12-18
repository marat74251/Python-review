import requests
from bs4 import BeautifulSoup

#item_info = soup.find_all('div', class_='item_info')
#item_data = []
#for product in item_info:
#    name = product.find('span')
#    optprice = product.find("span", class_="price_value")
#    roz = product.find("div", class_="price_group RETAIL_PRICE")
#    rozprice = roz.find("span", class_="price_value")
#    optprice_true = str(optprice.text)
#    optprice_true = optprice_true.replace('\\xa0', '', -1)
#    rozprice_true = str(rozprice.text)
#    rozprice_true = rozprice_true.replace('\\xa0', '', -1)
#    item_data.append([name.text, optprice_true, rozprice_true])
#print(item_data)

def fetch_data_from_site(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        titles = [h1.text.strip() for h1 in soup.find_all('h1')]
        
        return titles

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return []

if __name__ == "__main__":
    url = "https://galeontrade.ru/"
    data = fetch_data_from_site(url)
    print(f"Данные с {url}: {data}")