import csv
from src.CSVStub import ReadInterface


class ReadCSVFile(ReadInterface):
    filePathPrefix = "Customer/"

    def getFileData(self, directory, fileName):
        fileData = []
        with open("Customer/" + directory + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self, directory, fileName, numberOfLines):
        return self.getFileData(directory, fileName)[-1 * numberOfLines]
