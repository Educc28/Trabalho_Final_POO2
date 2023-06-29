class ultimaConsulta():  # Classe referente a todas as roupas
    def __init__(self, nome, data, vetNome, cpfVet, remedio):
        self.nome = nome
        self.data = data
        self.vetNome = vetNome
        self.cpfVet = cpfVet
        self.remedio = remedio

    def to_string():  # Faz overwrite dos metodos
        pass

    def toJSONConsulta(self):

        return {
            'nome': self.nome,
            'data': self.data,
            'nomeVet': self.vetNome,
            'cpf': self.cpfVet,
            'remedio': self.remedio,
        }
