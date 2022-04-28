import sys
from PySide6.QtCore import Slot, QStringListModel
from PySide6.QtWidgets import QWidget, QApplication, QCompleter
from Widgets.InvestListWidget import InvestListWidget
from util.Loading import Loading
from UI.OverviewUI import Ui_Form
from util.Ticker import Ticker


class OverviewWidget(QWidget, Ui_Form):
    def __init__(self, parent=None, ticker="KRW-BTC"):
        super().__init__(parent)
        self.setupUi(self)
        self.ticker = ticker
        self.loading = Loading(self)  # loading 위젯 로드
        self.getTicker = Ticker()
        self.investListWidget = InvestListWidget()
        self.ticker_cb.addItems(self.getTicker.tickers_kor)  # 한글 코인이름으로 목록 작성

        # 코인이름 autocomplete 설정
        model = QStringListModel()
        model.setStringList(self.getTicker.tickers_kor)
        completer = QCompleter()
        completer.setModel(model)
        self.ticker_cb.setCompleter(completer)
        self.ticker_cb.currentIndexChanged.connect(self.select_ticker)

        self.loading.start()

    def select_ticker(self):
        # 한글 이름을 market_code로 변경
        for select_coin in self.getTicker.tickers:
            if select_coin['korean_name'] == self.ticker_cb.currentText():
                self.ticker = select_coin['market']
        self.loading.start()  # 로딩 시작

    @Slot(float, str)
    def set_data(self, trade_price, change_rate, acc_trade_volume_24h, high_price, acc_trade_price_24h, low_price,
                 acc_bid_volume, acc_ask_volume, prev_closing_price, change, current_ticker):
        watch_list = [{"code": "KRW-WAVES", "price": 25220}, {"code": "KRW-ETH", "price": 3799000}]
        if self.ticker == current_ticker:
            if trade_price < 100:
                self.trade_price.setText(f"{trade_price:.2f}")
                self.prev_closing_price.setText(f"{prev_closing_price:.2f}")
                self.high_price.setText(f"{high_price:.2f}")
                self.low_price.setText(f"{low_price:.2f}")
            else:
                self.trade_price.setText(f"{int(trade_price):,}")
                self.prev_closing_price.setText(f"{int(prev_closing_price):,}")
                self.high_price.setText(f"{int(high_price):,}")
                self.low_price.setText(f"{int(low_price):,}")

            if change == 'RISE':
                self.change_rate.setText(f"+{change_rate * 100:.2f}%")
            else:
                self.change_rate.setText(f"-{change_rate * 100:.2f}%")

            self.trade_volume_24H.setText(f"{round(acc_trade_volume_24h):,} {current_ticker.replace('KRW-', '')}")
            self.volume.setText(f"{acc_trade_price_24h / 100000000:,.2f} 억")
            self.volume_power.setText(f"{acc_bid_volume / acc_ask_volume * 100:+.2f}%")

            self.loading.stop()  # 로딩 멈춤
            self.update_style(change)

        # for a in watch_list:
            # if current_ticker == a["code"] and trade_price <= a["price"]:
                # print(f"{current_ticker} 현재가격: {trade_price}, 감시가격: {a['price']}, 감시 가격 도달")

    def update_style(self, change):
        if change == "FALL":
            self.trade_price.setStyleSheet("color:blue;")
            self.change_rate.setStyleSheet("background-color:blue;color:white;")
        elif change == "RISE":
            self.trade_price.setStyleSheet("color:red;")
            self.change_rate.setStyleSheet("background-color:red;color:white;")
        elif change == "EVEN":
            self.trade_price.setStyleSheet("color:black;")
            self.change_rate.setStyleSheet("background-color:black;color:white;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ob = OverviewWidget()
    ob.show()
    exit(app.exec())
