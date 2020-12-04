###Cadastrar Prorpietario###
from datetime import date

from Classes_prova import Proprietario, Imovel, Inquilino


def cadastrar_proprietario():
    while True:
        nome = input("Informe o nome do proprietario: ")
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
    while True:
        codigo = input("Informe o codigo do imovel: ")
        cpf = input("Informe a matricula do professor: ")
        data = input("Informe a data de nascimento do professor (DD/MM/AAAA): ")
        tipo = input("Informe o tipo (CASA, APARTAMENTO): ")
        if tipo != 'CASA' and tipo != 'APARTAMENTO':
            print("tipo inválida!")
            continue
        endereco = input("Informe endereço: ")
        valor = input("Informe o valor do aluguel: ")
        status = input("Informe o Status de alugado (SIM, NAO): ")
        if status != 'SIM' and status != 'NAO':
            print("status inválida!")
        else:
            break
    Imovel(codigo, cpf, tipo, endereco, valor, status)
    print("imovel foi criado com sucesso!")

###Cadastrar Inquilino###
def cadastrar_inquilino():
    while True:
        nome = input("Informe o nome do inquilino: ")
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

def registrar_aluguel():
    while True:
        cpf = input("Informe o CPF do inquilino: ")
        codigo = input("Informe o código do imovel: ")
        data = input("Informe a data de inicio (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_inicio = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    #Inquilino(cpf, codigo,  data_de_inicio)
    print("Inquilino foi criado com sucesso!")

##Relátorio do Proprietário##
def relatorioProp(cpf):
    proprietario = Proprietario.find(int(cpf))
    if proprietario != None:
        nome_proprietario = proprietario.nome
        cpf_proprietario = proprietario.cpf
        nasc_proprietario = proprietario.data_nasc
    else:
        print("Esse proprietário não se encontra no banco de dados!")

##Relátorio do Inquilino##
def relatorioInqui(cpf):
    inquilino = Inquilino.find(int(cpf))
    if inquilino != None:
        nome_inquilino = inquilino.nome
        cpf_inquilino = inquilino.cpf
        nasc_inquilino = inquilino.data_nasc
    else:
        print("Esse inquilino não se encontra no banco de dados!")

##Relátorio de Imóveis##
def relatorioImov(cod_imovel):
    imovel = Imovel.find(int(cod_imovel))
    if imovel != None:
        cpf_proprietario = Proprietario.find(imovel.cpf).cpf_prop
        tipo_imovel = imovel.tipo
        endereco_imovel = imovel.endereco
        valor_aluguel_imovel = imovel.valor_aluguel
        status_alugado_imovel = imovel.status_alugado
    else:
        print("Esse imóvel não se encontra no banco de dados!")

