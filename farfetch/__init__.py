from bs4 import BeautifulSoup
import requests
import threading
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import process


class Farfetch:
    def __init__(self, url, ws):
        self.prefix = "https://www.farfetch.cn/"
        self.parser = "lxml"
        self.url = url
        self.ws = ws
        self.header = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/67.0.3396.79 Safari/537.36'
        }
        self.productList = []
        self.preloadPicList = []
        self._lock = threading.Lock()

    def _list_products(self):
        soup = self.make_soup(self.url)
        products = soup.find_all(name="a", attrs={"data-component": "ProductCardLink"})
        for product in products:
            self.productList.append(str(product["href"]))
            self.preloadPicList.append(product.meta["content"])

    def _single_product(self, url):
        soup = self.make_soup(self.prefix+url)
        content = soup.find(name="div", attrs={"data-tstid": "productDetails"})
        description = content.find(name="p", attrs={"data-tstid": "fullDescription"}).p
        #写入excel

        made_in = content.find(name="p", attrs={"data-tstid": "madeIn"})

        designer_style_id = content.find(name="p", attrs={"data-tstid": "designerStyleId"}).span

        print(description)


    def parse_all_product(self):
        #pool = ThreadPool()
        #for url in self.productList:
        #    _ = pool.map(self._single_product, url)
        self._list_products()
        for url in self.productList:
            self._single_product(url)

    def save_images(self):

        return


    def getInfo(self):
        for u in self.productList:
            url = self.prefix + u
            res = requests.get(url=url, headers=self.header)
            soup = BeautifulSoup(res.content, "html.parser")
            rawname = soup.find(name="span", attrs={"data-tstid": "cardInfo-description"})
            index1 = str(rawname).find("n\">")
            index2 = str(rawname).find("</span>")
            name = str(rawname)[index1+3:index2]
            print(name)
        return

    def make_soup(self, url):
        res = requests.get(url=url, headers=self.header)
        soup = BeautifulSoup(res.content, self.parser)
        return soup

    def shopping(self):

        return
