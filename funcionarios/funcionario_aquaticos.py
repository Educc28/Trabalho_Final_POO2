from funcionarios.funcionario import Funcionario


class FuncionarioAquatico(Funcionario):  # Classe referente a calças
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'aquatico'

    def limpa_aquatico(self):
        pass

    def ajusta_temperatura(self):
        pass

    def alimenta_aquatico(self):
        pass

    def ver_aquaticos(self):
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
