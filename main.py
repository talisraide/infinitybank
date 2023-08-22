from banco import *

from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.deposito import depositar


def menu():
    print("----- BEM VINDO AO BANCO INFINITY -----")
    while True:
        print("1 - Adicionar conta")
        print("2 - Alterar nome")
        print("3 - Consultar conta")
        print("4 - Remover conta")
        print("5 - Listar contas")
        print("6 - Realizar saque")
        print("7 - Realizar depósito")
        print("8 - Consultar saldo")
        print("9 - Realizar Transferência")
        print("10 - Sair")
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo do cliente: "))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input("Digite o número da conta: "))
            nome = input("Digite o novo nome: ")
            atualizarNome(conta, nome)
        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            print(obterConta(conta))
        elif opcao == 4:
            conta = int(input("Digite o número da conta: "))
            deletarConta(conta)
        elif opcao == 5:
            listarContas()
        elif opcao == 6:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser sacado: "))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser depositado: "))
            depositar(conta, valor)
        elif opcao == 8:
            conta = int(input("Digite o número da conta: "))
            consultarSaldo(conta)
        elif opcao == 9:
            contaOri = int(input("Digite a conta origem: "))
            contaDes = int(input("Digite a conta destino: "))
            valor = float(input("Informe o valor a ser transferido: "))
            transferir(contaOri, contaDes, valor)
        elif opcao == 10:
            print("Programa encerrado, tenha um bom dia.")
            break
        else:
            print("Opção inválida.")

menu()
