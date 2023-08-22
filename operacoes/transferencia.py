from banco import obterConta, banco


def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaDestino and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print("Transferência realizada com sucesso.")
        else:
            print("Saldo insuficiente")
    else:
        print("Uma ou mais contas não existem.")


if __name__ == "__main__":
    print(banco)
    transferir(1, 2, 500)
    print(banco)