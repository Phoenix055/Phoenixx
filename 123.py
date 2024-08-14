class User:
    name ='Jordan'

class ABC:
    def __init__(self,letters,number):
        self.letters = letters
        self.number = number

class Comment:
    def __init__(self,username,text,likes = 0):
        self.username = username
        self.text = text
        self.likes = likes
comment1 = Comment('Sardor','Hello','')
print(comment1.text)

class BankAccount:
    def __init__(self,username,balance):
        self.username = username
        self.balance = balance

    def deposit(self,plus):
        self.balance += plus
        print(f'Баланс успешно пополнен на {plus}$. Ваш баланс сейчас {self.balance}$')

    def cash(self,minus):
        if self.balance - minus > 0:
            print(f'Операция прошла успешно. Ваш баланс {self.balance}')
        else:
            print('На вашем счету недостаточно средств')

    def mybalance(self,):
        print(f'Ваш баланс {self.balance}$')

user1 = BankAccount('Aleksey','1000')


