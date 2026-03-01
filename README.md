# simple-bank-backend
Sistema de Conta Bancária em Python
Este projeto consiste em uma simulação de sistema bancário simples, desenvolvido para exercitar conceitos de Programação Orientada a Objetos (POO) e manipulação de fluxos de decisão em Python.

# Funcionalidades
O sistema permite que o usuário realize as seguintes operações:

Consultar Saldo: Exibe o valor total disponível na conta.

Realizar Depósito: Adiciona um valor positivo ao saldo existente.

Realizar Saque: Retira um valor da conta, desde que haja saldo suficiente.

Interface de Menu: Navegação interativa via terminal com tratamento de opções.

# Estrutura do Código
O projeto é estruturado em torno da classe ContaBancaria, que utiliza o conceito de encapsulamento para proteger o saldo (atributo privado __saldo).

# Métodos Principais:
__init__(self, saldo_inicial): Inicializa a conta com um valor definido.

depositar(valor): Valida se o depósito é positivo antes de somar ao saldo.

sacar(valor): Verifica se o valor é positivo e se há saldo disponível para a operação.

ver_saldo(): Formata e exibe o saldo atual para o usuário.

# Tecnologias utilizadas

Linguagem: Python

Paradigma: Orientada a Objetos (POO)

Interface: CLI (Interface de Linha de Comando)

# Exemplo de Uso:

Ao iniciar o programa, o usuário informa seu nome e é apresentado ao seguinte menu:

```

--------MENU DE OPÇÕES----------
1. SALDO | 2. DEPOSITAR | 3. SACAR | 4. SAIR


```


