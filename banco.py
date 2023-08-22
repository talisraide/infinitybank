from typing import Optional

banco = [
    {"conta": 1, "cliente": "Elias", "saldo": 1500.00}, {"conta": 2, "cliente": "Mariana", "saldo": 2000.00}
]

conta_atual = 2


def adicionarConta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {"conta": conta_atual, "cliente": nome, "saldo": saldo}
    banco.append(conta)
    print("Conta cadastrada com sucesso!")


def obterConta(conta: int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def atualizarNome(conta: int, novo_nome: str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['cliente'] = novo_nome
        print("Nome alterado com sucesso!")
    else:
        print("Conta não existe.")


def deletarConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print("Conta removida com sucesso!")
    else:
        print("Conta não existe!")


def listarContas() -> None:
    for cliente in banco:
        print(f"N. conta: {cliente['conta']}")
        print(f"Nome: {cliente['cliente']}")
        print(f"Saldo: {cliente['saldo']}")
        print('----------------------')

if __name__ == "__main__":
    adicionarConta("Luis", 1300.00)
    adicionarConta("Luana", 250.00)
    print(banco)
    print(obterConta(2))
    print(obterConta(10))
    atualizarNome(2, "Emanuel")
    atualizarNome(10, "Leandro")
    print(banco)
    deletarConta(2)
    print(banco)
    listarContas()