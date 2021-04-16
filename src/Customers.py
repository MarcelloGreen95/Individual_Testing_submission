from src.ReadCSVFile import ReadCSVFile


class Customers:

    def Load_Customers(self):
        readCSVFile = ReadCSVFile()
        customerData = readCSVFile.getFileData("customer.csv")
        return customerData

    def Format_Customers(self):
        display = ""
        customerData = self.Load_Customers()
        for counter in range(1, len(customerData)):
            display += customerData[counter] + " \n"
        return display
