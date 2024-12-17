# Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        if isinstance(account_holder, str):
            self.account_holder = account_holder
        else:
            self.account_holder = ""
            print("Le nom doit être un texte")
        if isinstance(balance, float) or isinstance(balance, int):
            float(balance)
            self.balance = balance
        else:
            print("Le solde doit être un nombre")
            self.balance = 0

    def deposit(self, amount):
        if isinstance(amount, float) or isinstance(amount, int):
            if amount > 0:
                self.balance = self.balance + amount
            else:
                print("Le dépôt ne peut pas être négatif")
        else:
            print("Le dépot doit être un nombre")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print(f"Le solde ({self.balance}€) n'est pas suffisant pour ce retrait ({amount}€)")

    def display_balance(self):
        print(f"Le propriétaire du compte est {self.account_holder} et le solde est de {self.balance}€")


account = BankAccount("Anthony", 2000)
account.display_balance()
account.deposit(300)
account.deposit(-300)
account.display_balance()
account.withdraw(500)
account.display_balance()
account.withdraw(2500)
