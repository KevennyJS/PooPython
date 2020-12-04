import Functions
import Classes
import Functions_prova

try:
    open('Proprietarios.xlsx', 'r')
except IOError:
    print('Criando novos arquivos...')
    Functions_prova.criarDataFrame()

Functions_prova.getDataFramefromExcel()


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
        if opcao == 1: #OK
            Functions_prova.cadastrar_proprietario()
            print()
        elif opcao == 2: #OK
            Functions_prova.cadastrar_imovel()
            print()
        elif opcao == 3: #OK
            Functions_prova.cadastrar_inquilino()
            print()
        elif opcao == 4:
            Functions.cadastrar_nota()
            print()
        elif opcao == 5:
            print(6)
        elif opcao == 6:
            Functions_prova.relatorioProp()
            print()
        elif opcao == 7:
            Functions_prova.relatorioImov()
            print()
        elif opcao == 8:
            Functions_prova.relatorioInqui()
            print()
        elif opcao == 9:
            Functions.cadastrar_nota()
            print()
        elif opcao == 10:
            Functions.cadastrar_nota()
            print()
        elif opcao == 0:
            Functions_prova.salvarDataframe()            #Functions.salvarDataframe()
            break


main()
