
import pybithumb
import datetime
import time
con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)
list_graph = []
########## 목표 금액 ###########
def get_target_price(ticker):
    df = pybithumb.get_candlestick(ticker) # 전일 시가, 종가, 고가, 저가 정보
    print(df.tail())
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5 # 변동성 돌파전략
    return target

########## 자동 매수 ###########
def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2] # 계좌 잔액
    orderbook = pybithumb.get_orderbook(ticker) # 해당 코인의 현재 가격
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price) # 매수 가능한 코인 개수
    bithumb.buy_market_order(ticker, unit) # 매수 함수
    result = bithumb.get_balance(ticker)[2]
    print("☆☆☆매수 알림☆☆☆")
    print("코인 : ", ticker)
    print("금액 : ", orderbook)
    print("잔액 : ", result)

########## 자동 매도 ###########
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0] # 현재 코인 가격
    bithumb.sell_market_order(ticker, unit) # 매도 함수
    result = bithumb.get_balance(ticker)[2]
    print("☆☆☆매도 알림☆☆☆")
    print("코인 : ", ticker)
    print("금액 : ", unit)
    print("잔액 : ", result)

if __name__ == '__main__':
    tickers = pybithumb.get_tickers()
    get_target_price(tickers)
    buy_crypto_currency(tickers)
    sell_crypto_currency(tickers)