import logging
import sys

from PyQt5.QtWidgets import (QWidget, QComboBox, QMessageBox, QScrollArea, QPlainTextEdit, QPushButton, QFormLayout, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

import emitstream
import farfetch
import logsignal
import tester


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # # Install the custom output stream
        # sys.stdout = emitstream.EmitStream(textWritten=self.normalOutputWritten)

        self.setGeometry(600, 400, 900, 550)
        self.setWindowTitle("Spider")
        self.setWindowIcon(QIcon('anime_icon.jpeg'))

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

        self.textBox = QPlainTextEdit()
        self.textBox.setReadOnly(True)
        handler = logsignal.Handler()
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        handler.logSignal.connect(self.textBox.appendPlainText)

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

        # create a form layout
        self.formlayout = QFormLayout()
        self.brandLabel = QLabel("Brand")
        # brand combo box（下拉框）
        self.combox = QComboBox(self)
        for brand in brands:
            self.combox.addItem(brand[0], brand[1])
        # download button
        self.downloadBtn = QPushButton('Download', self)
        self.downloadBtn.clicked.connect(self.tester)
        # text edit to print running process

        # # 添加滚动
        # self.scrollArea = QScrollArea()
        # self.scrollArea.setWidget(self.text)
        # #self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # #self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # message box to print
        # self.messageBox = QMessageBox()

        self.formlayout.addRow(self.brandLabel, self.combox)
        self.formlayout.addRow(self.downloadBtn)
        # self.formlayout.addRow(self.scrollArea)
        # self.formlayout.addRow(self.messageBox)
        self.formlayout.addRow(self.textBox)
        self.setLayout(self.formlayout)
        self.show()

    # def __del__(self):
    #     # Restore sys.stdout
    #     sys.stdout = sys.__stdout__

    def download(self):
        logging.info('start downloading...')
        if self.combox.currentText() != "All":
            logging.info('downloading ' + self.combox.currentText())
            brandName = self.combox.currentText().lower().replace(" ", "-")
            brandWomen = brandName + "-women"
            brandMen = brandName + "-men"
            urlWomen = "https://www.farfetch.cn/cn/shopping/women/" + brandName + "/items.aspx"
            urlMen = "https://www.farfetch.cn/cn/shopping/men/" + brandName + "/items.aspx"

            womenShopping = farfetch.Farfetch(urlWomen, brandWomen)
            menShopping = farfetch.Farfetch(urlMen, brandMen)

            # start downloading
            logging.info('shopping ' + brandWomen + ' closet...')
            womenShopping.shopping()
            logging.info('finished shopping' + brandWomen + ' closet.')
            logging.info('shopping ' + brandMen + ' closet...')
            menShopping.shopping()
            logging.info('finished shopping' + brandMen + ' closet.')
        else:
            logging.info('start downloading all brands...')
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

    # def normalOutputWritten(self, text):
    #     cursor = self.textBox.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textBox.setTextCursor(cursor)
    #     self.textBox.ensureCursorVisible()

    def tester(self):
        print("test")
        logging.info("tester func")
        t = tester.Tester()
        t.run()


