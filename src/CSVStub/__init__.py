class ReadInterface:
    def getConfig(self): pass


class CSVStub(ReadInterface):

    def getConfig(self):
        stubData = []
        stubData.append("phoneNumber")
        stubData.append("07946450569")
        stubData.append("07958963214")
        stubData.append("07798621358")
        return stubData

