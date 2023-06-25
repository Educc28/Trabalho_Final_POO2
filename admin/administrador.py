from funcionarios.funcionario import Funcionario


class Administrador(Funcionario):  # Classe referente a todos os carros
    def __init__(self, nome, cpf, senha, tipo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.tipo = tipo

    def cadastra_animais(self):  # Função que retorna o código de uma roupa
        pass

    def deleta_animais(self):
        pass

    def cadastra_funcionario(self):
        pass

    def deleta_funcionario(self):
        pass
