import datetime
import yaml
from abc import ABC, abstractmethod
import feather
import pandas as pd
import os
import pyarrow.parquet as pq

path = "/Users/imryrosenbaum/PycharmProjects/tsdb_data/"


class Singleton(type, ABC):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            super()
        return cls._instances[cls]


class LocalSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


# type asset class point(s) quote_style splitting char is _ and . for quote style
class AbstractMarkeDataExtractor(LocalSingleton, ABC):

    @classmethod
    @abstractmethod
    def load_mkt_data(cls, coord: dict):
        print("loading equity data")


class MktDataLoader(Singleton):
    @classmethod
    @abstractmethod
    def mkt_data_load(mcs, mkt_coord: dict):
        pass


class MktDataCfg(metaclass=Singleton):

    def __init__(self):
        with open('market_coords_cfg.YAML') as f:
            MktDataCfg.mkt_data_cfg = yaml.load(f, Loader=yaml.FullLoader).get("market_coordinates")


class Marketizer:
    @classmethod
    def marketize_save(cls, df: pd.DataFrame, file_name: str, msg: str = "") -> None:
        # feather.write_dataframe(df, cls.file_path(file_name))
        df.to_parquet(cls.file_path(file_name))
        if msg == "":
            print("markeitzed to " + file_name)
        else:
            print(msg)

    @classmethod
    def marketize_load(cls, file_name: str) -> pd.DataFrame:
        if os.path.isfile(cls.file_path(file_name)):
            # df = feather.read_dataframe(cls.file_path(file_name))
            df = pd.read_parquet(cls.file_path(file_name))
            return df

        return pd.DataFrame()

    @classmethod
    def file_path(cls, file_name: str):
        return path + file_name + '.parquet'

class MktObjData(metaclass=Singleton):
    mkt_date = None
    mkt_data = {}

class Mkt_Conventions:
    future_codes = {
        "january": "F",
        "february": "G",
        "march": "H",
        "april": "J",
        "may": "K",
        "june": "M",
        "july": "N",
        "august": "Q",
        "september": "U",
        "october": "V",
        "november": "X",
        "december": "Z"
    }
