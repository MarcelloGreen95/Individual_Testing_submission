import unittest
from unittest.mock import MagicMock
from src.CSVStub import CSVStub
from src.main import Main
from src.LogIn import LogIn
from src.Customers import Customers
from src.ReadCSVFile import ReadCSVFile


class Test_LogIn(unittest.TestCase):
    logIn = LogIn()
    main = Main()
    customers = Customers()

    listOfFakeNumbers = ['07946450569', '07958963214']

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.readCSVFile = None

    def test_CustomerInfo(self):
        customerInfo = self.readCSVFile.getFileData("Customer/", "customer.csv")
        customerColumns = customerInfo[0]
        self.assertEqual(customerColumns, ["Customers", ])

    def test_mockSingleResult(self):
        propertyData = []
        propertyData.append("Customers")
        propertyData.append("07946450569, 07958963214")

        self.logIn.property = []
        self.logIn.config.getConfig = MagicMock(return_value=propertyData)
        result = self.logIn.getCustomers()

        self.assertEqual(['Customers'], result)

    def test_mockEnterUserPassword(self):
        LogIn.getUserInfo = MagicMock(return_value='07946450569')
        self.assertEqual('Enter password', self.logIn.display())

    def test_getCustomerDataFromStub(self):
        self.main.setConfig(CSVStub)
        customerData = self.main.property
        customerColumns = customerData[0]
        self.assertEqual(customerColumns, "phoneNumber")

    def test_FakeList(self):
        displayFakeList = LogIn()
        fakeNumbers = Test_LogIn.listOfFakeNumbers
        displayFakeList.getCustomers = MagicMock(return_value=fakeNumbers.pop())
        self.assertEqual('Enter password', displayFakeList.display())


if __name__ == '__main__':
    unittest.main()
