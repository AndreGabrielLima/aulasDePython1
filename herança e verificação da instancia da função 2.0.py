class fuctura():
    def __init__(self, nome, matricula, telefone, email, funcionarios):
        self.aluno = nome
        self.matriculas = matricula
        self.telefone = telefone
        self.email = email
        self.funcionarios = funcionarios
        self.verificação = self.__class__.__name__

    def apresentação(self):
        print('Bem vindo a Fuctura! Aluno da filial: '.format(self.verificação))

class fuctura1(fuctura):
    def agendar_aula(self):
        print('Agendando aula para as turmas da Fuctura1')

    def apresentação(self):
        soma = 1 + 1
        print(soma)

class fuctura2(fuctura):
    def agendar_aula(self):
        print('Agendando aula para as turmas da Fuctura2')

aluno1 = fuctura('André', None, None, None, None)
print(aluno1.aluno)
aluno1.apresentação()
aluno2 = fuctura1('Bianca', None, None, None, None)
print(aluno2.aluno)
aluno2.apresentação()