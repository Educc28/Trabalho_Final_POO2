class Funcionario():  # Classe referente a todos os funcionarios
    def __init__(self, nome, cpf, senha, tipo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.tipo = tipo

    def get_tipo(self):  # Função que retorna o tipo de um funcionario
        return self.tipo
