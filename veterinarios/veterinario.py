from funcionarios.funcionario import Funcionario


class Veterinario(Funcionario):  # Classe referente a todos os veterinarios
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'veterinario'

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
