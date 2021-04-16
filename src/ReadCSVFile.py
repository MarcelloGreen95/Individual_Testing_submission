import csv


class ReadCSVFile:

    def Get_File_Data(self, fileName):
        fileData = []
        with open("resource/" + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self, fileName, numberOfLines):
        return self.Get_File_Data(fileName)[-1 * numberOfLines]
