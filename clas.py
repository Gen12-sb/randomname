from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui(object):
    def setupUi(self, Ui):
        Ui.setObjectName("Ui")
        Ui.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 220, 230, 60))
        self.pushButton.setObjectName("pushButton")
        Ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui)
        self.statusbar.setObjectName("statusbar")
        Ui.setStatusBar(self.statusbar)

        self.retranslateUi(Ui)
        QtCore.QMetaObject.connectSlotsByName(Ui)

    def retranslateUi(self, Ui):
        _translate = QtCore.QCoreApplication.translate
        Ui.setWindowTitle(_translate("Ui", "Git и желтые окружности"))
        self.pushButton.setText(_translate("Ui", "Создать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui = QtWidgets.QMainWindow()
    ui = Ui_Ui()
    ui.setupUi(Ui)
    Ui.show()
    sys.exit(app.exec_())
