# Dia 8 - Cadastro de Contatos

contatos = {}

while True:
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"Contato {nome} adicionado com sucesso!")

    elif opcao == "2":
        if contatos:
            print("\n=== Contatos ===")
            for nome, info in contatos.items():
                print(f"Nome: {nome}")
                print(f" Telefone: {info['telefone']}")
                print(f" E-mail: {info['email']}")
                print("-" * 20)
        else:
            print("Nenhum contato cadastrado.")

    elif opcao == "0":
        print("Encerrando programa. Até logo!")
        break

    else:
        print("Opção inválida.")
