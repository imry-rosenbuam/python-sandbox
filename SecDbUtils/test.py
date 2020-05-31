import pandas as pd
import yfinance as yf
import yahoofinancials
import feather
import os
import  datetime
from SecDbUtils.MktObj import MktObj
import yaml
import sys

xxx = sys.path

#path = "/Users/imryrosenbaum/PycharmProjects/tsdb_data/"


mkt_coord_str = "equity_index_snp500_spot"

date = datetime.date(2019,5,15)

mkt_obj = MktObj()

mkt_obj.set_date(date)

ss = mkt_obj.get_mkt_data(mkt_coord_str)

sdsf = 1