import pyupbit


class Ticker:
    def __init__(self):
        self.tickers = [x for x in pyupbit.get_tickers(verbose=True) if x['market'].startswith('KRW')]
        self.markets = [x['market'] for x in self.tickers]
        self.tickers_kor = [x['korean_name'] for x in self.tickers]
