class CurrentAccount:

    """ The class is responsible for handling the current account while the program is running.
        When the program is closed, the current account ceases to exist. """

    ''' Function that initializes the attributes of the CurrentAccount class: '''
    def __init__(self, balance, drawMoney, addMoney):
        self.balance = balance
        self.drawMoney = drawMoney
        self.addMoney = addMoney

    ''' Function that performs the deposit of the corresponding amount and updates the balance: '''
    def deposit(self, addMoney):
        self.balance += addMoney
        self.return_balance()

    ''' Function that withdraws the desired value.
        If the amount is less than the remaining balance, withdrawal is not allowed. '''
    def redraw(self, drawMoney):
        if self.balance - drawMoney < 0:
            print('O valor a ser sacado é maior que o saldo restante, saque não permitido!')
        else:
            self.balance -= drawMoney
            self.return_balance()

    ''' Function that only returns the updated balance. '''
    def return_balance(self):
        print('\nSeu saldo atualizado é de R${:.2f}.'.format(self.balance))


option = -1

print('Banco Burresco, seja bem vindo!')

c1 = CurrentAccount(0, 0, 0)

while option != 0:
    print('\nDigite a opção desejada: ')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Saldo')
    print('4 - Renomear nome correntista')
    print('0 - Encerrar')
    option = int(input('\nOpção: '))

    if option == 1:
        c1.deposit(float(input('Digite o valor a ser depositado: ')))

    if option == 2:
        c1.redraw(float(input('Digite o valor a ser sacado: ')))

    if option == 3:
        c1.return_balance()

    if option == 0:
        print('\nConta-corrente encerrada. Volte sempre!')
