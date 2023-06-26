from tkinter import *
from tkinter import ttk
from admin.adminFun import AdminFun


class MenuAdmin(AdminFun):  # Classe referente a tela
    def __init__(self):
        self.animais = []
        self.root = Tk()
        self.tela()
        self.framesTela()
        self.changeWindowButton()
        self.lista()
        # self.lerJsonCarros()
        # self.loadTrvCarros()
        self.campos()
        self.buttonsFrame()
        self.root.mainloop()

    def tela(self):  # Cria a tela
        self.root.title("Tela")
        self.root.configure(background='gray')
        self.root.geometry("1200x600")

    def framesTela(self):  # Cria os frames para a tela
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.97, relheight=0.1)

        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.02, rely=0.15, relwidth=0.97, relheight=0.45)

        self.frame3 = Frame(self.root)
        self.frame3.place(relx=0.02, rely=0.63, relwidth=0.97, relheight=0.35)

    def changeWindowButton(self):
        self.changeButton = Button(
            self.frame1, text="Ver Usuarios", command=self.changeWindow)
        self.changeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    def changeWindow(self):
        self.root.destroy()
        # MenuAdminFuncionarios()

    def lista(self):  # Cria o Treeview para visualizar todos os carros
        self.trv = ttk.Treeview(self.frame3,
                                columns=(1, 2, 3, 4), show="headings", height="16")

        self.trv.heading(1, text="Nome", anchor="w")
        self.trv.heading(2, text="CPF", anchor="center")
        self.trv.heading(3, text="Senha", anchor="center")
        self.trv.heading(4, text="Tipo", anchor="center")

        self.trv.column("#1", anchor="w", width=100, stretch=True)
        self.trv.column("#2", anchor="w", width=200, stretch=True)
        self.trv.column("#3", anchor="w", width=100, stretch=True)
        self.trv.column("#4", anchor="w", width=100, stretch=True)

        self.trv.place(relx=0, rely=0)

    def campos(self):  # Cria as labels e entries da tela
        self.tipo_roupa_label = Label(
            self.frame2, text="Tipo de roupa:", anchor='w')
        self.tipo_roupa_label.place(relx=0, rely=0)
        self.tipo_roupa_entry = Entry(self.frame2)
        self.tipo_roupa_entry.place(relx=0.07, rely=0.01)

        self.tamanho_label = Label(self.frame2, text="Tamanho:", anchor='w')
        self.tamanho_label.place(relx=0.2, rely=0)
        self.tamanho_entry = Entry(self.frame2)
        self.tamanho_entry.place(relx=0.25, rely=0.01)

        self.tecido_label = Label(self.frame2, text="Tecido:", anchor='w')
        self.tecido_label.place(relx=0.38, rely=0)
        self.tecido_entry = Entry(self.frame2)
        self.tecido_entry.place(relx=0.42, rely=0.01)

        self.marca_label = Label(self.frame2, text="Marca:", anchor='w')
        self.marca_label.place(relx=0.55, rely=0)
        self.marca_entry = Entry(self.frame2)
        self.marca_entry.place(relx=0.59, rely=0.01)

        self.preco_label = Label(self.frame2, text="Preço:", anchor='w')
        self.preco_label.place(relx=0.72, rely=0)
        self.preco_entry = Entry(self.frame2)
        self.preco_entry.place(relx=0.755, rely=0.01)

        self.comprimento_manga_label = Label(
            self.frame2, text="Comprimento da Manga:", anchor='w')
        self.comprimento_manga_label.place(relx=0, rely=0.3)
        self.comprimento_manga_entry = Entry(self.frame2)
        self.comprimento_manga_entry.place(relx=0.12, rely=0.31)

        self.corte_label = Label(self.frame2, text="Corte:", anchor='w')
        self.corte_label.place(relx=0.25, rely=0.3)
        self.corte_entry = Entry(self.frame2)
        self.corte_entry.place(relx=0.285, rely=0.31)

        self.tipo_label = Label(self.frame2, text="Tipo:", anchor='w')
        self.tipo_label.place(relx=0.4, rely=0.3)
        self.tipo_entry = Entry(self.frame2)
        self.tipo_entry.place(relx=0.43, rely=0.31)

        self.cor_label = Label(self.frame2, text="Cor:", anchor='w')
        self.cor_label.place(relx=0.55, rely=0.3)
        self.cor_entry = Entry(self.frame2)
        self.cor_entry.place(relx=0.575, rely=0.31)

        self.codigo_label = Label(self.frame2, text="Codigo:", anchor='w')
        self.codigo_label.place(relx=0.7, rely=0.3)
        self.codigo_entry = Entry(self.frame2)
        self.codigo_entry.place(relx=0.745, rely=0.31)

    def buttonsFrame(self):  # Cria os botões da tela
        self.createRoupa_button = Button(
            self.frame2, text="Create", command=self.createRoupa)
        self.createRoupa_button.place(relx=0.46, rely=0.55, anchor='w')

        self.deleteRoupa_button = Button(
            self.frame2, text="Delete", command=self.deleteRoupa)
        self.deleteRoupa_button.place(relx=0.498, rely=0.55, anchor='w')

        self.edit_Roupa_button = Button(
            self.frame2, text="Editar", command=self.editRoupa)
        self.edit_Roupa_button.place(relx=0.425, rely=0.55, anchor='w')
