import farfetch
from openpyxl import Workbook


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # alexander-mcqueen

    # women

    url = "https://www.farfetch.cn/cn/shopping/women/alexander-mcqueen/items.aspx"
    amw = farfetch.Farfetch(url, "Alexander_McQueen_women")
    amw.shopping()

    # men
    url = ""


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
