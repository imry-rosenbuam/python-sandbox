from SecDbUtils.SecDbClasses import Marketizer
import pandas
import sys
import yfinance as yf
import os
import yahoofinancials
import datetime

equity_tickers_to_marketsie = {
    "TESLA": 'TSLA',
    "SNP500": '^GSPC'
}


class equity_marketiser(Marketizer):
    @classmethod
    def get_equity_ticker_data(cls, ticker: str, start_date: datetime, end_date: datetime) -> pandas.DataFrame:
        df = yf.download(ticker,
                         start=start_date,
                         end=end_date,
                         progress=False)
        return df

    @classmethod
    def marketise_equity_data(cls, file_name: str, ticker: str, start_date: datetime, end_date: datetime) -> None:
        #we might need to add index as the timestamp in order to make retrivel of points easier via feather
        df = cls.marketize_load(file_name)

        df_new = cls.get_equity_ticker_data(ticker, start_date, end_date)

        if not df.empty:
            df.update(df_new)
        else:
            df = df_new

        cls.marketize_save(df, file_name)


if __name__ == "__main__":
    arg = sys.argv
    arg.pop(0)

    marketiser = equity_marketiser()
    tickers_to_marketise = equity_tickers_to_marketsie.keys()

    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=1)

    if len(arg) == 0:
        raise ('not enough args provided')
    elif len(arg) == 3:
        temp_arg = arg.pop(0).lower()

        if temp_arg != 'all':
            if arg in tickers_to_marketise:
                tickers_to_marketise = [arg]
            else:
                raise Exception('Wrong Ticker')

        temp_arg = arg.pop(0).lower()
        start_date = datetime.datetime.strptime(temp_arg, '%Y-%m-%d')

        temp_arg = arg.pop(0).lower()
        end_date = datetime.datetime.strptime(temp_arg, '%Y-%m-%d')
    elif len(arg) == 2:
        temp_arg = arg.pop().lower()

        if temp_arg != 'all':
            if arg in tickers_to_marketise:
                tickers_to_marketise = [arg]
            else:
                raise Exception('Wrong Ticker')

        temp_arg = arg.pop().lower()
        if temp_arg == 'PREV':
            start_date = start_date + datetime.timedelta(days=-1)
            end_date = end_date + datetime.timedelta(days=-1)
        elif temp_arg == 'TODAY':
            pass

    elif len(arg) == 1:
        arg = arg.pop().upper()

        if arg == 'PREV':
            start_date = start_date + datetime.timedelta(days=-1)
            end_date = end_date + datetime.timedelta(days=-1)
        elif arg == 'TODAY':
            pass

    for k in tickers_to_marketise:
        v = equity_tickers_to_marketsie.get(k, "")
        marketiser.marketise_equity_data(k, v, start_date, end_date)
        print("the ticker " + v + " has been marketised succesfuly")

    xx = 1
