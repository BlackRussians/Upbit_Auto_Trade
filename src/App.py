import os
import multiprocessing
import pyupbit

from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import *
from PySide6.QtCore import QTime, Qt, QCoreApplication, QTimer, QEventLoop, Slot
from UI.MainWindowUI import Ui_MainWindow
from OverviewWorker import OverviewWorker
from util.StdoutRedirect import StdoutRedirect
from ConfigDialog import ConfigDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        icon_path = os.path.join(os.path.dirname(__file__), "../data/favicon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        # 최소화 버튼만 활성화
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.configDialog = ConfigDialog()
        self.secret_key_list = ConfigDialog().secret_key_list
        self.update_login_data()

        # 파이썬 console내용 textEdit 박스에서 출력하도록 시그널 연결
        # self._stdout = StdoutRedirect()
        # self._stdout.start()
        # self._stdout.printOccur.connect(lambda x: self._append_text(x))

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.current_time)
        self.timer.start()

        self.config_sub_menu.triggered.connect(self.config_open)
        self.exit_sub_menu.triggered.connect(self.exit_event)
        self.login_btn.clicked.connect(self.login)
        self.start_trading_btn.clicked.connect(self.start_trading)

        self.status_label = QLabel(QTime.currentTime().toString("hh.mm.ss"))
        self.status_label.setStyleSheet("margin-right: 5px")
        self.status_label.setAlignment(Qt.AlignRight)
        self.statusBar().addWidget(self.status_label, True)

        self.ovw = OverviewWorker(self.OverviewWidget.getTicker.markets)
        self.ovw.dataSent.connect(self.OverviewWidget.set_data)
        self.ovw.start()

    def _append_text(self, msg):
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(msg)
        # refresh textedit show, refer) https://doc.qt.io/qt-5/qeventloop.html#ProcessEventsFlag-enum
        QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)

    def config_open(self):
        if self.configDialog.exec():
            self.configDialog.check_config()
            self.update_login_data()
            # self.textEdit.append("확인")
        else:
            self.configDialog.reload_list()
            # self.textEdit.append("Cancel")
            pass

    def exit_event(self):
        reply = QMessageBox.question(self, '종료', '종료 하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.ovw.close()
            QCoreApplication.quit()
            print(os.path.abspath(__file__))

    def current_time(self):
        self.status_label.setText(QTime.currentTime().toString("hh:mm:ss"))

    def update_login_data(self):
        self.keyId_cb.clear()
        self.secret_key_list = ConfigDialog().secret_key_list
        for key in self.configDialog.secret_key_list:
            self.keyId_cb.addItem(key["name"])

    def login(self):
        if self.login_btn.text() == "로그인" and self.keyId_cb.currentText() != "":
            API_KEY = self.secret_key_list[self.keyId_cb.currentIndex()]['API_KEY']
            SECRET_KEY = self.secret_key_list[self.keyId_cb.currentIndex()]['SECRET_KEY']
            if len(API_KEY) != 40 or len(SECRET_KEY) != 40:
                self.textEdit.append("KEY가 올바르지 않습니다.")
                return
            else:
                # 로그인 버튼 텍스트
                self.login_btn.setText("로그아웃")
                login_info = pyupbit.Upbit(API_KEY, SECRET_KEY)
                try:
                    balances = login_info.get_balances()
                    # 로그인 성공 메세지 출력
                    self.textEdit.clear()
                    self.textEdit.append("업비트 로그인에 성공하였습니다.")
                    self.InvestListWidget.update_list(balances, self.OverviewWidget)
                    self.ovw.dataSent.connect(self.InvestListWidget.set_data)
                except TypeError:
                    return
        elif self.login_btn.text() == "로그아웃" and self.keyId_cb.currentText() != "":
            # 로그인 버튼 텍스트
            self.login_btn.setText("로그인")
            self.textEdit.clear()
            self.InvestListWidget.reset()
            self.ovw.dataSent.disconnect(self.InvestListWidget.set_data)
            self.textEdit.append("정상적으로 로그아웃 되었습니다.")
        elif self.keyId_cb.currentText() == "":
            warning_text = "등록된 API KEY, SECRET KEY가 없습니다.\n환경설정에서 등록해 주세요."
            QMessageBox.warning(self, '오류', warning_text, QMessageBox.Ok | QMessageBox.NoButton)

    def start_trading(self):
        if self.start_trading_btn.text() == "매매 시작":
            text = "매매 중지"
            self.ovw.dataSent.connect(self.set_data)
            print(self.configDialog.watch_coin_list)
        else:
            text = "매매 시작"
            self.ovw.dataSent.disconnect(self.set_data)
        self.start_trading_btn.setText(text)

    @Slot(str, float)
    def set_data(self, *datas):
        print(datas)
        # print(self.OverviewWidget.getTicker.tickers)
        # print(self.configDialog.watch_coin_list)
        # for a in self.configDialog.watch_coin_list:
        #     if current_ticker == a["code"] and trade_price <= a["price"]:
        #         print(f"{current_ticker} 현재가격: {trade_price}, 감시가격: {a['price']}, 감시 가격 도달")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
