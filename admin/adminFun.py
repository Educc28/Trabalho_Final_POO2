import json
from tkinter import *
from animais.animais_terrestres import AnimalTerrestre
from animais.animais_aquaticos import AnimalAquatico
from animais.animais_aves import AnimalAve
from utilities import *
# from utilities import *
# from carro import Carro

global dadosAnimais
global dadosUsuarios
dadosAnimais = []
dadosUsuarios = []


class AdminFun():  # Classe referente as funções do programa
    def __init__(self):
        self.Animais = []
        self.Usuarios = []

    def lerJsonAnimais(self):  # Lê todos os carros do JSON
        global dadosAnimais
        with open("animais.json", "r") as f:
            dadosAnimais = json.load(f)
        f.close

    def RemoveTodosAnimais(self):  # Remove os Animais do Treeview
        for item in self.trv.get_children():
            self.trv.delete(item)

    def loadTrvAnimais(self):  # Carrega dadosAnimais para o Treeview
        global dadosAnimais

        self.RemoveTodosAnimais()

        rowIndex = 1

        for k in dadosAnimais:
            nome = k["nome"]
            idade = k["idade"]
            dieta = k["dieta"]
            sexo = k["sexo"]
            porte = k["porte"]
            limpo = k["limpo"]
            saude = k["saude"]
            tipo = k["tipo"]

            if tipo == "terrestre":
                especial = k["qualidade_solo"]
            elif tipo == "ave":
                especial = k["qualidade_ninho"]
            else:
                especial = k["temperatura_atual"]

            codigo = k["codigo"]

            self.trv.insert('', index='end', iid=rowIndex, text="",
                            values=(nome, idade, dieta, sexo, porte, limpo, saude, tipo, especial, codigo))
            rowIndex = rowIndex+1

    def createAnimal(self):  # Cria um carro no JSON
        self.animais = []
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        dieta = self.dieta_entry.get()
        sexo = self.sexo_entry.get()
        porte = self.porte_entry.get()
        limpo = self.limpo_entry.get()
        saude = self.saude_entry.get()
        tipo = self.tipo_entry.get()
        qualidadeTemperatura = self.qualidadeTemperatura_entry.get()

        if tipo == "terrestre":
            animal = AnimalTerrestre(
                nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidadeTemperatura)
            self.animais.append(animal)
            writeToFileAnimaisTerrestres(self.animais)

        elif tipo == "ave":
            animal = AnimalAve(
                nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidadeTemperatura)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)

        elif tipo == "aquatico":
            animal = AnimalAquatico(
                nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidadeTemperatura)
            self.animais.append(animal)
            writeToFileAnimaisAquaticos(self.animais)

        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.clearEntry()

    def deleteAnimal(self):  # Deleta um carro do JSON com base em seu código
        todosAnimais = []
        codigo = self.codigo_entry.get()
        with open("animais.json", "r") as r:
            todosAnimais = json.load(r)
        with open("animais.json", "w+") as w:
            for animal in todosAnimais:
                if str(animal["codigo"]) == codigo:
                    todosAnimais.remove(animal)
                    json.dump(todosAnimais, w, cls=UUIDEncoder)

        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.clearEntry()

    def editAnimal(self):  # Edita todas as informações de um carro, mantendo seu código
        todosAnimais = []
        self.animais = []
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        dieta = self.dieta_entry.get()
        sexo = self.sexo_entry.get()
        porte = self.porte_entry.get()
        limpo = self.limpo_entry.get()
        saude = self.saude_entry.get()
        tipo = self.tipo_entry.get()
        qualidadeTemperatura = self.qualidadeTemperatura_entry.get()

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)
        codigo = selected_values.get("values")[9]

        with open("animais.json", "r") as r:
            todosAnimais = json.load(r)
        with open("animais.json", "w+") as w:
            for animal in todosAnimais:
                if str(animal["codigo"]) == codigo:
                    todosAnimais.remove(animal)
                    json.dump(todosAnimais, w, cls=UUIDEncoder)

        self.trv.item(selected_item, values=(
            nome, idade, dieta, sexo, porte, limpo, saude, tipo, qualidadeTemperatura, codigo))

        if tipo == "terrestre":
            animal = AnimalTerrestre(nome, idade, dieta, sexo, porte, limpo,
                                     saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisTerrestres(self.animais)

        elif tipo == "ave":
            animal = AnimalAve(nome, idade, dieta, sexo, porte, limpo,
                               saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)

        else:
            animal = AnimalAquatico(nome, idade, dieta, sexo, porte, limpo,
                                    saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)

        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.clearEntry()

    # Mostra no Treeview todos os carros de uma marca determinada pelo usuário
    def buscarAnimal(self):
        global dadosAnimais
        nome = self.nome_entry.get()
        dadosAnimais = []

        if nome == "":
            self.lerJsonAnimais()
            self.loadTrvAnimais()
            self.clearEntry()
        else:
            todosAnimais = []
            with open("animais.json", "r") as f:
                todosAnimais = json.load(f)
            f.close

            for animal in todosAnimais:
                if nome == animal["nome"]:
                    dadosAnimais.append(animal)

        self.loadTrvAnimais()
        self.clearEntry()

    def mostrarAnimal(self):

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        selected_item_nome = selected_values.get("values")[0]
        selected_item_idade = selected_values.get("values")[1]
        selected_item_dieta = selected_values.get("values")[2]
        selected_item_sexo = selected_values.get("values")[3]
        selected_item_porte = selected_values.get("values")[4]
        selected_item_limpo = selected_values.get("values")[5]
        selected_item_saude = selected_values.get("values")[6]
        selected_item_tipo = selected_values.get("values")[7]
        selected_item_qualidadeTemperatura = selected_values.get("values")[8]
        selected_item_codigo = selected_values.get("values")[9]

        self.nome_entry.insert(0, selected_item_nome)
        self.idade_entry.insert(0, selected_item_idade)
        self.dieta_entry.insert(0, selected_item_dieta)
        self.sexo_entry.insert(0, selected_item_sexo)
        self.porte_entry.insert(0, selected_item_porte)
        self.limpo_entry.insert(0, selected_item_limpo)
        self.saude_entry.insert(0, selected_item_saude)
        self.tipo_entry.insert(0, selected_item_tipo)
        self.qualidadeTemperatura_entry.insert(
            0, selected_item_qualidadeTemperatura)
        self.codigo_entry.insert(0, selected_item_codigo)

    def clearEntry(self):  # Limpa todas as Entries
        self.nome_entry.delete(0, "end")
        self.idade_entry.delete(0, "end")
        self.dieta_entry.delete(0, "end")
        self.sexo_entry.delete(0, "end")
        self.porte_entry.delete(0, "end")
        self.limpo_entry.delete(0, "end")
        self.saude_entry.delete(0, "end")
        self.tipo_entry.delete(0, "end")
        self.qualidadeTemperatura_entry.delete(0, "end")
        self.codigo_entry.delete(0, "end")
