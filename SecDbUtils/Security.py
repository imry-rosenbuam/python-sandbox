

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

    def __init__(self,economicData):
        SecValidation(economicData)
        self.__economicData = economicData

    def Price(self):
        raise NotImplementedError
    def GetCcy(self):
        return self.__economicData.ccy
    def DollarPrice(self, mkt):
        return mkt.getFxSpot(self.GetCcy(), "USD")

