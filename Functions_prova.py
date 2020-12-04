import pandas as pd
from datetime import date

from Classes_prova import *

###Cadastrar Prorpietario###
def cadastrar_proprietario():
    while True:
        nome = input("Informe o nome do proprietario: ")
        cpf = input("Informe a CPF do proprietario: ")
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
        cpf = input("Informe a CPF do professor: ")
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
        cpf = input("Informe a CPF do inquilino: ")
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
def relatorioInqui():
    for dado in Inquilino.inquilinos:
        inquilino = Inquilino.find(dado.cpf)
        nome_do_inquilino = inquilino.nome
        cpf_inquilino = inquilino.cpf
        nasc_inquilino = inquilino.data_nasc
        print(f"Inquilino: {nome_do_inquilino} CPF: {cpf_inquilino} Data de nascimento: {nasc_inquilino}")

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

def criarDataFrame():
    proprietario_dataframe = pd.DataFrame(columns=['Nome', 'Cpf', 'Data de Nascimento'])  # Dataframe Proprietario
    imovel_dataframe = pd.DataFrame(columns=['Codigo', 'Cpf do Proprietario', 'Tipo', 'Endereco', 'Valor Aluguel', 'Status Alugado'])  # Dataframe Imovel
    inquilino_dataframe = pd.DataFrame(columns=['Nome', 'Cpf', 'Data de Nascimento'])  # Dataframe Inquilino
    proprietario_dataframe.to_excel('Proprietarios.xlsx', 'Plan1', index=False)
    imovel_dataframe.to_excel('Imoveis.xlsx', 'Plan1', index=False)
    inquilino_dataframe.to_excel('Inquilinos.xlsx', 'Plan1', index=False)

def salvarDataframe():
    # Salvar proprietario no excel
    i = 0
    dados = pd.read_excel('Proprietarios.xlsx')
    for proprietario in Proprietario.proprietarios:
        linha = [proprietario.nome, proprietario.cpf, proprietario.data_nasc]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Proprietarios.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()

    # Salvar imovel no excel
    i = 0
    dados = pd.read_excel('Imoveis.xlsx')
    for imovel in Imovel.imoveis:
        linha = [imovel.cod, imovel.cpf_prop, imovel.tipo, imovel.endereco, imovel.valor_aluguel, imovel.status_alugado]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Imoveis.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()

    # Salvar inquilino no excel
    i = 0
    dados = pd.read_excel('Inquilinos.xlsx')
    for inquilino in Inquilino.inquilinos:
        linha = [inquilino.nome, inquilino.cpf, inquilino.data_nasc]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Inquilinos.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()

def getDataFramefromExcel():
    # Proprietário
    dados = pd.read_excel('Proprietarios.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        cpf = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        Proprietario(nome, cpf, data_nascimento)
    # Imovel
    dados = pd.read_excel('Imoveis.xlsx')
    for i in range(len(dados)):
        codigo = dados.loc[i][0]
        cpf_proprietario = dados.loc[i][1]
        tipo = dados.loc[i][2]
        endereco = dados.loc[i][3]
        valor_aluguel = dados.loc[i][4]
        status_alugado = dados.loc[i][5]
        Proprietario(codigo, cpf_proprietario, tipo, endereco, valor_aluguel, status_alugado)
    # Inquilino
    dados = pd.read_excel('Inquilinos.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        cpf = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        Inquilino(nome, cpf, data_nascimento)