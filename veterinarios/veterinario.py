from funcionarios.funcionario import Funcionario


class Veterinario(Funcionario):  # Classe referente a todos os carros
    def __init__(self, nome, cpf, senha, tipo):
        super().__init__(nome, cpf, senha, tipo)
        self.tipo = 'veterinario'

    def pega_ultima_consulta(self):  # Função que retorna o código de uma roupa
        pass

    def cuida_animais(self):
        pass

    def alimenta_terrestre(self):
        pass

    def alimenta_ave(self):
        pass

    def alimenta_aquatico(self):
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
