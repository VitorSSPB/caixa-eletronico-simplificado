def exibir_menu():
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1) Consultar saldo")
    print("2) Depositar")
    print("3) Sacar")
    print("4) Sair")
    escolha = input("Escolha uma opção: ")
    return escolha


def consultar_saldo(saldo):
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")


def depositar(saldo, valor):
    if valor <= 0:
        print("\nErro: o valor do depósito deve ser positivo.")
        return saldo

    novo_saldo = saldo + valor
    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    return novo_saldo


def sacar(saldo, valor):
    if valor <= 0:
        print("\nErro: o valor do saque deve ser positivo.")
        return saldo

    if valor > saldo:
        print("\nErro: saldo insuficiente para realizar o saque.")
        return saldo

    novo_saldo = saldo - valor
    print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    return novo_saldo


def ler_valor(mensagem):
    try:
        valor = float(input(mensagem))
        return valor
    except ValueError:
        print("\nErro: digite um valor numérico válido.")
        return None


def main():
    saldo = 0.0
    opcao = ""

    while opcao != "4":
        opcao = exibir_menu()

        if opcao == "1":
            consultar_saldo(saldo)

        elif opcao == "2":
            valor = ler_valor("Digite o valor do depósito: R$ ")
            if valor is not None:
                saldo = depositar(saldo, valor)

        elif opcao == "3":
            valor = ler_valor("Digite o valor do saque: R$ ")
            if valor is not None:
                saldo = sacar(saldo, valor)

        elif opcao == "4":
            print("\nEncerrando o caixa eletrônico. Até logo!")

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()