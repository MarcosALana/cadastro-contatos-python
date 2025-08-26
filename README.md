# Cadastro de Contatos em Python

Programa em Python que simula uma **agenda de contatos**, armazenando dados em um **dicionário**.  
Cada contato possui **nome, telefone e e-mail**, permitindo adicionar e listar informações.

## 🚀 Código principal
```python
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


O que foi aprendido
Criação e manipulação de dicionários em Python.
Uso de pares chave → valor para organizar dados.
Estruturas aninhadas (dicionário dentro de outro dicionário).
Iteração em dicionários com .items().
Integração de conceitos: entrada do usuário + estrutura de dados.

💭 Comentário pessoal

Gostei muito de aprender dicionários, pois percebi como eles ajudam a organizar dados de forma estruturada.
A agenda de contatos já começa a se parecer com um sistema real, e vejo como isso pode evoluir para projetos maiores, como cadastros de alunos ou clientes.
