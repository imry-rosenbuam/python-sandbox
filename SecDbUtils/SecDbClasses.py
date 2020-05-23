import datetime
import yaml
from abc import ABC,abstractmethod

class Singleton(type,ABC):
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
class AbstractMarkeDataExtractor(LocalSingleton,ABC):

    @classmethod
    @abstractmethod
    def load_mkt_data(cls, coord:dict):
        print("loading equity data")


class MktDataCfg:

    def __init__(self):
        with open('market_coords_cfg.YAML') as f:
            MktDataCfg.mkt_data_cfg = yaml.load(f, Loader=yaml.FullLoader).get("market_coordinates")

