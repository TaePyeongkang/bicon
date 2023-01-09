import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

form_class = uic.loadUiType('beacon.ui')[0]


class Login(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.MoveLoginPage)
        self.home1.clicked.connect(self.MainPage)




    def MoveLoginPage(self):        # 로그인 페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(0)

    def MainPage(self):
        self.stackedWidget.setCurrentIndex(1)









if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Login()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    app.exec_()