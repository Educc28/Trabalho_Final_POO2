from animais.animais import Animais


class AnimalAve(Animais):  # Classe referente a animais aves
    def __init__(self, nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidade_ninho, codigo=None):
        super().__init__(nome, idade, dieta, sexo, porte, limpo, saude, tipo)
        self.tipo = 'ave'
        self.qualidade_ninho = qualidade_ninho

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
            qualidade_ninho: {self.qualidade_ninho}
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
            'qualidade_ninho': self.qualidade_ninho,
            'codigo': self.codigo,
        }
