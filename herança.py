class fuctura():

    def __init__(self, nome, matricula, telefone, email, funcionarios):
        self.aluno = nome
        self.matriculas = matricula
        self.telefone = telefone
        self.email = email
        self.funcionarios = funcionarios

    def apresentação(self):
        print('Bem vindo a Fuctura !')

class fuctura1(fuctura):
    pass

class fuctura2(fuctura):
    pass

aluno1 = fuctura('André', None, None, None, None)
print(aluno1.aluno)
aluno1.apresentação()
aluno2 = fuctura1('Bianca', None, None, None, None)
print(aluno2.aluno)
aluno2.apresentação()