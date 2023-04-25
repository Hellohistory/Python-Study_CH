import ccxt

# 需要注意！！在中国大陆这段代码可能会出现访问错误

def getprice(symbol, exchange_id):
    symbol = symbol.upper()  # 将symbol转换为大写，方便后续处理。例如：btc/usdt -> BTC/USDT
    exchange_id = exchange_id.lower()  # 将exchange_id转换为小写，方便后续处理。例如：BINANCE -> binance
    symbol_1 = symbol.split("/")  # 将symbol按照'/'分割，例如：BTC/USDT -> ['BTC', 'USDT']
    exchange = getattr(ccxt, exchange_id)(
        {
            # https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
            "enableRateLimit": True  # 启用速率限制
        }
    )
    try:
        v_price = exchange.fetch_ticker(symbol)  # 获取交易对的最新价格
        r_price = v_price["info"]["lastPrice"]  # 获取最新价格
        if symbol_1[1] == "USD" or symbol_1[1] == "USDT":  # 如果交易对中的计价货币是USD或USDT
            v_return = "{:.2f} {}".format(float(r_price), symbol_1[1])  # 将价格保留两位小数，并添加计价货币符号
            return v_return
        else:
            v_return = "{:.8f} {}".format(float(r_price), symbol_1[1])  # 将价格保留八位小数，并添加计价货币符号
            return v_return
    except (ccxt.ExchangeError, ccxt.NetworkError) as error:
        # 添加必要的处理或重新抛出异常
        return "发生错误", type(error).__name__, error.args
    raise


print(getprice("btc/usdt", "BINANCE"))  # 获取BINANCE交易所中BTC/USDT的最新价格
print(getprice("btc/usd", "BITMEX"))  # 获取BITMEX交易所中BTC/USD的最新价格
