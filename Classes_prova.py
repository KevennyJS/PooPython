class Proprietario:
    proprietarios = []

    def __init__(self, nome, cpf, data_nasc):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        if Proprietario.find(cpf) == None:
            Proprietario.proprietarios.append(self)

    @staticmethod
    def find(cpf):
        for p in Proprietario.proprietarios:
            if p.cpf == cpf:
                return p
        return None

class Inquilino:
    inquilinos = []

    def __init__(self, nome, cpf, data_nasc):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        if Inquilino.find(cpf) == None:
            Inquilino.inquilinos.append(self)

    @staticmethod
    def find(cpf):
        for p in Inquilino.inquilinos:
            if p.cpf == cpf:
                return p
        return None

class Imovel:
    imoveis = []

    def __init__(self, cod, cpf_prop, tipo, endereco, valor_aluguel, status_alugado):
        self.cod = cod
        self.cpf_prop = cpf_prop
        self.tipo = tipo
        self.endereco = endereco
        self.valor_aluguel = valor_aluguel
        self.status_alugado = status_alugado
        if Imovel.find(cod) == None:
            Imovel.imoveis.append(self)

    @staticmethod
    def find(cod):
        for p in Imovel.imoveis:
            if p.cod == cod:
                return p
        return None

class Aluguel:
    alugueis = []

    def __init__(self, cpf_inquilino, cod_imovel, data_inicio, data_fim):
        self.cpf_inquilino = cpf_inquilino
        self.cod_imovel = cod_imovel
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        if Aluguel.find(cod_imovel) == None:
            Aluguel.alugueis.append(self)

    @staticmethod
    def find(cod):
        for p in Aluguel.alugueis:
            if p.cod_imovel == cod:
                return p
        return None