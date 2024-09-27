print("Bem vindos a lista de contatos do [Seu Nome Completo]")

lista_contatos = []
id_global = [Seu RU aqui]  

def cadastrar_contato(id):
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }
    lista_contatos.append(contato.copy())

def consultar_contatos():
    while True:
        opcao = input("Qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Atividade / 4. Retornar ao menu): ")
        
        if opcao == '1':
            for contato in lista_contatos:
                print(contato)
        elif opcao == '2':
            id_consulta = int(input("Informe o ID do contato: "))
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(contato)
                    break
            else:
                print("Contato não encontrado.")
        elif opcao == '3':
            atividade_consulta = input("Informe a atividade: ")
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(contato)
            else:
                print("Nenhum contato encontrado com essa atividade.")
        elif opcao == '4':
            return
        else:
            print("Opção inválida")

def remover_contato():
    while True:
        id_remover = int(input("Informe o ID do contato a ser removido: "))
        for contato in lista_contatos:
            if contato['id'] == id_remover:
                lista_contatos.remove(contato)
                print("Contato removido com sucesso.")
                return
        print("Id inválido")

while True:
    opcao = input("Qual opção deseja (1. Cadastrar Contato / 2. Consultar Contato / 3. Remover Contato / 4. Encerrar Programa): ")
    
    if opcao == '1':
        id_global[0] += 1
        cadastrar_contato(id_global[0])
    elif opcao == '2':
        consultar_contatos()
    elif opcao == '3':
        remover_contato()
    elif opcao == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")

cadastrar_contato(1)  # Cadastro meu contato
cadastrar_contato(2)  # Cadastro contato 2
cadastrar_contato(3)  # Cadastro contato 3

print("Consulta todos os contatos:")
consultar_contatos()

print("Consulta por ID do contato 1:")
for contato in lista_contatos:
    if contato['id'] == 1:
        print(contato)

print("Consulta por atividade (mesma atividade para 2 contatos):")
for contato in lista_contatos:
    if contato['atividade'] == 'estudante':
        print(contato)

print("Removendo contato ID 1:")
remover_contato()
print("Consulta todos os contatos após remoção:")
consultar_contatos()
