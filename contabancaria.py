class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!!') 
        
        else:
            print('VALOR NÃO ACEITO!!')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} realizado!!')

        else:
            print('Saldo insuficiente')
    def ver_saldo(self):
        print(f'O seu saldo disponível é de R${self.__saldo:.2f}')

nome_cliente = input('informe seu nome: ')
print(f'Bem vindo, {nome_cliente.upper()}')

minha_conta = ContaBancaria(1000)

while True:
    print('\n--------MENU DE OPÇÕES----------')
    print('\n1. SALDO | 2. DEPOSITAR | 3. SACAR | 4.SAIR')
    

    opcao =  input('O que deseja fazer agora?  ').upper()

    if opcao == '1' or opcao == 'SALDO':
        minha_conta.ver_saldo()
        print('-'*30)

    elif opcao =='2' or opcao == 'DEPOSITAR':
        v = float(input('Quanto deseja depositar?  '))
        minha_conta.depositar(v)
        print('-'*30)
    
    elif opcao =='3' or opcao == 'SACAR':
        v = float(input('Quando deseja sacar? '))
        minha_conta.sacar(v)
        print('-'*30)
    
    elif opcao == '4' or opcao == 'SAIR':
        print('Até logo!!')
        break
    else:
        print('Opção inválida!!')

    #DEU CERTO VAMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        