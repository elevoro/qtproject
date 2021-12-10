from PySide2 import QtWidgets
import MainForm


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = MainForm.Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        self.ui.lineEdit_2.setText("Иван")

        self.ui.toolBox.setCurrentIndex(0)

        self.ui.pushButton.clicked.connect(self.line_edit_disabled)
        self.ui.pushButton_2.clicked.connect(self.line_edit_enable)



    def line_edit_disabled(self):
        self.ui.lineEdit_3.setEnabled(False)


    def line_edit_enable(self):
        self.ui.lineEdit_3.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()