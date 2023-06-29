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


class VetFun():  # Classe referente as funções do programa do veterinario
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

    def loadTrvAnimais(self):  # Carrega Animais para o Treeview
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

    # Faz com que os animais selecionados fiquem saudaveis e salva as informações no json da ultima consulta
    def cuidarAnimal(self):

        todosAnimais = []
        todasConsultas = []
        self.animais = []
        self.consulta = []

        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        nome = selected_values.get("values")[0]
        idade = selected_values.get("values")[1]
        dieta = selected_values.get("values")[2]
        sexo = selected_values.get("values")[3]
        porte = selected_values.get("values")[4]
        limpo = selected_values.get("values")[5]
        saude = "Saudavel"
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

        with open("ultimaConsulta.json", "r") as t:
            todasConsultas = json.load(t)
        with open("ultimaConsulta.json", "w+") as z:
            for consulta in todasConsultas:
                if str(consulta["nome"]) == nome:
                    todasConsultas.remove(consulta)
                    json.dump(todasConsultas, z, cls=UUIDEncoder)

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
            writeToFileAnimaisAquaticos(self.animais)

        data = self.data_entry.get()
        remedio = self.remedio_entry.get()
        nomeVet = self.nomeVet_entry.get()
        cpf = self.cpf_entry.get()

        consulta = ultimaConsulta(nome, data, nomeVet, cpf, remedio)
        self.consulta.append(consulta)
        writeToFileUltimaConsulta(self.consulta, todasConsultas)

    def alimentaAnimal(self):  # Alimenta os animais selecionados
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

        elif tipo == "ave":
            animal = AnimalAve(nome, idade, dieta, sexo, porte, limpo,
                               saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAves(self.animais)

        else:
            animal = AnimalAquatico(nome, idade, dieta, sexo, porte, limpo,
                                    saude, tipo, qualidadeTemperatura, codigo)
            self.animais.append(animal)
            writeToFileAnimaisAquaticos(self.animais)

        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.clearEntry()

    # Mostra no Treeview todos os animais de um nome determinado pelo usuário

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

    def clearEntry(self):  # Limpa a entry do nome
        self.nome_entry.delete(0, "end")
