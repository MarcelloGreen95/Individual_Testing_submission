from src.Customers import Customers


class NewCustomer:

    def NewCustomer(self):
        print("\nPlease add a new customer to the customer list")

        while True:
            try:
                NewCustomerNumber = int(input("\nEnter new customer phone number here:"))
                print("\nYou have now added", NewCustomerNumber, "to the customer list ")
                break
            except ValueError:
                print("\nPlease enter a number.")
                print()
