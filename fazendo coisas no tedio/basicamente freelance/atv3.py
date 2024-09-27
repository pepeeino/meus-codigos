print("Bem-vindos à Madeireira de pepeeino")

def escolha_tipo():
    while True:
        tipo = input("Escolha o tipo de madeira (PIN/PER/MOG/IPE/IMB): ").upper()
        if tipo == "PIN":
            return 150.4
        elif tipo == "PER":
            return 170.2
        elif tipo == "MOG":
            return 190.9
        elif tipo == "IPE":
            return 210.1
        elif tipo == "IMB":
            return 220.7
        else:
            print("Opção inválida. Tente novamente.")

def qtd_toras():
    while True:
        try:
            quantidade = float(input("Digite a quantidade de toras (m³): "))
            if quantidade <= 0 or quantidade > 2000:
                raise ValueError("Valor inválido. Digite um número positivo até 2000 m³.")
            desconto = 0
            if quantidade >= 100 and quantidade < 500:
                desconto = 0.04
            elif quantidade >= 500 and quantidade < 1000:
                desconto = 0.09
            elif quantidade >= 1000:
                desconto = 0.16
            return quantidade, desconto
        except ValueError as e:
            print(e)


def transporte():
    while True:
        opcao = input("Escolha o tipo de transporte (1 - Rodoviário, 2 - Ferroviário, 3 - Hidroviário): ")
        if opcao == "1":
            return 1000
        elif opcao == "2":
            return 2000
        elif opcao == "3":
            return 2500
        else:
            print("Opção de transporte inválida. Tente novamente.")


def calcular_total(tipo_madeira, qtd_toras, desconto, valor_transporte):
    return tipo_madeira * qtd_toras * (1 - desconto) + valor_transporte


tipo_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
valor_transporte = transporte()
total = calcular_total(tipo_madeira, quantidade, desconto, valor_transporte)

print("O valor total a pagar é: R$" + f"{total:.2f}")
