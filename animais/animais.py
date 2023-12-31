import uuid


class Animais():  # Classe referente a todas os animais
    def __init__(self, nome, idade, dieta, sexo, porte, limpo, saude, tipo):
        self.nome = nome
        self.idade = idade
        self.dieta = dieta
        self.sexo = sexo
        self.porte = porte
        self.limpo = limpo
        self.saude = saude
        self.tipo = tipo
        self.codigo = uuid.uuid4()

    def getCodigo(self):  # Função que retorna o código de um animal
        return self.codigo

    def to_string():  # Faz overwrite dos metodos
        pass
