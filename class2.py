class Fuctura():
    def __init__(self, nome, matricula, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email

aluno1 = Fuctura('André', '123', '987648036', 'andregabriel_lima@hotmail.com.br')
print(aluno1.nome)
aluno2 = Fuctura('Bianca', '124', '997330372', 'biancamarques@gmail')
print(aluno2.nome)
