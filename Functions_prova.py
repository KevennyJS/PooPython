###Cadastrar Prorpietario###
def cadastrar_proprietario():
    nome = input("Informe o nome do proprietario: ")
    while True:
        cpf = input("Informe a matricula do proprietario: ")
        data = input("Informe a data de nascimento do proprietario (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_nascimento = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    Proprietario(nome, cpf, data_de_nascimento)
    print("Proprietario foi criado com sucesso!")

###Cadastrar Imovel###
def cadastrar_imovel():
    codigo = input("Informe o codigo do imovel: ")
    while True:
        cpf = input("Informe a matricula do professor: ")
        data = input("Informe a data de nascimento do professor (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_nascimento = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    Imovel(nome, cpf, data_de_nascimento)
    print("Proprietario foi criado com sucesso!")

###Cadastrar Prorpietario###
def cadastrar_inquilino():
    nome = input("Informe o nome do inquilino: ")
    while True:
        cpf = input("Informe a matricula do inquilino: ")
        data = input("Informe a data de nascimento do inquilino (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_nascimento = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    Inquilino(nome, cpf, data_de_nascimento)
    print("Inquilino foi criado com sucesso!")
