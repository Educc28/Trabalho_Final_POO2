from tkinter import *
from tkinter import ttk
from veterinarios.vetFun import VetFun


class MenuVet(VetFun):  # Classe referente a tela
    def __init__(self):
        self.animais = []
        self.root = Tk()
        self.tela()
        self.framesTela()
        self.campos()
        self.lista()
        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.buttonsFrame()
        self.root.mainloop()

    def tela(self):  # Cria a tela
        self.root.title("Tela Veterinario")
        self.root.configure(background='green')
        self.root.geometry("1200x600")

    def framesTela(self):  # Cria os frames para a tela
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)

    def lista(self):  # Cria o Treeview para visualizar todos os carros
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

        self.data_label = Label(self.frame1, text="Data:", anchor='w')
        self.data_label.place(relx=0.2, rely=0)
        self.data_entry = Entry(self.frame1)
        self.data_entry.place(relx=0.235, rely=0.01)

        self.remedio_label = Label(self.frame1, text="Remedio:", anchor='w')
        self.remedio_label.place(relx=0.38, rely=0)
        self.remedio_entry = Entry(self.frame1)
        self.remedio_entry.place(relx=0.43, rely=0.01)

        self.nomeVet_label = Label(self.frame1, text="Nome Vet:", anchor='w')
        self.nomeVet_label.place(relx=0.6, rely=0)
        self.nomeVet_entry = Entry(self.frame1)
        self.nomeVet_entry.place(relx=0.66, rely=0.01)

        self.cpf_label = Label(self.frame1, text="CPF:", anchor='w')
        self.cpf_label.place(relx=0.8, rely=0)
        self.cpf_entry = Entry(self.frame1)
        self.cpf_entry.place(relx=0.825, rely=0.01)

    def buttonsFrame(self):  # Cria os botões da tela
        self.pegarConsulta_button = Button(
            self.frame1, text="Ultima Consulta", command=self.pegarConsulta)
        self.pegarConsulta_button.place(relx=0.498, rely=0.7, anchor='w')

        self.cuidarAnimal_button = Button(
            self.frame1, text="Cuidar", command=self.cuidarAnimal)
        self.cuidarAnimal_button.place(relx=0.498, rely=0.55, anchor='w')

        self.cuidarAnimal_button = Button(
            self.frame1, text="Alimentar", command=self.alimentaAnimal)
        self.cuidarAnimal_button.place(relx=0.425, rely=0.55, anchor='w')

        self.buscarAnimal_button = Button(
            self.frame1, text="Buscar", command=self.buscarAnimal)
        self.buscarAnimal_button.place(relx=0.425, rely=0.7, anchor='w')
