from SecDbUtils.SecDbClasses import AbstractMarkeDataExtractor, MktDataLoader


class EquityDataExtractor(AbstractMarkeDataExtractor):

    @classmethod
    def load_mkt_data(cls, mkt_coord: dict):
        print("loading equity data")
        return _equity_mkt_load(mkt_coord)


def _equity_mkt_load(mkt_coord: dict):
    asset = mkt_coord["asset"]

    mkt_data_loaders = {
        "index": _EquityIndexDataLoader.mkt_data_load
    }

    mkt_data_loader = mkt_data_loaders.get(asset,None)
    return mkt_data_loader(mkt_coord)

class _EquityIndexDataLoader(MktDataLoader):
    def mkt_data_load(cls,mkt_coord:dict):
        return 1;

