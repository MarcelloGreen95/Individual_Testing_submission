from src.Customers import Customers


class LogIn:
    def __init__(self):
        self.config = None

    def Get_Password(self, phoneNumber):
        customers = Customers()
        customerData = customers.Load_Customers()
        password = ""
        counter = 0
        while password == "" and counter < len(customerData):
            if phoneNumber == customerData[counter][0]:
                password = customerData[counter][3]
            counter += 1
        return password

    def logIn(self):
        phoneNumber = input("Enter your email address")
        password = self.Get_Password(phoneNumber)
        if password == "":
            result = "You are not a user"
        else:
            if input("Enter password") == password:
                result = "You are logged in"
            else:
                result = "Wrong password, no second chances"
        return result

    def getCustomers(self):
        return self.getCustomers()

    def display(self):
        return self.logIn()
