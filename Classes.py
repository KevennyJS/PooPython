class Professor:
    professores = []
    
    def __init__(self, nome, matricula, data_nasc):
        self.nome = nome
        self.matricula = matricula
        self.data_nasc = data_nasc
        if Professor.find(matricula) == None:
            Professor.professores.append(self)
    
    @staticmethod
    def find(matricula):
        for p in Professor.professores:
            if p.matricula == matricula:
                return p
        return None

class Aluno:
    alunos = []
    
    def __init__(self, nome, matricula, data_nasc):
        self.nome = nome
        self.matricula = matricula
        self.data_nasc = data_nasc
        if Aluno.find(matricula) == None:
            Aluno.alunos.append(self)
    
    @staticmethod
    def find(matricula):
        for p in Aluno.alunos:
            if p.matricula == matricula:
                return p
        return None

class Disciplina:
    disciplinas = []
    
    def __init__(self, cod, nome, matricula_prof):
        self.cod = cod
        self.nome = nome
        self.matricula_prof = matricula_prof
        if Disciplina.find(cod) == None:
            Disciplina.disciplinas.append(self)
   
    @staticmethod
    def find(cod):
        for p in Disciplina.disciplinas:
            if p.cod == cod:
                return p
        return None

class Nota:
    notas = []

    def __init__(self, cod_disciplina, matricula_aluno, n1, n2):
        self.cod_disciplina = int(cod_disciplina)
        self.matricula_aluno = matricula_aluno
        self.n1 = n1
        self.n2 = n2
        if Nota.find(cod_disciplina, matricula_aluno) == None:
            Nota.notas.append(self)
    
    @staticmethod
    def find(cod_disciplina, matricula_aluno):
        for p in Nota.notas:
            if p.cod_disciplina == cod_disciplina and p.matricula_aluno == matricula_aluno:
                return p
        return None

