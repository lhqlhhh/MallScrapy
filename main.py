# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup

import farfetch
from openpyxl import Workbook


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # create an excel
    wb = Workbook()
    dest_filename = "farfetch.xlsx"
    ws = wb.active

    # alexander-mcqueen

    # women
    am_women = wb.create_sheet(title="Alexander McQueen_women")

    url = "https://www.farfetch.cn/cn/shopping/women/alexander-mcqueen/items.aspx"
    w = farfetch.Farfetch(url, am_women)
    w.parseFarfetch()
    #w.getInfo()
    # men
    am_men = wb.create_sheet(title="Alexander McQueen_men")
    url = ""

    #htm = requests.get("https://www.farfetch.cn/cn/shopping/women/alexander-mcqueen/items.aspx")
    #htm = requests.get("https://www.baidu.com")
    #print(htm.content)

    #soup = BeautifulSoup(htm.content, "html.parser")
    #print(soup.contents)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
