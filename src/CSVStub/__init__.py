class ReadInterface:
    def getConfig(self): pass


class CSVStub(ReadInterface):

    def getConfig(self):
        stubData = []
        stubData.append("Email")
        stubData.append("derek.somerville@glasgow.ac.uk")
        stubData.append("matthew.barr@glasgow.ac.uk")
        stubData.append("e.kelly.1@research.gla.ac.uk")
        return stubData

