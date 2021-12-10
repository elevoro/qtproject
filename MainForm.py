# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'practis1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.groupBox)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toolButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.toolButton_3 = QToolButton(self.groupBox)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.toolButton_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton_4 = QToolButton(self.groupBox)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.toolButton_4)

        self.toolButton_5 = QToolButton(self.groupBox)
        self.toolButton_5.setObjectName(u"toolButton_5")
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.toolButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.toolButton_6 = QToolButton(self.groupBox)
        self.toolButton_6.setObjectName(u"toolButton_6")
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.toolButton_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(self.groupBox)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_4.addWidget(self.plainTextEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0432\u0435\u0440\u0445", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"HEX", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIN", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HEX", None))
    # retranslateUi

