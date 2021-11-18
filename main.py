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
    #w.list_products()
    w.parse_all_product()
    #w.getInfo()
    # men
    am_men = wb.create_sheet(title="Alexander McQueen_men")
    url = ""

    wb.save(dest_filename)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
