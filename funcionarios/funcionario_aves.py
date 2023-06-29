from funcionarios.funcionario import Funcionario


class FuncionarioAve(Funcionario):  # Classe referente a funcionarios aves
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'ave'

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
