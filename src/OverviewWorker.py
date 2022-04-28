from pyupbit import WebSocketManager
from PySide6.QtCore import Signal, QThread


class OverviewWorker(QThread):
    dataSent = Signal(float, float, float, float, float, float, float, float, float, str, str)

    def __init__(self, markets):
        super().__init__()
        self.markets = markets
        # self.ticker = ticker  # 현재 선택 중인 ticker
        self.alive = True
        # self.loading = loading

    def close(self):
        self.alive = False
        self.wait()

    def run(self):
        wm = WebSocketManager("ticker", self.markets)  # self.markets = ["KRW-BTC", "KRW-ETH", ...]
        while self.alive:
            data = wm.get()
            self.dataSent.emit(
                float(data['trade_price']),
                float(data['change_rate']),
                float(data['acc_trade_volume_24h']),
                float(data['high_price']),
                float(data['acc_trade_price_24h']),
                float(data['low_price']),
                float(data['acc_bid_volume']),
                float(data['acc_ask_volume']),
                float(data['prev_closing_price']),
                str(data['change']),
                str(data['code'])
            )
        wm.terminate()
