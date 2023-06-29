from funcionarios.funcionario import Funcionario


class Administrador(Funcionario):  # Classe referente a todos os administradores
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'administrador'

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
