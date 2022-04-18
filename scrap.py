import sys

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

class Danawa:
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/100.0.4896.60 Safari/537.36'
        ),
    }

    def __init__(self, pcode, cate=None):
        self.url = f'http://prod.danawa.com/info/?pcode={pcode}'
        if cate is not None:
            self.url += '&cate={cate}'

    def scrap(self):
        resp = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(resp.text, 'lxml')

        self.product_name = soup.find('h3', class_='prod_tit').text

        raw_prices = soup.find('tbody', class_='high_list').find_all('tr')
        self.prices = []
        for each in raw_prices:
            shop_link = each.find('div', class_='logo_over').find('a')
            shop_logo = shop_link.find('img')
            if shop_logo is None:
                shop = shop_link['title']
            else:
                try:
                    shop = shop_logo['alt']
                except KeyError:
                    continue

            delevery = each.find('td', class_='ship').find(class_='stxt').text.replace(',', '').replace('원', '')
            if delevery == '무료배송':
                delevery = 0
            delevery = int(delevery)

            self.prices.append({
                'shop': shop,
                'price': int(each.find('em', class_='prc_t').text.replace(',', '')),
                'delevery': delevery,
            })

    def pprint(self):
        print(f'{Fore.MAGENTA}{self.product_name}{Style.RESET_ALL}')
        for price in self.prices:
            delevery = price['delevery']
            if delevery == 0:
                delevery = '무료배송'
            else:
                delevery = format(delevery, ',') + '원'
            print(f'  {Fore.YELLOW}{price["shop"]}{Style.RESET_ALL} {Fore.CYAN}{price["price"]:,}원{Style.RESET_ALL} {Fore.BLUE}({delevery}){Style.RESET_ALL}')
        sys.stdout.flush()

if __name__ == '__main__':
    asus_tuf_3070ti = Danawa(14444705)
    asus_tuf_3070ti.scrap()
    asus_tuf_3070ti.pprint()

    asus_rog_3070ti = Danawa(14444267)
    asus_rog_3070ti.scrap()
    asus_rog_3070ti.pprint()
