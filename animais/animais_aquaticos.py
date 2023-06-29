from animais.animais import Animais


class AnimalAquatico(Animais):  # Classe referente a animais aquaticos
    def __init__(self, nome, idade, dieta, sexo, porte, limpo, saude, tipo, temperatura_atual, codigo=None):
        super().__init__(nome, idade, dieta, sexo, porte, limpo, saude, tipo)
        self.tipo = 'aquatico'
        self.temperatura_atual = temperatura_atual

        if codigo:
            self.codigo = codigo
        else:
            self.codigo = super().getCodigo()

    def to_string(self):
        return f'''
            nome: {self.nome}
            idade: {self.idade} 
            dieta: {self.dieta}
            sexo: {self.sexo}
            porte: {self.porte}
            limpo: {self.limpo}
            saude: {self.saude}
            tipo: {self.tipo}
            temperatura_atual: {self.temperatura_atual}
            codigo: {self.codigo}
        '''

    def toJSON(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'dieta': self.dieta,
            'sexo': self.sexo,
            'porte': self.porte,
            'limpo': self.limpo,
            'saude': self.saude,
            'tipo': self.tipo,
            'temperatura_atual': self.temperatura_atual,
            'codigo': self.codigo,
        }
