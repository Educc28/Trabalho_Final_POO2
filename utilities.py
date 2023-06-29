import json
from uuid import UUID
from animais.animais_terrestres import AnimalTerrestre
from animais.animais_aves import AnimalAve
from animais.animais_aquaticos import AnimalAquatico
from funcionarios.funcionario_terrestres import FuncionarioTerrestre
from funcionarios.funcionario_aves import FuncionarioAve
from funcionarios.funcionario_aquaticos import FuncionarioAquatico
from admin.administrador import Administrador
from veterinarios.veterinario import Veterinario
from veterinarios.ultimaConsulta import ultimaConsulta


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


# Função que escreve um animal terrestre no json
def writeToFileAnimaisTerrestres(animais):
    todosAnimais = []
    animais_json = []

    with open("animais.json", "r") as r:
        todosAnimais = json.load(r)

    with open("animais.json", "w+") as f:
        for animal in animais:
            animais_json.append(AnimalTerrestre.toJSON(animal))
        todosAnimais.append(animais_json[0])
        json.dump(todosAnimais, f, cls=UUIDEncoder)


# Função que escreve um animal ave no json
def writeToFileAnimaisAves(animais):
    todosAnimais = []
    animais_json = []

    with open("animais.json", "r") as r:
        todosAnimais = json.load(r)

    with open("animais.json", "w+") as f:
        for animal in animais:
            animais_json.append(AnimalAve.toJSON(animal))
        todosAnimais.append(animais_json[0])
        json.dump(todosAnimais, f, cls=UUIDEncoder)


# Função que escreve um animal aquatico no json
def writeToFileAnimaisAquaticos(animais):
    todosAnimais = []
    animais_json = []

    with open("animais.json", "r") as r:
        todosAnimais = json.load(r)

    with open("animais.json", "w+") as f:
        for animal in animais:
            animais_json.append(AnimalAquatico.toJSON(animal))
        todosAnimais.append(animais_json[0])
        json.dump(todosAnimais, f, cls=UUIDEncoder)


# Função que escreve um funcionario terrestre no json
def writeToFileFuncionarioTerrestre(usuarios):
    todosFuncionarios = []
    funcionarios_json = []

    with open("usuarios.json", "r") as r:
        todosFuncionarios = json.load(r)

    with open("usuarios.json", "w+") as f:
        for funcionario in usuarios:
            funcionarios_json.append(FuncionarioTerrestre.toJSON(funcionario))
        todosFuncionarios.append(funcionarios_json[0])
        json.dump(todosFuncionarios, f, cls=UUIDEncoder)


# Função que escreve um funcionario ave no json
def writeToFileFuncionarioAve(usuarios):
    todosFuncionarios = []
    funcionarios_json = []

    with open("usuarios.json", "r") as r:
        todosFuncionarios = json.load(r)

    with open("usuarios.json", "w+") as f:
        for funcionario in usuarios:
            funcionarios_json.append(FuncionarioAve.toJSON(funcionario))
        todosFuncionarios.append(funcionarios_json[0])
        json.dump(todosFuncionarios, f, cls=UUIDEncoder)


# Função que escreve um funcionario aquatico no json
def writeToFileFuncionarioAquatico(usuarios):
    todosFuncionarios = []
    funcionarios_json = []

    with open("usuarios.json", "r") as r:
        todosFuncionarios = json.load(r)

    with open("usuarios.json", "w+") as f:
        for funcionario in usuarios:
            funcionarios_json.append(FuncionarioAquatico.toJSON(funcionario))
        todosFuncionarios.append(funcionarios_json[0])
        json.dump(todosFuncionarios, f, cls=UUIDEncoder)

# Função que escreve um funcionario administrador no json


def writeToFileFuncionarioAdmin(usuarios):
    todosFuncionarios = []
    funcionarios_json = []

    with open("usuarios.json", "r") as r:
        todosFuncionarios = json.load(r)

    with open("usuarios.json", "w+") as f:
        for funcionario in usuarios:
            funcionarios_json.append(Administrador.toJSON(funcionario))
        todosFuncionarios.append(funcionarios_json[0])
        json.dump(todosFuncionarios, f, cls=UUIDEncoder)


# Função que escreve um veterinario no json
def writeToFileFuncionarioVeterinario(usuarios):
    todosFuncionarios = []
    funcionarios_json = []

    with open("usuarios.json", "r") as r:
        todosFuncionarios = json.load(r)

    with open("usuarios.json", "w+") as f:
        for funcionario in usuarios:
            funcionarios_json.append(Veterinario.toJSON(funcionario))
        todosFuncionarios.append(funcionarios_json[0])
        json.dump(todosFuncionarios, f, cls=UUIDEncoder)


# Função que escreve a ultima consulta no json

def writeToFileUltimaConsulta(consultas, todasConsultas):
    consultas_json = []

    with open("ultimaConsulta.json", "w+") as f:
        for consulta in consultas:
            consultas_json.append(ultimaConsulta.toJSONConsulta(consulta))
        todasConsultas.append(consultas_json[0])
        json.dump(todasConsultas, f, cls=UUIDEncoder)
