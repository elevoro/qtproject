from PySide2 import QtWidgets, QtCore, QtGui

import PingMonitor
import PingMonitor_settings
import Tracert_design
from ping3 import ping
import subprocess
import time


class MainTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # начальный список адресов для мониторинга
        self.ipAddresses = [
            IpAddress("192.168.1.1", True),
            IpAddress("google.com", True),
            IpAddress("yandex.ru", False)]

        self.ui = PingMonitor.Ui_Form()
        self.ui.setupUi(self)
        self.tracert = Tracert_design_()
        self.settings = Settings(self.ipAddresses)
        self.settings.ipAddressesUpdatedSignal.connect(self.onIpAddressesUpdated, QtCore.Qt.AutoConnection)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)
        self.ui.pushButton_4.clicked.connect(self.open_many_windows)
        self.ui.pushButton_3.clicked.connect(self.open_many_windows)

        # отображаем начальный список адресов
        self.refresh_list_ui()

        # настраиваем таймер и проверку доступности адресов в отдельных потоках
        self.ipChecker = MyIpChecker(self.ipAddresses)
        self.ipChecker.ipStatusChangedSignal.connect(self.onIpStatusChanged, QtCore.Qt.AutoConnection)
        self.ipChecker.stoppedSignal.connect(self.onStopped, QtCore.Qt.AutoConnection)

    def onIpAddressesUpdated(self):
        self.refresh_list_ui()


    def onIpStatusChanged(self, message):
        self.refresh_list_ui()
        self.ui.plainTextEdit.appendPlainText(message)
        file_log = open('log.txt', 'a')
        file_log.write(message)
        file_log.close()

    def onStopped(self):
        # делаем кнопки управления неактивными
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_4.setDisabled(False)

        self.ui.plainTextEdit.appendPlainText("Остановка потока произведена")

    def start(self):
        # делаем кнопки управления неактивными
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)

        self.ipChecker.start()
        self.ui.plainTextEdit.appendPlainText("Запуск потока произведен")

    def stop(self):
        self.ipChecker.stop()
        self.ui.plainTextEdit.appendPlainText("Остановка потока запрошена")

    def open_many_windows(self):
        if self.sender().objectName() == "pushButton_3":
            # открываем окно с трассировкой только если выбра адрес
            if len(self.ui.tableWidget.selectedIndexes()) > 0:
                self.tracert.set_ip_address(
                    self.ipAddresses[self.ui.tableWidget.selectedIndexes()[0].row()])
                self.tracert.show()
        else:
            self.settings.show()

    def refresh_list_ui(self):
        self.ui.tableWidget.clear()

        i = 0
        for ip in self.ipAddresses:
            statusStr = "not active"
            if ip.status:
                statusStr = "active"

            # добавляем строчку
            self.ui.tableWidget.insertRow(i)

            # настраиваем ячейку для отображения адреса
            self.ui.tableWidget.setItem(
                i,
                0,
                QtWidgets.QTableWidgetItem(ip.ip))

            # настраиваем ячейку для отображения статуса
            self.ui.tableWidget.setItem(
                i,
                1,
                QtWidgets.QTableWidgetItem(statusStr))

            i += 1


class IpAddress:
    def __init__(self, ip, status):
        self.ip = ip
        self.status = status

class Tracert_design_(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Tracert_design.Ui_Form()
        self.ui.setupUi(self)

        self.tracert = MyTracert()
        self.tracert.receivedLineSignal.connect(self.onReceivedLineSignal, QtCore.Qt.AutoConnection)
        self.tracert.stoppedSignal.connect(self.onStopped, QtCore.Qt.AutoConnection)

    def show(self):
        super().show()
        self.ui.plainTextEdit.clear()

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        # останавливаем трассировку если окно закрывается
        self.tracert.stop()

    def onReceivedLineSignal(self, message):
        self.ui.plainTextEdit.appendPlainText(message)

    def onStopped(self):
        self.ui.plainTextEdit.appendPlainText("\n\nГотово!")

    def set_ip_address(self, ipAddress):
        self.tracert.set_ip(ipAddress.ip)
        self.tracert.start()


class MyTracert(QtCore.QThread):
    receivedLineSignal = QtCore.Signal(str)
    stoppedSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.shouldStop = False
        self.ip = None

    def set_ip(self, ip):
        self.ip = ip

    def stop(self):
        self.shouldStop = True

    def run(self):
        self.shouldStop = False

        # https://pythobyte.com/python-running-ping-traceroute-and-more-e7e3da6a/

        proc = subprocess.Popen(f"tracert -d {self.ip}",
                                stdout=subprocess.PIPE)

        i = 1

        while not self.shouldStop:
            line = proc.stdout.readline().decode("cp850")

            # показываем только сообщения вида:
            # 2     2 ms     1 ms     1 ms  10.220.11.254
            # с кодировкой кириллицы проблему решить не удалось
            if line.strip().startswith(f"{i}"):
                self.receivedLineSignal.emit(line.strip())
                i += 1

            if not line:
                break

        self.stoppedSignal.emit()

class Settings(QtWidgets.QWidget):
    ipAddressesUpdatedSignal = QtCore.Signal()

    def __init__(self, ipAddresses, parent=None):
        super().__init__(parent)

        self.ipAddresses = ipAddresses

        self.waitingForOperand = True
        self.ui = PingMonitor_settings.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.new_ip)
        self.ui.pushButton_2.clicked.connect(self.delete)

    def show(self):
        super().show()
        self.refresh_list_ui()

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        # стираем адрес при закрытии окна
        self.ui.ipTextInput.setText("")

    def refresh_list_ui(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(label.ip for label in self.ipAddresses)

    def new_ip(self):
        # добавляем новый адрес
        newIpAddress = IpAddress(self.ui.ipTextInput.text(), False)
        self.ui.ipTextInput.setText("")
        self.ipAddresses.append(newIpAddress)

        # обновляем UI
        self.refresh_list_ui()

        # уведомляем слушателя что список изменен
        self.ipAddressesUpdatedSignal.emit()

    def delete(self):
        # удаляем выбранный адрес
        if len(self.ui.listWidget.selectedIndexes()) > 0:
            # удаляем из списка
            self.ipAddresses.pop(
                self.ui.listWidget.selectedIndexes()[0].row())

            # обновляем UI
            self.refresh_list_ui()

            # уведомляем слушателя что список изменен
            self.ipAddressesUpdatedSignal.emit()

class MyIpChecker(QtCore.QThread):
    ipStatusChangedSignal = QtCore.Signal(str)
    stoppedSignal = QtCore.Signal()

    def __init__(self, ipAddresses):
        super().__init__()

        self.shouldStop = False
        self.ipAddresses = ipAddresses

    def stop(self):
        self.shouldStop = True

    def run(self):
        self.shouldStop = False

        while not self.shouldStop:
            # пробегаемся по всем адресам и пингуем их
            for ip in self.ipAddresses:
                if self.shouldStop:
                    break

                r = ping(ip.ip)

                # запоминаем статус адреса перед проверкой
                oldStatus = ip.status

                if r is not None and r is not False:
                    ip.status = True
                else:
                    ip.status = False

                # сообщаем основному потоку только если статус поменялся
                if oldStatus != ip.status:
                    statusStr = "not active"
                    if ip.status:
                        statusStr = "active"

                    message = f'Адрес {ip.ip} изменил свой статус на "{ip.status}" в {time.ctime()}'

                    self.ipStatusChangedSignal.emit(message)

            time.sleep(1)

        self.stoppedSignal.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()
