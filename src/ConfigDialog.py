import os
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QCompleter
from UI.ConfigUI import Ui_Dialog
from util.EasyConfig import EasyConfig
from util.Ticker import Ticker


class ConfigDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        icon_path = os.path.join(os.path.dirname(__file__), "../data/favicon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.secret_key_list = []
        self.watch_coin_list = []
        self.easyConfig = EasyConfig()
        self.easyConfig.read(self.key_list, self.secret_key_list, self.watch_list, self.watch_coin_list)
        self.getTicker = Ticker()
        self.ticker_cb.addItems(self.getTicker.tickers_kor)

        # 코인이름 autocomplete 설정
        model = QStringListModel()
        model.setStringList(self.getTicker.tickers_kor)
        completer = QCompleter()
        completer.setModel(model)
        self.ticker_cb.setCompleter(completer)

        # ListWidget의 시그널
        # 키 설정 탭 시그널
        self.key_list.currentItemChanged.connect(self.chkKeyClicked)
        self.name.textChanged.connect(self.saveKey)
        self.API_KEY.textChanged.connect(self.saveKey)
        self.SECRET_KEY.textChanged.connect(self.saveKey)

        # 감시 탭 시그널
        self.watch_list.itemClicked.connect(self.chkItemClicked)
        self.watch_list.currentItemChanged.connect(self.chkItemClicked)
        self.ticker_cb.currentIndexChanged.connect(self.saveValue)
        self.watch_price.valueChanged.connect(self.saveValue)

        # 버튼에 기능 연결
        self.btn_addKey.clicked.connect(self.addKeyListWidget)
        self.btn_addItem.clicked.connect(self.addListWidget)
        self.btn_removeItem.clicked.connect(self.removeCurrentItem)
        self.btn_removeKey.clicked.connect(self.removeCurrentKey)

    def reload_list(self):
        self.key_list.clear()
        self.secret_key_list.clear()
        self.watch_list.clear()
        self.watch_coin_list.clear()

        # Reset QlineEdit, QCombobox, QdoubleSpinbox
        self.name.setText("")
        self.API_KEY.setText("")
        self.SECRET_KEY.setText("")
        self.ticker_cb.setCurrentText("")
        self.watch_price.setValue(0)
        self.easyConfig.read(self.key_list, self.secret_key_list, self.watch_list, self.watch_coin_list)

    def saveKey(self):
        # 비정상적 이벤트 실행 방지
        if self.key_list.currentRow() == -1:
            return
        # 키 설정 탭 데이터 저장
        self.secret_key_list[self.key_list.currentRow()] = {"name": self.name.text(),
                                                            "API_KEY": self.API_KEY.text(),
                                                            "SECRET_KEY": self.SECRET_KEY.text()}
        self.key_list.item(self.key_list.currentRow()).setText(self.name.text())

    def saveValue(self):
        # 비정상적 이벤트 실행 방지
        if self.watch_list.currentRow() == -1:
            return
        # 감시 탭 데이터 저장
        self.watch_coin_list[self.watch_list.currentRow()] = {"coin": self.ticker_cb.currentText(),
                                                              "watch_price": self.watch_price.value()}

    def chkKeyClicked(self):
        self.name.blockSignals(True)
        self.API_KEY.blockSignals(True)
        self.SECRET_KEY.blockSignals(True)
        if self.key_list.currentRow() != -1:
            self.name.setText(self.secret_key_list[self.key_list.currentRow()]["name"])
            self.API_KEY.setText(self.secret_key_list[self.key_list.currentRow()]["API_KEY"])
            self.SECRET_KEY.setText(self.secret_key_list[self.key_list.currentRow()]["SECRET_KEY"])
        elif self.key_list.currentRow() == -1:
            self.name.setText('')
            self.API_KEY.setText('')
            self.SECRET_KEY.setText('')
        self.name.blockSignals(False)
        self.API_KEY.blockSignals(False)
        self.SECRET_KEY.blockSignals(False)

    def chkItemClicked(self):
        self.ticker_cb.setCurrentText(self.watch_coin_list[self.watch_list.currentRow()]["coin"])
        self.watch_price.setValue(self.watch_coin_list[self.watch_list.currentRow()]["watch_price"])

    def addKeyListWidget(self):
        addKeyName = self.name.text()
        self.key_list.addItem(addKeyName)
        self.secret_key_list.append({"name": self.name.text(),
                                     "API_KEY": self.API_KEY.text(),
                                     "SECRET_KEY": self.SECRET_KEY.text()})

    def addListWidget(self):
        self.ticker_cb.blockSignals(True)
        self.watch_price.blockSignals(True)
        addItemText = f"코인{len(self.watch_coin_list) + 1}"
        self.watch_list.addItem(addItemText)
        self.watch_coin_list.append({"coin": self.ticker_cb.currentText(),
                                     "watch_price": float(self.watch_price.text())})
        self.ticker_cb.setCurrentText("")
        self.watch_price.setValue(0)
        self.ticker_cb.blockSignals(False)
        self.watch_price.blockSignals(False)

    def removeCurrentKey(self):
        self.removeItemRow = self.key_list.currentRow()
        del self.secret_key_list[self.key_list.currentRow()]
        self.key_list.takeItem(self.removeItemRow)

    def removeCurrentItem(self):
        self.removeItemRow = self.watch_list.currentRow()
        del self.watch_coin_list[self.watch_list.currentRow()]
        self.watch_list.takeItem(self.removeItemRow)

    def check_config(self):
        self.easyConfig.reset()
        for i in range(len(self.secret_key_list)):
            self.easyConfig.config[f"API{i + 1}"] = {}
            self.easyConfig.config[f"API{i + 1}"]["name"] = str(self.secret_key_list[i]['name'])
            self.easyConfig.config[f"API{i + 1}"]["API_KEY"] = str(self.secret_key_list[i]['API_KEY'])
            self.easyConfig.config[f"API{i + 1}"]["SECRET_KEY"] = str(self.secret_key_list[i]['SECRET_KEY'])

        for i in range(len(self.watch_coin_list)):
            self.easyConfig.config[f"WATCH_COIN{i + 1}"] = {}
            self.easyConfig.config[f"WATCH_COIN{i + 1}"][self.watch_coin_list[i]['coin']] = str(self.watch_coin_list[i]['watch_price'])

        self.easyConfig.write()
