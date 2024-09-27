print("Bem-vindos à Pizzaria do Gustavo")

print("Menu:")
print("P - Pizza Salgada: P - Pequena: R$30, M - Média: R$45, G - Grande: R$60")
print("D - Pizza Doce: P - Pequena: R$34, M - Média: R$48, G - Grande: R$66")

sabor = input("Escolha o sabor (PS para Pizza Salgada ou PD para Pizza Doce): ")

if sabor != "PS" and sabor != "PD":
    print("Sabor inválido. Tente novamente.")

tamanho = input("Escolha o tamanho (P para Pequena, M para Média, G para Grande): ")

if tamanho != "P" and tamanho != "M" and tamanho != "G":
    print("Tamanho inválido. Tente novamente.")

 if (sabor === "PS") {
      if (tamanho === "P") {
        total += 30;
      } else if (tamanho === "M") {
        total += 45;
      } else if (tamanho === "G") {
        total += 60;
      }
    } else if (sabor === "PD") {
      if (tamanho === "P") {
        total += 34;
      } else if (tamanho === "M") {
        total += 48;
      } else if (tamanho === "G") {
        total += 66;
      }
    }

def processar_pedido():
    continuar = True
    total = 0

    while continuar:
        sabor = input("Escolha o sabor (PS para Pizza Salgada ou PD para Pizza Doce): ")
        tamanho = input("Escolha o tamanho (P para Pequena, M para Média, G para Grande): ")

        if sabor == "PS":
            if tamanho == "P":
                total += 30
            elif tamanho == "M":
                total += 45
            elif tamanho == "G":
                total += 60
        elif sabor == "PD":
            if tamanho == "P":
                total += 34
            elif tamanho == "M":
                total += 48
            elif tamanho == "G":
                total += 66

        mais = input("Deseja pedir mais alguma coisa? (Sim/Não): ").lower()

        if mais != "sim":
            continuar = False

    print("Valor total do pedido: R$", total)

processar_pedido()

