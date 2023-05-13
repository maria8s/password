from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets,QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        #top bar
        h_topbar = QtWidgets.QHBoxLayout()
        topbar = QtWidgets.QFrame()
        self.btn_add_pwd = QtWidgets.QPushButton('Добавить пароль')
        h_topbar.addStretch(6)
        h_topbar.addWidget(self.btn_add_pwd, stretch = 2)
        topbar.setLayout(h_topbar)

        #Password List
        self.list_pwd = QtWidgets.QlistWidget()

        #main

        v_main = QtWidgets.QVBoxLayout()
        v_main.addWidget(topbar)
        v_main.addWidget(self.list_pwd)

        #set Layout

        self.setLayout(v_main)

class AddPasswordWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        def initUI(self):
            v_main = QtWidgets.QVBoxLayout()
            lbl_service = QtWidgets.QLabel('Сервис')
            lbl_login = QtWidgets.QLabel('Логин')
            lbl_password = QtWidgets.QLabel('Пароль')

            self.service_edit = QtWidgets.QLineEdit()
            self.login_edit = QtWidgets.QLineEdit()
            self.password_edit = QtWidgets.QLineEdit()

            self.password_edit.setEchoMode(...)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
