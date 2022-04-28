import re
import sys
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QTableWidget, QHeaderView
from PySide6.QtCore import Slot
from UI.InvestListUI import Ui_Form
import numpy as np
from util.Ticker import Ticker


class InvestListWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.investListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.header = self.investListTable.horizontalHeader()
        self.coin_list = []
        self.ticker = Ticker()

    def resize_section(self):
        # 컬럼 너비 자동 조정 https://kwonkyo.tistory.com/370
        column_width = []
        for col in range(self.header.count()):
            self.header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
            column_width.append(self.header.sectionSize(col))

        for col in range(self.header.count()):
            self.header.setSectionResizeMode(col, QHeaderView.Interactive)
            self.header.resizeSection(col, column_width[col] * self.header.width() / sum(column_width))

    def reset(self):
        for row in range(self.investListTable.rowCount()):
            for col in range(self.investListTable.columnCount()):
                self.investListTable.takeItem(row, col)
        self.investListTable.setRowCount(0)
        self.coin_list.clear()

    def update_list(self, balances, overview):
        self.investListTable.setRowCount(len(balances) - 1)
        for i, wallet in enumerate(balances):
            balance = float(wallet['balance']) + float(wallet['locked'])
            total_buy_price = np.ceil((float(wallet['balance']) + float(wallet['locked'])) * round(
                float(wallet['avg_buy_price']), 2))
            avg_buy_price = float(wallet['avg_buy_price'])
            display_list = [
                {"currency": wallet['currency'], "korean_name": ""},
                balance,
                avg_buy_price,
                total_buy_price
            ]
            for coin in self.ticker.tickers:
                if coin['market'].replace('KRW-', '') == wallet['currency']:
                    display_list[0]['korean_name'] = coin['korean_name']

            # 보유 현금 받아오기
            if wallet['currency'] == 'KRW':
                overview.current_krw.setText(f"{int(balance):,}")
                continue
            self.coin_list.append({
                "currency": display_list[0]['currency'],
                "balance": display_list[1],
                "avg_buy_price": display_list[2],
                "total_buy_price": display_list[3]
            })

            # 보유코인들 QTableWidget에 넣기
            for col, val in enumerate(display_list):
                item = QTableWidgetItem('')
                if col == 0:
                    if val['korean_name'] != '':
                        item = QTableWidgetItem(f"{val['korean_name']}\n{val['currency']}")
                    else:
                        item = QTableWidgetItem(f"{val['currency']}")
                elif col == 1:
                    item = QTableWidgetItem(f"{val:,.8f}")
                elif col == 2 or col == 3:
                    if val >= 100 or col == 3:
                        item = QTableWidgetItem(f"{int(np.ceil(val)):,} KRW")
                    else:
                        item = QTableWidgetItem(f"{val} KRW")
                # 테이블에 value 값 삽입
                self.investListTable.setItem(i - 1, 4, QTableWidgetItem("동기화 중.."))
                self.investListTable.setItem(i - 1, 5, QTableWidgetItem("동기화 중.."))

                if val == 0:
                    item = QTableWidgetItem("-")
                    self.investListTable.setItem(i - 1, 4, QTableWidgetItem("-"))
                    self.investListTable.setItem(i - 1, 5, QTableWidgetItem("-"))
                self.investListTable.setItem(i - 1, col, item)

    @Slot(float, str)
    def set_data(self, *datas):
        coin = datas[10].replace("KRW-", "")
        # 예를 들어 "이더리움\nETH" 일때 알파벳과 숫자만 매치하는 정규식
        coin_regex = re.compile("[A-Z0-9]+")
        if coin in [c["currency"] for c in self.coin_list]:
            for row in range(self.investListTable.rowCount()):
                # print(coin_regex.search(self.investListTable.item(row, 0).text()).group(), coin)
                if coin_regex.search(self.investListTable.item(row, 0).text()).group() == coin:
                    # 평가금액
                    calculated_price = QTableWidgetItem(f"{int(np.ceil(datas[0] * self.coin_list[row]['balance'])):,} KRW")
                    # 평가손익
                    profit = QTableWidgetItem(
                        f"{(datas[0] / self.coin_list[row]['avg_buy_price'] - 1) * 100:.2f} %\n"
                        f"{int(np.ceil(datas[0] * self.coin_list[row]['balance'] - self.coin_list[row]['total_buy_price'])):,} KRW")
                    # 평가손익이 손해구간일 때
                    # if datas[0] * self.coin_list[row]['balance'] < self.coin_list[row]['total_buy_price']:
                    #     profit = QTableWidgetItem(
                    #         f"{(np.ceil(datas[0] * self.coin_list[row]['balance']) / self.coin_list[row]['total_buy_price'] - 1) * 100:.2f}%\n"
                    #         f"{int(datas[0] * self.coin_list[row]['balance'] - self.coin_list[row]['total_buy_price']):,}")
                    self.investListTable.setItem(row, 4, calculated_price)
                    self.investListTable.setItem(row, 5, profit)
            self.resize_section()
        self.investListTable.resizeRowsToContents()  # 줄 바꿈 가능하도록 변경


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = InvestListWidget()
    widget.show()
    exit(app.exec())
