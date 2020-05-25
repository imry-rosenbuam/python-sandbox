import os
from SecDbClasses import *
from abc import ABC, abstractmethod
from EquityDataExtractor import *
import EquityDataExtractor as xs

# let us call the mkt data cfg so it will be always evaluated
from SecDbUtils.SecDbClasses import MktDataCfg, AbstractMarkeDataExtractor, Singleton

mkt_data_cfg = MktDataCfg()

extractors = {
    "equity": EquityDataExtractor,
    "none": None
}


# type asset class point(s) quote_style splitting char is _ and . for quote style

class MarketDataExtractor(AbstractMarkeDataExtractor):

    @classmethod
    def get_extractor(self, date, coord: dict):
        if coord.get("type"):
            return extractors[coord["type"]]
        else:
            raise "failed to find extractor for type"


# type asset class point(s) quote_style splitting char is _ and . for quote style
class MarketDataLoader(metaclass=Singleton):

    @classmethod
    def get_points(cls, coord: dict):
        MarketDataExtractor.get_extractor()

    @classmethod
    def get_assets(cls, coord: dict):
        MarketDataExtractor.get_extractor()

    @classmethod
    def get_classes(cls, coord: dict):
        MarketDataExtractor.get_extractor()

    @classmethod
    def get_types(cls):
        MarketDataExtractor.get_extractor()

    @classmethod
    def get_mkt_data(cls, mkt_coords: dict):
        type_ = mkt_coords.get("type", None)

        if not type_:
            raise ("failed to havea a class to load")

        extractor = MarketDataExtractor.get_extractor(type_)
        return extractor.load_mkt_data(mkt_coords)
