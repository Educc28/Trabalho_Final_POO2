import json
from tkinter import *
from animais.animais_terrestres import AnimalTerrestre
from animais.animais_aquaticos import AnimalAquatico
from animais.animais_aves import AnimalAve
from utilities import *


global dadosAnimais
global dadosUsuarios
dadosAnimais = []
dadosUsuarios = []


class FuncionarioFun():  # Classe referente as funções do programa dos funcionarios
    def __init__(self):
        self.Animais = []
        self.Usuarios = []

    def lerJsonAnimais(self):  # Lê todos os animais do JSON
        global dadosAnimais
        with open("animais.json", "r") as f:
            dadosAnimais = json.load(f)
        f.close

    def RemoveTodosAnimais(self):  # Remove os Animais do Treeview
        for item in self.trv.get_children():
            self.trv.delete(item)

    def loadTrvAnimaisTerrestres(self):  # Carrega Animais para o Treeview
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
            codigo = k["codigo"]

            if tipo == "terrestre":
                especial = k["qualidade_solo"]

                self.trv.insert('', index='end', iid=rowIndex, text="",
                                values=(nome, idade, dieta, sexo, porte, limpo, saude, tipo, especial, codigo))
                rowIndex = rowIndex+1

    def loadTrvAnimaisAves(self):  # Carrega Animais para o Treeview
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
            codigo = k["codigo"]

            if tipo == "ave":
                especial = k["qualidade_ninho"]
                self.trv.insert('', index='end', iid=rowIndex, text="",
                                values=(nome, idade, dieta, sexo, porte, limpo, saude, tipo, especial, codigo))
                rowIndex = rowIndex+1

    def loadTrvAnimaisAquaticos(self):  # Carrega Animais para o Treeview
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
            codigo = k["codigo"]

            if tipo == "aquatico":
                especial = k["temperatura_atual"]
                self.trv.insert('', index='end', iid=rowIndex, text="",
                                values=(nome, idade, dieta, sexo, porte, limpo, saude, tipo, especial, codigo))
                rowIndex = rowIndex+1

    def limpaAnimal(self):  # Faz com que os animais selecionados fiquem limpos
        todosAnimais = []
        self.animais = []

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        nome = selected_values.get("values")[0]
        idade = selected_values.get("values")[1]
        dieta = selected_values.get("values")[2]
        sexo = selected_values.get("values")[3]
        porte = selected_values.get("values")[4]
        limpo = "Limpo"
        saude = selected_values.get("values")[6]
        tipo = selected_values.get("values")[7]
        qualidadeTemperatura = selected_values.get("values")[8]
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
            self.lerJsonAnimais()
            self.loadTrvAnimaisTerrestres()

        elif tipo == "ave":
            animal = AnimalAve(nome, idade, dieta, sexo, porte, limpo,
                               saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAves()

        else:
            animal = AnimalAquatico(nome, idade, dieta, sexo, porte, limpo,
                                    saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAquaticos(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAquaticos()

        self.clearEntry()

    def alimentaAnimal(self):  # Faz com que os animais selecionados fiquem alimentados
        todosAnimais = []
        self.animais = []

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        nome = selected_values.get("values")[0]
        idade = selected_values.get("values")[1]
        dieta = "Alimentado"
        sexo = selected_values.get("values")[3]
        porte = selected_values.get("values")[4]
        limpo = selected_values.get("values")[5]
        saude = selected_values.get("values")[6]
        tipo = selected_values.get("values")[7]
        qualidadeTemperatura = selected_values.get("values")[8]
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
            self.lerJsonAnimais()
            self.loadTrvAnimaisTerrestres()

        elif tipo == "ave":
            animal = AnimalAve(nome, idade, dieta, sexo, porte, limpo,
                               saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAves()

        else:
            animal = AnimalAquatico(nome, idade, dieta, sexo, porte, limpo,
                                    saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAquaticos(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAquaticos()

        self.clearEntry()

    def ajustaSolo(self):  # Arruma o solo dos animais selecionados
        todosAnimais = []
        self.animais = []

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        nome = selected_values.get("values")[0]
        idade = selected_values.get("values")[1]
        dieta = selected_values.get("values")[2]
        sexo = selected_values.get("values")[3]
        porte = selected_values.get("values")[4]
        limpo = selected_values.get("values")[5]
        saude = selected_values.get("values")[6]
        tipo = selected_values.get("values")[7]
        qualidadeTemperatura = "Ótimo"
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
            self.lerJsonAnimais()
            self.loadTrvAnimaisTerrestres()

        elif tipo == "ave":
            animal = AnimalAve(nome, idade, dieta, sexo, porte, limpo,
                               saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAves()

    def ajustaTemperatura(self):  # Ajusta a temperatura dos animais selecionados
        todosAnimais = []
        self.animais = []

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        nome = selected_values.get("values")[0]
        idade = selected_values.get("values")[1]
        dieta = selected_values.get("values")[2]
        sexo = selected_values.get("values")[3]
        porte = selected_values.get("values")[4]
        limpo = selected_values.get("values")[5]
        saude = selected_values.get("values")[6]
        tipo = selected_values.get("values")[7]
        qualidadeTemperatura = self.temperatura_entry.get()

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

        if tipo == "aquatico":
            animal = AnimalAquatico(nome, idade, dieta, sexo, porte, limpo,
                                    saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAquaticos(self.animais)
            self.lerJsonAnimais()
            self.loadTrvAnimaisAquaticos()
            self.temperatura_entry.delete(0, "end")

    # Mostra no Treeview todos os animais com um nome determinado pelo usuário
    def buscarAnimalTerrestre(self):

        global dadosAnimais
        nome = self.nome_entry.get()
        dadosAnimais = []

        if nome == "":
            self.lerJsonAnimais()
            self.loadTrvAnimaisTerrestres()
            self.clearEntry()
        else:
            todosAnimais = []
            with open("animais.json", "r") as f:
                todosAnimais = json.load(f)
            f.close

            for animal in todosAnimais:
                if nome == animal["nome"]:
                    dadosAnimais.append(animal)

        self.loadTrvAnimaisTerrestres()
        self.clearEntry()

    # Mostra no Treeview todos os animais com um nome determinado pelo usuário
    def buscarAnimalAve(self):
        global dadosAnimais
        nome = self.nome_entry.get()
        dadosAnimais = []

        if nome == "":
            self.lerJsonAnimais()
            self.loadTrvAnimaisAves()
            self.clearEntry()
        else:
            todosAnimais = []
            with open("animais.json", "r") as f:
                todosAnimais = json.load(f)
            f.close

            for animal in todosAnimais:
                if nome == animal["nome"]:
                    dadosAnimais.append(animal)

        self.loadTrvAnimaisAves()
        self.clearEntry()

    # Mostra no Treeview todos os animais com um nome determinado pelo usuário
    def buscarAnimalAquaticos(self):
        global dadosAnimais
        nome = self.nome_entry.get()
        dadosAnimais = []

        if nome == "":
            self.lerJsonAnimais()
            self.loadTrvAnimaisAquaticos()
            self.clearEntry()
        else:
            todosAnimais = []
            with open("animais.json", "r") as f:
                todosAnimais = json.load(f)
            f.close

            for animal in todosAnimais:
                if nome == animal["nome"]:
                    dadosAnimais.append(animal)

        self.loadTrvAnimaisAquaticos()
        self.clearEntry()

    def clearEntry(self):  # Limpa todas as Entries
        self.nome_entry.delete(0, "end")
