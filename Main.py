import Functions
import Classes

try:
    open('Alunos.xlsx', 'r')
except IOError:
    print('Criando novos arquivos...')
    Functions.criarDataFrame()

Functions.getDataFramefromExcel()


def main():
    while True:
        try:
            print(
                "----Menu----\n"
                "1---Cadastrar Proprietário\n"
                "2---Cadastrar Imóvel\n"
                "3---Cadastrar Inquilino\n"
                "4---Registrar Aluguel\n"
                "5---Finalizar Aluguel\n"
                "6---Relatório de Proprietários\n"
                "7---Relatório de Imóveis\n"
                "8---Relatório de Inquilinos\n"
                "9---Relatório de Aluguéis\n"
                "10---Relatório de Comissões\n"

                "0---Sair")

            opcao = int(input("Informe uma opção: "))
        except ValueError:
            print("Selecione uma opção válida!")
            continue
        if opcao == 1:
            Functions.cadastrar_professor()
            print()
        elif opcao == 2:
            Functions.cadastrar_aluno()
            print()
        elif opcao == 3:
            Functions.cadastrar_disciplina()
            print()
        elif opcao == 4:
            Functions.cadastrar_nota()
            print()
        elif opcao == 5:
            cod_disciplina = input("Informe o código da disciplina: ")
            Functions.relatorio(cod_disciplina)
        elif opcao == 6:
            Functions.cadastrar_nota()
            print()
        elif opcao == 7:
            Functions.cadastrar_nota()
            print()
        elif opcao == 8:
            Functions.cadastrar_nota()
            print()
        elif opcao == 9:
            Functions.cadastrar_nota()
            print()
        elif opcao == 10:
            Functions.cadastrar_nota()
            print()
        elif opcao == 0:
            Functions.salvarDataframe()
            break


main()
