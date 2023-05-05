class Fuctura():
    def __init__(self, nome, matricula, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email

nome = input('Digite o nome do aluno: ')
matricula = input('Digite a matricula do aluno: ')
telefone = input('Digite o telefone do aluno: ')
email = input('Digite o email do aluno: ')

aluno1 = Fuctura(nome, matricula, telefone, email)
print(aluno1.nome, aluno1.matricula, aluno1.telefone, aluno1.email)