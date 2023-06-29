from funcionarios.funcionario import Funcionario


# Classe referente a funcionarios terrestres
class FuncionarioTerrestre(Funcionario):
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'terrestre'

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
