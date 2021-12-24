from PySide2 import QtWidgets, QtCore, QtGui
import PingMonitor, PingMonitor_settings, Tracert_design
from ping3 import ping


class MainTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = PingMonitor.Ui_Form()
        self.ui.setupUi(self)
        self.tracert = Tracert_design_()
        self.settings = Settings()
        self.ui.pushButton.clicked.connect(self.ping_)
        self.ui.pushButton_4.clicked.connect(self.open_many_windows)
        self.ui.pushButton_3.clicked.connect(self.open_many_windows)

    def open_many_windows(self):
        if self.sender().objectName() == "pushButton_3":
            self.tracert.show()
            #print(self.ui.tableWidget.selectedItems())#получить данные от выбранной строки таблицы
        else:
            self.settings.show()


    def ping_(self):

        r = ping('google.com')
        self.ui.tableWidget.insertRow(0)
        if r is not None and r is not False:
            self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("active"))
        else:
            self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("passive"))
        print(r)


class Tracert_design_(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Tracert_design.Ui_Form()
        self.ui.setupUi(self)


class Settings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = PingMonitor_settings.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.new_IP)


    def new_IP(self):
        self.ui.listWidget.addItem(QtWidgets.QListWidgetItem())

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()