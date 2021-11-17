from bs4 import BeautifulSoup
import requests
import re


class Farfetch:
    def __init__(self, url, ws):
        self.prefix = "https://www.farfetch.cn/"
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

    def _listProducts(self):
        res = requests.get(url=self.url, headers=self.header)
        soup = BeautifulSoup(res.content, "html.parser")
        products = soup.find_all(name="a", attrs={"data-component": "ProductCardLink"})
        return products

    def parseFarfetch(self):
        products = self._listProducts()

        for product in products:
            print(product)
            pro = str(product)
            index1 = pro.find("href")
            index2 = pro.find(" target=")
            index3 = pro.find("</div><meta content=\"")
            index4 = pro.find(" itemprop=")
            proUrl = pro[index1+6:index2]
            picUrl = pro[index3+20:index4]
            self.productList.append(proUrl)
            self.preloadPicList.append(picUrl)
        #print(self.productList)
        #print(self.preloadPicList)
        return

    def saveImg(self):

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