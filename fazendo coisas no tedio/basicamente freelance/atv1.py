print("Sistema desenvolvido por Gustavo")

valorBase = float(input("Informe o valor base do plano: "))
idadeDoCliente = int(input("Informe a idade do cliente: "))

if idadeDoCliente >= 0 and idadeDoCliente < 19:
    percentual = 1.0
elif idadeDoCliente >= 19 and idadeDoCliente < 29:
    percentual = 1.5
elif idadeDoCliente >= 29 and idadeDoCliente < 39:
    percentual = 2.25
elif idadeDoCliente >= 39 and idadeDoCliente < 49:
    percentual = 2.4
elif idadeDoCliente >= 49 and idadeDoCliente < 59:
    percentual = 3.5
elif idadeDoCliente >= 59:
    percentual = 6.0
else:
    percentual = None
    print("Idade inválida.")

if percentual is not None:
    valorMensal = valorBase * percentual
    print(f"O valor mensal do plano é de: {valorMensal}")
