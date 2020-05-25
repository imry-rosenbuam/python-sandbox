def SecValidation(economicData):
    # values that need to be populated
    vals = {
        "CCY",
        "CLASS NAME"
    }
    if vals.isdisjoint(set(economicData.keys())):
        raise AssertionError


class Security:
    __economicData = {}

    def __init__(self, economic_data):
        SecValidation(economic_data)
        self.__economicData = economic_data

    def price(self):
        raise NotImplementedError

    def get_ccy(self):
        return self.__economicData.ccy

    def dollar_price(self, mkt):
        return mkt.getFxSpot(self.GetCcy(), "USD")
