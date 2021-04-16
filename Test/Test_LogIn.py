import unittest
from unittest.mock import MagicMock
from src.main import Main
from src.LogIn import LogIn
from src.Customers import Customers
from src.ReadCSVFile import ReadCSVFile
import faker


class Test_LogIn(unittest.TestCase):
    logIn = LogIn()
    main = Main()
    Customers = Customers()

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.readCSVFile = None

    def test_CustomerInfo(self):
        customerInfo = self.readCSVFile.getFiledata("Customer/", "customer.csv")
        customerColumns = customerInfo[0]
        self.assertEqual(customerColumns, ["Customers", ])

    def test_mockSingleResult(self):
        propertyData = []
        propertyData.append("Customers")
        propertyData.append("derek.somerville@glasgow.ac.uk, matthew.barr@glasgow.ac.uk")

        self.LogIn.property = []
        self.LogIn.config.getConfig = MagicMock(return_value=propertyData)
        result = self.LogIn.getCustomers()

        self.assertEqual(['Customers'], result)

    def test_mockEnterUserPassword(self):
        LogIn.getUserInfo = MagicMock(return_value='matthew.barr@glasgow.ac.uk')
        self.assertEqual('Enter password', self.logIn.display())


if __name__ == '__main__':
    unittest.main()
