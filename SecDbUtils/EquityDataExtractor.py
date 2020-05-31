from SecDbUtils.SecDbClasses import AbstractMarkeDataExtractor, MktDataLoader, MktObjData
from SecDbUtils.EquityMarketizer import EquityMarketiser
import datetime

class EquityDataExtractor(AbstractMarkeDataExtractor):

    @classmethod
    def load_mkt_data(cls, mkt_coord: dict):
        print("loading equity data")
        return _equity_mkt_load(mkt_coord)


def _equity_mkt_load(mkt_coord: dict):
    asset = mkt_coord["asset"]

    mkt_equity_data_loaders = {
        "index": _EquityIndexDataLoader.mkt_data_load
    }

    mkt_data_loader = mkt_equity_data_loaders.get(asset, None)
    return mkt_data_loader(mkt_coord)


class _EquityIndexDataLoader(MktDataLoader):

    @classmethod
    def mkt_data_load(mcs, mkt_coord: dict):
        mkt_obj = MktObjData()
        date = mkt_obj.mkt_date

        ticker: str = mkt_coord.get("class", None)
        pt = mkt_coord.get("points", None)
        if not ticker:
            raise Exception("No class provided in the mkt coordinates")
        elif "spot" not in pt:
            raise Exception("Wrong point given")

        return EquityMarketiser.get_equity_ticker_data_point(ticker.upper(), date)
