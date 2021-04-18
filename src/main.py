from src.LogIn import LogIn
from src.NewCustomer import NewCustomer


class Main:
    def __init__(self):
        self.property = None

    def main(self):
        logIn = LogIn()
        print(logIn.logIn())
        newCustomer = NewCustomer()
        newCustomer.NewCustomer()

    def setConfig(self, CSVStub):
        pass


if __name__ == '__main__':
    Main.main()
