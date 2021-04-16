from src.LogIn import LogIn


class Main:
    def __init__(self):
        self.property = None

    def main(self):
        logIn = LogIn()
        print(logIn.logIn())

    def setConfig(self, CSVStub):
        pass


if __name__ == '__main__':
    Main.main()
