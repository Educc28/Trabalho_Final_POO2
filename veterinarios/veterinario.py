from funcionarios.funcionario import Funcionario


class Veterinario(Funcionario):  # Classe referente a todos os carros
    def __init__(self, nome, cpf, senha, tipo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.tipo = tipo

    def pega_ultima_consulta(self):  # Função que retorna o código de uma roupa
        pass

    def cuida_animais(self):
        pass

    def alimenta_terrestre(self):
        pass

    def alimenta_ave(self):
        pass

    def alimenta_aquatico(self):
        pass
