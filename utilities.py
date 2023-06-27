import json
from uuid import UUID
from animais.animais_terrestres import AnimalTerrestre
from animais.animais_aves import AnimalAve
from animais.animais_aquaticos import AnimalAquatico


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


# Função que escreve uma roupa no jscon
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


# Função que escreve uma roupa no jscon
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


# Função que escreve uma roupa no jscon
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
