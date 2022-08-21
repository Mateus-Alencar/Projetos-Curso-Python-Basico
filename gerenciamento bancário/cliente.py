class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return 'Nome:' + self.nome + '\n CPF:' + self.cpf + '\n Idade:' + str(self.idade)