import os
from SecDbUtils.SecDbClasses import *
from abc import ABC, abstractmethod
from SecDbUtils.EquityDataExtractor import EquityDataExtractor

# let us call the mkt data cfg so it will be always evaluated
from SecDbUtils.SecDbClasses import MktDataCfg, AbstractMarkeDataExtractor, Singleton

mkt_data_cfg = MktDataCfg()

extractors = {
    "equity": EquityDataExtractor,
    "none": None
}


# type asset class point(s) quote_style splitting char is _ and . for quote style

class MarketDataExtractor(AbstractMarkeDataExtractor, ABC):
    @classmethod
    def get_extractor(self, coord: dict):
        if coord.get("type"):
            return extractors[coord["type"]]
        else:
            raise Exception("failed to find extractor for type")


# type asset class point(s) quote_style splitting char is _ and . for quote style
class MarketDataLoader(metaclass=Singleton):

    @classmethod
    def get_points(cls, coord: dict):
        if set(["type", "asset", "type"]).issubset(set(coord.keys())):
            return list(MktDataCfg.mkt_data_cfg["market_coordinates"][coord["type"]][coord["asset"]][coord["class"]]["points"])
        else:
            return []

    @classmethod
    def get_classes(cls, coord: dict):
        if set(["type", "asset"]).issubset(set(coord.keys())):
            return list(MktDataCfg.mkt_data_cfg["market_coordinates"][coord["type"]][coord["asset"]].keys())
        else:
            return []

    @classmethod
    def get_assets(cls, coord: dict):
        if set(["type"]).issubset(set(coord.keys())):
            return list(MktDataCfg.mkt_data_cfg["market_coordinates"][coord["type"]].keys())
        else:
            return []

    @classmethod
    def get_types(cls):
       return MktDataCfg.mkt_data_cfg["market_coordinates"].keys()

    @classmethod
    def get_mkt_data(cls, mkt_coords: dict):
        type_ = mkt_coords.get("type", None)

        if not type_:
            raise Exception("failed to have a class to load")

        extractor = MarketDataExtractor.get_extractor(mkt_coords)
        return extractor.load_mkt_data(mkt_coords)
