from PySide2 import QtWidgets
import MainForm2
from PySide2 import QtCore, QtWidgets, QtGui

class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = MainForm2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.moveButton)
        self.ui.toolButton_2.clicked.connect(self.moveButton)
        self.ui.toolButton_3.clicked.connect(self.moveButton)
        self.ui.toolButton_4.clicked.connect(self.moveButton)
        self.ui.toolButton_5.clicked.connect(self.moveButton)
        self.ui.toolButton_6.clicked.connect(self.dataButton)
        self.ui.dial.valueChanged


    def moveButton(self):

        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()

        params = {'Лево/Верх': (0, 0),
        'Право/верх': (screenWidth - self.width(), 0),
        'Центр': ((screenWidth - self.width()) // 2, (screenHeight - self.height()) // 2),
        'Лево/Низ': (0, screenHeight - self.height() - 75),
        'Право/Низ': (screenWidth - self.width(), screenHeight - self.height() - 75),
        }

        x, y = params.get(self.sender().text())

        self.move(x, y)

    def dataButton(self):
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        print(screen_resolution, width, height)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()


    app.exec_()