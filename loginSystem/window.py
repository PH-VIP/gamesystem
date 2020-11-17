from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from filetransport import file_update, file_download
import os


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.setupUi(self)

        self.toolButton.clicked.connect(self.ontoolbuttonclick)
        self.pushButton.clicked.connect(self.onpushbuttonclick)
        self.actionchange_account.triggered.connect(self.onpushbuttonchange_account)
        self.actionexit.triggered.connect(self.close)

    def ontoolbuttonclick(self):
        text_path = r'D:\软工项目\game\游戏说明.txt'
        with open(text_path, 'r', encoding='utf-8') as file:
            output = file.read()
        file.close()
        file_update()
        self.textBrowser.setText(output)

    def onpushbuttonclick(self):
        file_download()
        self.hide()
        os.system('python D:/pythongame/游戏.py')



    def onpushbuttonchange_account(self):
        self.hide()
        os.system('python D:/pythongame/main.py')