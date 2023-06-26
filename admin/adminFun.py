import json
from tkinter import *
# from utilities import *
# from carro import Carro

global dadosCarros
dadosCarros = []


class AdminFun():  # Classe referente as funções do programa
    def __init__(self):
        self.carros = []

    def lerJsonCarros(self):  # Lê todos os carros do JSON
        global dadosCarros
        with open("carros.json", "r") as f:
            dadosCarros = json.load(f)
        f.close

    def RemoveTodosCarros(self):  # Remove os carros do Treeview
        for item in self.trv.get_children():
            self.trv.delete(item)

    def loadTrvCarros(self):  # Carrega dadosCarros para o Treeview
        global dadosCarros

        self.RemoveTodosCarros()

        rowIndex = 1

        for k in dadosCarros:
            marca = k["marca"]
            modelo = k["modelo"]
            ano = k["ano"]
            preco = k["preco"]
            estado = k["estado"]
            codigo = k["codigo"]

            self.trv.insert('', index='end', iid=rowIndex, text="",
                            values=('edit', marca, modelo, ano, preco, estado, codigo))
            rowIndex = rowIndex+1

    def createCarro(self):  # Cria um carro no JSON
        self.carros = []
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        ano = self.ano_entry.get()
        preco = self.preco_entry.get()
        estado = self.estado_entry.get()

        # carro = Carro(marca, modelo, ano, preco, estado)
        # self.carros.append(carro)
        # writeToFileCarro(self.carros)

        self.lerJsonCarros()
        self.loadTrvCarros()
        self.mediaCarro()
        self.clearEntry()

    # def deleteCarro(self):  # Deleta um carro do JSON com base em seu código
    #     codigo = self.codigo_entry.get()
    #     with open("carros.json", "r") as r:
    #         todosCarros = json.load(r)
    #     with open("carros.json", "w+") as w:
    #         for carro in todosCarros:
    #             if str(carro["codigo"]) == codigo:
    #                 todosCarros.remove(carro)
    #                 json.dump(todosCarros, w, cls=UUIDEncoder)

    #     self.lerJsonCarros()
    #     self.loadTrvCarros()
    #     self.mediaCarro()
    #     self.clearEntry()

    # def editCarro(self):  # Edita todas as informações de um carro, mantendo seu código
    #     self.carros = []
    #     marca = self.marca_entry.get()
    #     modelo = self.modelo_entry.get()
    #     ano = self.ano_entry.get()
    #     preco = self.preco_entry.get()
    #     estado = self.estado_entry.get()

    #     selected_item = self.trv.selection()[0]
    #     selected_values = self.trv.item(selected_item)
    #     codigo = selected_values.get("values")[6]

    #     with open("carros.json", "r") as r:
    #         todosCarros = json.load(r)
    #     with open("carros.json", "w+") as w:
    #         for carro in todosCarros:
    #             if str(carro["codigo"]) == codigo:
    #                 todosCarros.remove(carro)
    #                 json.dump(todosCarros, w, cls=UUIDEncoder)

    #     self.trv.item(selected_item, values=(
    #         'edit', marca, modelo, ano, preco, estado, codigo))
    #     carro = Carro(marca, modelo, ano, preco, estado, codigo)
    #     self.carros.append(carro)
    #     writeToFileCarro(self.carros)

    #     self.lerJsonCarros()
    #     self.loadTrvCarros()
    #     self.mediaCarro()
    #     self.clearEntry()

    def mediaCarro(self):  # Calcula a média de todos os carros do JSON
        media = 0
        count = 0
        with open("carros.json", "r") as r:
            todosCarros = json.load(r)

        for carro in todosCarros:
            media = media + float(carro["preco"])
            count += 1
        media = media/count

        self.media_label.set(media)

    # Mostra no Treeview todos os carros de uma marca determinada pelo usuário
    def buscarCarro(self):
        global dadosCarros
        marca = self.marca_entry.get()
        dadosCarros = []

        if marca == "":
            self.lerJsonCarros()
            self.loadTrvCarros()
            self.mediaCarro()
            self.clearEntry()
        else:
            todosCarros = []
            with open("carros.json", "r") as f:
                todosCarros = json.load(f)
            f.close

            for carro in todosCarros:
                if marca == carro["marca"]:
                    dadosCarros.append(carro)

        self.loadTrvCarros()
        self.mediaCarro()
        self.clearEntry()

    def clearEntry(self):  # Limpa todas as Entries
        self.marca_entry.delete(0, "end")
        self.modelo_entry.delete(0, "end")
        self.ano_entry.delete(0, "end")
        self.preco_entry.delete(0, "end")
        self.estado_entry.delete(0, "end")
        self.codigo_entry.delete(0, "end")
