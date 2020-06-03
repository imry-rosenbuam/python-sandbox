from SecDbUtils.SecDbClasses import *
import datetime
import yaml
from SecDbUtils.MktDataLoader import MarketDataLoader
from SecDbUtils.SecDbClasses import Singleton, LocalSingleton, MktObjData


class Market(metaclass=Singleton):
    _data = MktObjData()
    _mkt_cfg = MktDataCfg()

    def get_date(self):
        if not self._data.mkt_date:
            raise Exception("Market Object has not been initalized")
        return self._data.mkt_date

    def set_date(self, date):
        self._data.mkt_date = date

    def get_mkt_data(self, data_key: str):

        mkt_coord = MktCoordParser.parse_mkt_coord(data_key)

        if not mkt_coord.get("asset", None):
            return None
        else:
            mkt_key = (mkt_coord['type'], mkt_coord['class'], mkt_coord['asset'], mkt_coord['quote'])

        if mkt_key not in self._data.mkt_data.keys():
            self._data.mkt_data[mkt_key] = self._load_mkt_data(data_key)

        return self._data.mkt_data.get(mkt_key, None)

    def _load_mkt_data(self, data_key: str):
        mkt_coord = MktCoordParser.parse_mkt_coord(data_key)

        return MarketDataLoader.get_mkt_data(mkt_coord)

# type asset class point(s) quote_style splitting char is _ and . for quote style
# inflation zcs gbp 10y.yoy
class MktCoordParser(LocalSingleton):
    @classmethod
    def parse_mkt_coord(cls, mkt_coord_str: str):

        mkt_coord = mkt_coord_str.lower().split(".")
        quote_style = "default" if len(mkt_coord) == 1 else mkt_coord.pop()
        mkt_coord = mkt_coord.pop().split("_")
        mkt_coords = {}

        type = mkt_coord.pop(0)  # get type
        mkt_coords["type"] = type

        if len(mkt_coord):
            asset = mkt_coord.pop(0)  # get asset
            mkt_coords["asset"] = asset

        if len(mkt_coord):
            klass = mkt_coord.pop(0)  # get class
            mkt_coords["class"] = klass

        if len(mkt_coord):
            points = mkt_coord  # get point(s)
            mkt_coords["points"] = points

        mkt_coords["quote"] = quote_style

        return mkt_coords


