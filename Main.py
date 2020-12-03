import Classes
import Functions

try:
    open('Alunos.xlsx', 'r')
except IOError:
    print('Criando novos arquivos...')
    Functions.criarDataFrame()

Functions.getDataFramefromExcel()

def main():
    while True:
        try:
            print("----Menu----\n1---Cadastro Professor\n2---Cadastrar Aluno\n3---Cadastrar Disciplina\n4---Cadastrar nota\n5---Relátorio de Notas\n6---Sair")
            opcao = int(input("Informe uma opção: "))
        except ValueError:
            print("Selecione uma opção válida!")
            continue
        if opcao == 1:
            Functions.cadastrar_professor()
            print()
        if opcao == 2:
            Functions.cadastrar_aluno()
            print()
        if opcao == 3:
            Functions.cadastrar_disciplina()
            print()
        if opcao == 4:
            Functions.cadastrar_nota()
            print()
        if opcao == 5:
            cod_disciplina = input("Informe o código da disciplina: ")
            Functions.relatorio(cod_disciplina)
        if opcao == 6:
            Functions.salvarDataframe()
            break
main()