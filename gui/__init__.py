from PyQt5.QtWidgets import (QWidget, QComboBox, QPushButton, QFormLayout, QLabel, QLineEdit)
from PyQt5.QtGui import QIcon
import farfetch


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.brands = ["alexander-mcQueen", "alexander-wang", "ami-alexandre-mattiussi",
                       "balenciaga", "burberry", "bottega-veneta",
                       "dior",
                       "fendi",
                       "givenchy", "gucci",
                       "loewe",
                       "maison-margiela",
                       "offWhite",
                       "palm-angels",
                       "saint-laurent",
                       "valentino",
                       "thom-browne",
                       "we11done"]
        self.Init_UI()

    def Init_UI(self):
        brands = [[QIcon("./assets/all.png"), "All"],
                  [QIcon("./assets/am.jpg"), "Alexander McQueen"],
                  [QIcon("./assets/aw.jpg"), "Alexander Wang"],
                  [QIcon("./assets/amiparis.jpg"), "Ami Paris"],
                  [QIcon("./assets/balenciaga.jpg"), "Balenciaga"],
                  [QIcon("./assets/burberry.jpg"), "Burberry"],
                  [QIcon("./assets/bv.jpg"), "Bottega Veneta"],
                  [QIcon("./assets/cdior.jpg"), "Dior"],
                  [QIcon("./assets/fendi.jpg"), "Fendi"],
                  [QIcon("./assets/givenchy.jpg"), "Givenchy"],
                  [QIcon("./assets/gucci.jpg"), "Gucci"],
                  [QIcon("./assets/loewe.jpg"), "Loewe"],
                  [QIcon("./assets/mm.jpg"), "Maison Margiela"],
                  [QIcon("./assets/offwhite.jpg"), "OffWhite"],
                  [QIcon("./assets/palmangels.jpg"), "Palm Angels"],
                  [QIcon("./assets/ysl.jpg"), "Saint Laurent"],
                  [QIcon("./assets/valentino.jpg"), "Valentino"],
                  [QIcon("./assets/tb.jpg"), "Thom Browne"],
                  [QIcon("./assets/we11done.jpg"), "We11done"]]

        self.setGeometry(600, 400, 900, 550)
        self.setWindowTitle("Spider")
        self.setWindowIcon(QIcon('anime_icon.jpeg'))
        # create a form layout
        self.formlayout = QFormLayout()
        self.brandLabel = QLabel("Brand")
        self.combox = QComboBox(self)
        for brand in brands:
            self.combox.addItem(brand[0], brand[1])

        self.downloadBtn = QPushButton('Download', self)
        self.downloadBtn.clicked.connect(self.download)
        self.formlayout.addRow(self.brandLabel, self.combox)
        self.formlayout.addRow(self.downloadBtn)
        self.setLayout(self.formlayout)

        self.show()

    def download(self):
        if self.combox.currentText() != "All":
            brandName = self.combox.currentText().lower().replace(" ", "-")
            brandWomen = brandName + "-women"
            brandMen = brandName + "-men"
            urlWomen = "https://www.farfetch.cn/cn/shopping/women/" + brandName + "/items.aspx"
            urlMen = "https://www.farfetch.cn/cn/shopping/men/" + brandName + "/items.aspx"
            womenShopping = farfetch.Farfetch(urlWomen, brandWomen)
            menShopping = farfetch.Farfetch(urlMen, brandMen)
            
            # start downloading
            womenShopping.shopping()
            menShopping.shopping()
        else:
            for brand in self.brands:
                brandWomen = brand + "-women"
                brandMen = brand + "-men"
                urlWomen = "https://www.farfetch.cn/cn/shopping/women/" + brand + "/items.aspx"
                urlMen = "https://www.farfetch.cn/cn/shopping/men/" + brand + "/items.aspx"
                womenShopping = farfetch.Farfetch(urlWomen, brandWomen)
                menShopping = farfetch.Farfetch(urlMen, brandMen)
                # ami-paris 没有女装
                if brand != "ami-alexandre-mattiussi":
                    # start downloading
                    womenShopping.shopping()
                    menShopping.shopping()
                else:
                    menShopping.shopping()
