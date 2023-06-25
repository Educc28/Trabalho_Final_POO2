from funcionario import Funcionario


class FuncionarioTerrestre(Funcionario):  # Classe referente a calças
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'ave'

    def limpa_ave(self):
        pass

    def ajusta_ninho(self):
        pass

    def alimenta_ave(self):
        pass

    def ver_aves(self):
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
