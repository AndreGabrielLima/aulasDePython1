class PessoaFisica():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def impostoderendaPF(self):
        irrf = self.salario * 0.03
        print(f'{self.nome} seu salário é R$ {self.salario} e seu IRRF é R$ {irrf}')

class PessoaJuridica():
    def __init__(self, razaoSocial, faturamento):
        self.razaoSocial = razaoSocial
        self.faturamento = faturamento

    def impostoderendaPF(self):
        irrf = self.faturamento * 0.01
        print(f'{self.razaoSocial} seu salário é R$ {self.faturamento} e seu IRRF é R$ {irrf}')

while True:
    print('Escolha a opção 0 - Pessoa Física | 1 - Pessoa Jurídica: ')
    conf = int(input())

    if conf == 0:
        nome = input('Digite seu nome: ')
        salario = float(input('Digite seu salário: '))
        in1 = PessoaFisica(nome, salario)
        in1.impostoderendaPF()

    elif conf == 1:
        razao = input('Digite a razão social da empresa: ')
        faturamento = float(input('Digite o faturamento da empresa: '))
        in2 = PessoaJuridica(razao, faturamento)
        in2.impostoderendaPF()

    print('')
    print('0 - CONTINUAR | 1 - SAIR')
    if (int(input())) == 1:
        break