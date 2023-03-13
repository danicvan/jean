class Account:

    __agency = None
    __account_number = None
    __account_holder = None
    __account_balance = 0.00

    def __init__(
        self, 
        agency:str, 
        account_number: str, 
        account_holder: str, 
        account_balance: float
    ) -> None:
        self.__agency = agency
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__account_balance = account_balance

    # Get

    def get_agency(self):
        return self.__agency

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_account_balance(self):
        return self.__account_balance
        
    # Set

    def set_agency(self, agency):
        self.__agency = agency

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def set_account_balance(self, balance):
        self.__account_balance = balance

    def cash_in(self, amount: float):
        self.__account_balance += amount

    def cash_out(self, amount: float):
        self.__account_balance -= amount

    def __has_balance(self):
        has_balance = 

def main():
    account_01 = Account(
        agency="001",
        account_number="12345678-9",
        account_holder="Daniel Camilo",
        account_balance=10000.00
    )

    account_01.set_account_balance(10000.00);
    account_01.cash_in(5000.00);
    account_01.cash_out(15.12);

    print(account_01.get_account_balance())

if __name__ == "__main__":
    main()