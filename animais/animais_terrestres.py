from animais.animais import Animais


class AnimalTerrestre(Animais):  # Classe referente a calças
    def __init__(self, nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidade_solo, codigo=None):
        super().__init__(nome, idade, dieta, sexo, porte, limpo, saude, tipo)
        self.tipo = 'terrestre'
        self.qualidade_solo = qualidade_solo
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
            qualidade_solo: {self.qualidade_solo}
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
            'qualidade_solo': self.qualidade_solo,
            'codigo': self.codigo,
        }
