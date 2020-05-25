from SecDbClasses import *
import datetime
import yaml
from mkt_data_loader import *

from SecDbUtils.SecDbClasses import Singleton, LocalSingleton


class mktObj(metaclass=Singleton):
    _date = datetime.date.today()
    _dateStr = "ss"
    _mkt_data = {}

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_mkt_data(self, data_key: str):
        s = dict()

        if data_key not in s.keys():
            x._load_mkt_data(data_key)

        return self._mkt_data.get(data_key, None)

    def _load_mkt_data(self, data_key: str):
        mkt_coord = MktCoordParser.Parse_Mkt_Coord(data_key)

        mkt_loader = MarketDataloader.get_market_loader(mkt_coord)


# type asset class point(s) quote_style splitting char is _ and . for quote style
# inflation zcs gbp 10y.yoy
class MktCoordParser(LocalSingleton):
    @classmethod
    def parse_mkt_coord(cls, mkt_coord_str: str):

        mkt_coord = mkt_coord_str.lower().split(".")
        quote_style = "default" if len(mkt_coord) == 1 else mkt_coord.pop()
        mkt_coord = mkt_coord.pop().split("_")
        mkt_coords = {}

        type = mkt_coord.pop()  # get type
        mkt_coords["type"] = type

        if len(mkt_coord):
            asset = mkt_coord.pop()  # get asset
            mkt_coords["asset"] = asset

        if len(mkt_coord):
            klass = mkt_coord.pop()  # get class
            mkt_coords["class"] = klass

        if len(mkt_coord):
            points = mkt_coord  # get point(s)
            mkt_coords["points"] = points

        mkt_coords["quote"] = quote_style

        return mkt_coords


xxx = 1
