import json
from tkinter import *
from animais.animais_terrestres import AnimalTerrestre
from animais.animais_aquaticos import AnimalAquatico
from animais.animais_aves import AnimalAve
from funcionarios.funcionario_terrestres import FuncionarioTerrestre
from funcionarios.funcionario_aves import FuncionarioAve
from funcionarios.funcionario_aquaticos import FuncionarioAquatico
from admin.administrador import Administrador
from veterinarios.veterinario import Veterinario
from utilities import *


global dadosAnimais
global dadosUsuarios
dadosAnimais = []
dadosUsuarios = []


class AdminFun():  # Classe referente as funções do admin
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

    def createAnimal(self):  # Cria um animal no JSON
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

    def deleteAnimal(self):  # Deleta um animal do JSON com base em seu código
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

    def editAnimal(self):  # Edita todas as informações de um animal, mantendo seu código
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

    def mostrarAnimal(self):  # Coloca as informações do animal selecionado no Treeview
        self.clearEntry()
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


# ****************************************************************************


    def lerJsonUsuarios(self):  # Lê todos os usuarios do JSON
        global dadosUsuarios
        with open("usuarios.json", "r") as f:
            dadosUsuarios = json.load(f)
        f.close

    def RemoveTodosUsuarios(self):  # Remove os Usuarios do Treeview
        for item in self.trv.get_children():
            self.trv.delete(item)

    def loadTrvUsuarios(self):  # Carrega Usuarios para o Treeview
        global dadosUsuarios

        self.RemoveTodosUsuarios()

        rowIndex = 1

        for k in dadosUsuarios:
            nome = k["nome"]
            cpf = k["cpf"]
            senha = k["senha"]
            tipo = k["tipo"]

            self.trv.insert('', index='end', iid=rowIndex, text="",
                            values=(nome, cpf, senha, tipo))
            rowIndex = rowIndex+1

    def createUsuario(self):  # Cria um usuario no JSON
        self.usuarios = []
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()
        tipo = self.tipo_entry.get()

        if tipo == "terrestre":
            usuario = FuncionarioTerrestre(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioTerrestre(self.usuarios)

        elif tipo == "ave":
            usuario = FuncionarioAve(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAve(self.usuarios)

        elif tipo == "aquatico":
            usuario = FuncionarioAquatico(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAquatico(self.usuarios)

        elif tipo == "administrador":
            usuario = Administrador(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAdmin(self.usuarios)

        elif tipo == "veterinario":
            usuario = Veterinario(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioVeterinario(self.usuarios)

        self.lerJsonUsuarios()
        self.loadTrvUsuarios()
        self.clearEntryUsuarios()

    def deleteUsuario(self):  # Deleta um usuario do JSON com base em seu nome
        todosUsuarios = []
        nome = self.nome_entry.get()
        with open("usuarios.json", "r") as r:
            todosUsuarios = json.load(r)
        with open("usuarios.json", "w+") as w:
            for usuario in todosUsuarios:
                if str(usuario["nome"]) == nome:
                    todosUsuarios.remove(usuario)
                    json.dump(todosUsuarios, w, cls=UUIDEncoder)

        self.lerJsonUsuarios()
        self.loadTrvUsuarios()
        self.clearEntryUsuarios()

    def editUsuario(self):  # Edita todas as informações de um usuario, mantendo seu código
        todosUsuarios = []
        self.usuarios = []
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()
        tipo = self.tipo_entry.get()

        selected_item = self.trv.selection()[0]

        with open("usuarios.json", "r") as r:
            todosUsuarios = json.load(r)
        with open("usuarios.json", "w+") as w:
            for usuario in todosUsuarios:
                if str(usuario["nome"]) == nome:
                    todosUsuarios.remove(usuario)
                    json.dump(todosUsuarios, w, cls=UUIDEncoder)

        self.trv.item(selected_item, values=(nome, cpf, senha, tipo))

        if tipo == "terrestre":
            usuario = FuncionarioTerrestre(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioTerrestre(self.usuarios)

        elif tipo == "ave":
            usuario = FuncionarioAve(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAve(self.usuarios)

        elif tipo == "aquatico":
            usuario = FuncionarioAquatico(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAquatico(self.usuarios)

        elif tipo == "administrador":
            usuario = Administrador(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioAdmin(self.usuarios)

        elif tipo == "veterinario":
            usuario = Veterinario(
                nome, cpf, senha, tipo)
            self.usuarios.append(usuario)
            writeToFileFuncionarioVeterinario(self.usuarios)

        self.lerJsonUsuarios()
        self.loadTrvUsuarios()
        self.clearEntryUsuarios()

    # Mostra no Treeview todos os usuario de um nome determinado pelo usuário
    def buscarUsuario(self):
        global dadosUsuarios
        nome = self.nome_entry.get()
        dadosUsuarios = []

        if nome == "":
            self.lerJsonUsuarios()
            self.loadTrvUsuarios()
            self.clearEntryUsuarios()
        else:
            todosUsuarios = []
            with open("usuarios.json", "r") as f:
                todosUsuarios = json.load(f)
            f.close

            for usuario in todosUsuarios:
                if nome == usuario["nome"]:
                    dadosUsuarios.append(usuario)

        self.loadTrvUsuarios()
        self.clearEntryUsuarios()

    def mostrarUsuario(self):  # Mostra nas entries, as informações selecionadas de um usuario
        self.clearEntryUsuarios()
        selected_item = self.trv.selection()[0]
        selected_values = self.trv.item(selected_item)

        selected_item_nome = selected_values.get("values")[0]
        selected_item_cpf = selected_values.get("values")[1]
        selected_item_senha = selected_values.get("values")[2]
        selected_item_tipo = selected_values.get("values")[3]

        self.nome_entry.insert(0, selected_item_nome)
        self.cpf_entry.insert(0, selected_item_cpf)
        self.senha_entry.insert(0, selected_item_senha)
        self.tipo_entry.insert(0, selected_item_tipo)

    def clearEntryUsuarios(self):  # Limpa todas as Entries
        self.nome_entry.delete(0, "end")
        self.cpf_entry.delete(0, "end")
        self.senha_entry.delete(0, "end")
        self.tipo_entry.delete(0, "end")
