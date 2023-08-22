from banco import obterConta, banco


def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu saldo = {cliente['saldo']}")
    else:
        print("Conta não existe.")


if __name__ == "__main__":
    consultarSaldo(1)
    consultarSaldo(2)
    consultarSaldo(3)
    print(banco)