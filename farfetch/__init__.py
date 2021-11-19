import random
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from bs4 import BeautifulSoup
import requests
from util import Tactic
import os
import time


def _save_image(url):
    tac = Tactic()
    res = requests.get(url, headers=tac.rand_user_agent())
    file_name = url.split('/')[-1]
    if os.path.exists(file_name):
        return file_name
    else:
        with open(file_name, 'wb') as f:
            for data in res.iter_content(128):
                f.write(data)
    return file_name


class Farfetch:

    def __init__(self, url, brand):
        self.brand = brand
        self.prefix = "https://www.farfetch.cn/"
        self.parser = "lxml"
        self.url = url
        self.count = 1
        self.first_page = ""
        self.prod_pic_list = [[]]
        # create workbook
        wb = Workbook()
        ws = wb.active
        self.wb = wb
        self.ws = ws
        self.excel_name = "farfetch_" + self.brand + ".xlsx"

    def _list_products(self):
        while True:
            soup = self._make_soup(self.url + "?page=" + str(self.count))
            if self.count == 1:
                self.first_page = str(soup)

            products = soup.find_all(name="a", attrs={"data-component": "ProductCardLink"})
            for product in products:
                product_name = product.find(name="p",
                                            attrs={"data-component": "ProductCardDescription", "itemprop": "name"}).text
                product_url = self.prefix + (str(product["href"]))
                self.prod_pic_list.append([product_name, product_url])
            self.count += 1

            if self.first_page == str(soup) and self.count != 1:
                break

        # remove first empty element
        self.prod_pic_list.pop(0)

    def _single_product(self, name, url):
        # 随机0-1秒访问，防反扒
        time.sleep(random.random())
        soup = self._make_soup(url)
        content = soup.find(name="div", attrs={"data-tstid": "productDetails"})
        gallery = soup.find(name="div", attrs={"data-tstid": "gallery-and-productoffer"})

        print("content: ", content)
        print("product name: ", name)

        para = content.find_all(name="p")
        details = ""
        for p in para:
            details = details + p.text + "\n"

        data = [name, details]
        # save to files
        self.ws.append(data)

        pics = gallery.find_all(name="link", attrs={"itemprop": "image"})
        count = 3
        for pic in pics:
            # download pic
            img_path = _save_image(str(pic["href"]))
            img = Image(img_path)
            coor = self.ws.cell(self.count-1, count).coordinate
            self.ws.column_dimensions[coor[0]].width = img.width
            self.ws.row_dimensions[int(coor[1])].height = img.height
            count += 1
            self.ws.add_image(img, coor)

    def _browse_all_product(self):
        self._list_products()

        for elem in self.prod_pic_list:
            self._single_product(elem[0], elem[1])
        # 保存到excel中
        self.wb.save(self.excel_name)

    def _make_soup(self, url):
        tac = Tactic()
        res = requests.get(url=url, headers=tac.rand_user_agent())
        soup = BeautifulSoup(res.content, self.parser)
        return soup

    def shopping(self):
        self._browse_all_product()
        return
