from bs4 import BeautifulSoup
import requests
from util import random_agents as ra
import os


def _save_image(url):
    res = requests.get(url, headers=ra.random_agent())
    file_name = url.split('/')[-1]
    if os.path.exists(file_name):
        return file_name
    else:
        with open(file_name, 'wb') as f:
            for data in res.iter_content(128):
                f.write(data)
    return file_name


class Farfetch:
    def __init__(self, url, ws):
        self.prefix = "https://www.farfetch.cn/"
        self.parser = "lxml"
        self.url = url
        self.ws = ws
        self.prod_pic_list = [[]]

    def _list_products(self):
        soup = self.make_soup(self.url)
        products = soup.find_all(name="a", attrs={"data-component": "ProductCardLink"})
        for product in products:
            product_name = product.find(name="p", attrs={"data-component": "ProductCardDescription", "itemprop": "name"}).text
            product_url = self.prefix + (str(product["href"]))
            self.prod_pic_list.append([product_name, product_url])
        # remove first empty element
        self.prod_pic_list.pop(0)

    def _single_product(self, name, url):
        soup = self.make_soup(url)
        content = soup.find(name="div", attrs={"data-tstid": "productDetails"})
        gallery = soup.find(name="div", attrs={"data-tstid": "gallery-and-productoffer"})

        print(name)

        para = content.find_all(name="p")
        details = ""
        for p in para:
            details = details + p.text + "\n"

        data = [name, details]

        pics = gallery.find_all(name="link", attrs={"itemprop": "image"})
        for pic in pics:
            # download pic
            img = _save_image(str(pic["href"]))
            data.append(img)

        # save to files
        self.ws.append(data)

    def parse_all_product(self):
        self._list_products()

        for elem in self.prod_pic_list:
            self._single_product(elem[0], elem[1])

    def make_soup(self, url):
        res = requests.get(url=url, headers=ra.random_agent())
        soup = BeautifulSoup(res.content, self.parser)
        return soup

    def shopping(self):

        return
