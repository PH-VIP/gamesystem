import resource.loadsystem
import resource.register
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QLineEdit
import sys
import pymysql


#  注册按钮窗口连接
class MyRegisterForm(QMainWindow, resource.register.Ui_Form):
    def __init__(self, parent=None):
        super(MyRegisterForm, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.pushButton.clicked.connect(self.register)

    #  注册实现
    def register(self):
        name = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        again_pwd = self.lineEdit_3.text()

        if name != '' and pwd != '':
            pass
        else:
            QMessageBox.critical(self, "出现错误", "用户名或者密码不能为空", QMessageBox.Retry)

        #   密码不一致时弹出错误对话框
        if pwd != again_pwd:
            QMessageBox.critical(self, "出现错误", "密码输入不一致", QMessageBox.Retry)
            return

        db = pymysql.connect('localhost', 'root', '123456', 'user')

        cur = db.cursor()

        sql = '''
            insert into account(user_name, user_password)
            values ('%s', '%s')
        ''' % (name, pwd)

        try:
            cur.execute(sql)
            db.commit()

            QMessageBox.information(self, '信息提示对话框', '注册成功', QMessageBox.Ok)
        except:
            QMessageBox.critical(self, "出现错误", "已存在该用户名", QMessageBox.Retry)

        cur.close()
        db.close()


class MyLoginWindow(QMainWindow, resource.loadsystem.Ui_MainWindow):

    def __init__(self, register, parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.register = MyRegisterForm()
        self.pwd_label.setEchoMode(QLineEdit.Password)
        self.register2_label.clicked.connect(self.openRegister)
        self.login_button.clicked.connect(self.login_database)

    def openRegister(self):
        self.register.show()

    def login_database(self):
        name = self.account_label.text()
        pwd = self.pwd_label.text()

        if name != '' and pwd != '':
            pass
        else:
            QMessageBox.critical(self, "出现错误", "用户名或者密码不能为空", QMessageBox.Retry)
            return

        db = pymysql.connect('localhost', 'root', '123456', 'user')

        cur = db.cursor()

        sql = '''
            select * 
            from account
            where user_name = '%s' and user_password = '%s'
        ''' % (name, pwd)

        cnt = cur.execute(sql)

        cur.close()
        db.close()

        if cnt > 0:
            # 进入界面
            self.hide()
            self.register.hide()
            pass
        else:
            QMessageBox.critical(self, "出现错误", "用户名或者密码不正确", QMessageBox.Retry)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myreg = MyRegisterForm()
    myWin = MyLoginWindow(myreg)
    myWin.show()
    sys.exit(app.exec_())
