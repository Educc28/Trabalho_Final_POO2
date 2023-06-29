from tkinter import *
from tkinter import ttk
from funcionarios.funcionarioFun import FuncionarioFun


class MenuAve(FuncionarioFun):  # Classe referente a tela dos funcionarios aves
    def __init__(self):
        self.animais = []
        self.root = Tk()
        self.tela()
        self.framesTela()
        self.campos()
        self.lista()
        self.lerJsonAnimais()
        self.loadTrvAnimaisAves()
        self.buttonsFrame()
        self.root.mainloop()

    def tela(self):  # Cria a tela
        self.root.title("Tela Funcionario Ave")
        self.root.configure(background='cyan')
        self.root.geometry("1200x600")

    def framesTela(self):  # Cria os frames para a tela
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)

    def lista(self):  # Cria o Treeview para visualizar todos os animais aves
        self.trv = ttk.Treeview(self.frame2,
                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings", height="16")

        self.trv.heading(1, text="Nome", anchor="w")
        self.trv.heading(2, text="Idade", anchor="center")
        self.trv.heading(3, text="Dieta", anchor="center")
        self.trv.heading(4, text="Sexo", anchor="center")
        self.trv.heading(5, text="Porte", anchor="center")
        self.trv.heading(6, text="Limpo", anchor="center")
        self.trv.heading(7, text="Saude", anchor="center")
        self.trv.heading(8, text="Tipo", anchor="center")
        self.trv.heading(9, text="Qualidade/Temperatura", anchor="center")
        self.trv.heading(10, text="Codigo", anchor="center")

        self.trv.column("#1", anchor="w", width=100, stretch=True)
        self.trv.column("#2", anchor="w", width=100, stretch=True)
        self.trv.column("#3", anchor="w", width=100, stretch=True)
        self.trv.column("#4", anchor="w", width=100, stretch=True)
        self.trv.column("#5", anchor="w", width=100, stretch=True)
        self.trv.column("#6", anchor="w", width=100, stretch=True)
        self.trv.column("#7", anchor="w", width=100, stretch=True)
        self.trv.column("#8", anchor="w", width=100, stretch=True)
        self.trv.column("#9", anchor="w", width=150, stretch=True)
        self.trv.column("#10", anchor="w", width=250, stretch=True)

        self.trv.place(relx=0, rely=0)

    def campos(self):  # Cria as labels e entries da tela
        self.nome_label = Label(
            self.frame1, text="Nome:", anchor='w')
        self.nome_label.place(relx=0, rely=0)
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.035, rely=0.01)

    def buttonsFrame(self):  # Cria os botões da tela
        self.createAnimal_button = Button(
            self.frame1, text="Limpar", command=self.limpaAnimal)
        self.createAnimal_button.place(relx=0.498, rely=0.7, anchor='w')

        self.deleteAnimal_button = Button(
            self.frame1, text="Alimentar", command=self.alimentaAnimal)
        self.deleteAnimal_button.place(relx=0.498, rely=0.55, anchor='w')

        self.edit_Animal_button = Button(
            self.frame1, text="Ajustar Solo", command=self.ajustaSolo)
        self.edit_Animal_button.place(relx=0.425, rely=0.55, anchor='w')

        self.edit_Animal_button = Button(
            self.frame1, text="Buscar", command=self.buscarAnimalAve)
        self.edit_Animal_button.place(relx=0.425, rely=0.7, anchor='w')
