from funcionario import Funcionario


class FuncionarioTerrestre(Funcionario):  # Classe referente a calças
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'terrestre'

    def limpa_terrestre(self):
        pass

    def ajusta_solo(self):
        pass

    def alimenta_terrestre(self):
        pass

    def ver_terrestres(self):
        pass

    def to_string(self):
        return f'''
            nome: {self.nome}
            cpf: {self.cpf} 
            senha: {self.senha}
            tipo: {self.tipo}
        '''

    def toJSON(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha,
            'tipo': self.tipo,
        }
