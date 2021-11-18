from bs4 import BeautifulSoup
import requests
import threading
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import process


def _save_image(url):
    res = requests.get(url)
    file_name = url.split('/')[-1]
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
        self.header = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/67.0.3396.79 Safari/537.36'
        }
        self.productList = []
        self.preloadPicList = []
        self._lock = threading.Lock()
        self.data = [[]]
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

        para = content.find_all(name="p")
        details = ""
        for p in para:
            details = details + p.text + "\n"

        data = [name, details]

        pics = gallery.find_all(name="link", attrs={"itemprop": "image"})
        for pic in pics:
            # download pic
            img = _save_image(pic)
            data.append(img)

        # save to files
        self._lock.acquire()
        self.ws.append(data)
        self._lock.release()

    def parse_all_product(self):
        self._list_products()
        pool = ThreadPool()
        for elem in self.prod_pic_dict:
            _ = pool.map(self._single_product, elem[0], elem[1])
            pool.close()
            pool.join()

        #for elem in self.prod_pic_list:
        #    self._single_product(elem[0], elem[1])

    def make_soup(self, url):
        res = requests.get(url=url, headers=self.header)
        soup = BeautifulSoup(res.content, self.parser)
        return soup

    def shopping(self):

        return
