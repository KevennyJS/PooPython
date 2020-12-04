import pandas as pd
from datetime import date
from Classes import *


###Cadastro do Professor###
def cadastrar_professor():
    nome = input("Informe o nome do professor: ")
    while True:
        matricula = input("Informe a matricula do professor: ")
        data = input("Informe a data de nascimento do professor (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_nascimento = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    Professor(nome, matricula, data_de_nascimento)
    print("Professor foi criado com sucesso!")


###Cadastro do Aluno###
def cadastrar_aluno():
    nome = input("Informe o nome do Aluno: ")
    while True:
        matricula = input("Informe a matricula do aluno: ")
        data = input("Informe a data de nascimento do aluno (DD/MM/AAAA): ")
        data = data.split('/')
        if data[0].isnumeric() and data[1].isnumeric() and data[2].isnumeric():
            data_de_nascimento = date(int(data[2]), int(data[1]), int(data[0]))
            break
        else:
            print("Data inválida!")
            continue
    Aluno(nome, matricula, data_de_nascimento)
    print("Aluno foi criado com sucesso!")


###Cadastro de Disciplinas###
def cadastrar_disciplina():
    cod = input("Informe o código da disciplina: ")
    nome = input("Informe o nome da disciplina: ")
    matricula_prof = input("Informe a matricula do professor que leciona a disciplina: ")
    Disciplina(cod, nome, matricula_prof)
    print("Disciplina foi criado com sucesso!")


###Cadastrar Nota###
def cadastrar_nota():
    cod_disciplina = input("Informe o código da disciplina: ")
    matricula_aluno = input("Informe a matricula do aluno: ")
    n1 = int(input("Informe a primeira nota do aluno: "))
    n2 = int(input("Informe a segunda nota do aluno: "))
    Nota(cod_disciplina, matricula_aluno, n1, n2)
    print("As notas foram adicionadas com sucesso!")


##Relátorio
def relatorio(cod_disciplina):
    disciplina = Disciplina.find(int(cod_disciplina))
    if disciplina != None:
        nome_disciplina = disciplina.nome
        nome_prof = Professor.find(disciplina.matricula_prof).nome
        print(f"Nome da disciplina: {nome_disciplina}\nNome do professor que leciona: {nome_prof} ")
        for nota in Nota.notas:
            aluno = Aluno.find(nota.matricula_aluno)
            nome_do_aluno = aluno.nome
            print(f"Aluno: {nome_do_aluno} Media: {(int(nota.n1) + int(nota.n2)) / 2:.2f}")
    else:
        print("Essa disciplina não se encontra no banco de dados!")


def criarDataFrame():
    professores_dataframe = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])  # Dataframe Professor
    alunos_dataframe = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])  # Dataframe Aluno
    disciplinas_dataframe = pd.DataFrame(columns=['Codigo', 'Nome', 'Matricula do professor'])  # Dataframe Disciplinas
    notas_dataframe = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])  # Dataframe Notas
    professores_dataframe.to_excel('Professores.xlsx', 'Plan1', index=False)
    alunos_dataframe.to_excel('Alunos.xlsx', 'Plan1', index=False)
    disciplinas_dataframe.to_excel('Disciplinas.xlsx', 'Plan1', index=False)
    notas_dataframe.to_excel('Notas.xlsx', 'Plan1', index=False)


def salvarDataframe():
    # Salvar professor no excel
    i = 0
    dados = pd.read_excel('Professores.xlsx')
    for professor in Professor.professores:
        linha = [professor.nome, professor.matricula, professor.data_nasc]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Professores.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()
    # Salvar aluno no excel
    i = 0
    dados = pd.read_excel('Alunos.xlsx')
    for aluno in Aluno.alunos:
        linha = [aluno.nome, aluno.matricula, aluno.data_nasc]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Alunos.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()
    # Salvar disciplinas
    i = 0
    dados = pd.read_excel('Disciplinas.xlsx')
    for disciplina in Disciplina.disciplinas:
        linha = [disciplina.cod, disciplina.nome, disciplina.matricula_prof]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Disciplinas.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()
    # Salvar Notas
    i = 0
    dados = pd.read_excel('Notas.xlsx')
    for nota in Nota.notas:
        linha = [nota.cod_disciplina, nota.matricula_aluno, nota.n1, nota.n2]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('Notas.xlsx')
    dados.to_excel(excel_writer, 'Plan1', index=False)
    excel_writer.save()


def getDataFramefromExcel():
    # Professor
    dados = pd.read_excel('Professores.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        Professor(nome, matricula, data_nascimento)
    # Aluno
    dados = pd.read_excel('Alunos.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        Aluno(nome, matricula, data_nascimento)
    # Disciplina
    dados = pd.read_excel('Disciplinas.xlsx')
    for i in range(len(dados)):
        codigo = dados.loc[i][0]
        nome = dados.loc[i][1]
        matricula_professor = dados.loc[i][2]
        Disciplina(codigo, nome, matricula_professor)
    # Notas
    dados = pd.read_excel('Notas.xlsx')
    for i in range(len(dados)):
        codigo_disciplina = dados.loc[i][0]
        matricula_aluno = dados.loc[i][1]
        nota1 = dados.loc[i][2]
        nota2 = dados.loc[i][3]
        Nota(codigo_disciplina, matricula_aluno, nota1, nota2)
