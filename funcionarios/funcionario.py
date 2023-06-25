class Funcionario():  # Classe referente a todos os carros
    def __init__(self, nome, cpf, senha, tipo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.tipo = tipo

    def get_tipo(self):  # Função que retorna o código de uma roupa
        return self.tipo

    def ver_animais(self):
        pass
