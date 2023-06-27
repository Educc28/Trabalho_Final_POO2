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
        self.campos()
        self.lista()
        self.lerJsonAnimais()
        self.loadTrvAnimais()
        self.buttonsFrame()
        self.root.mainloop()

    def tela(self):  # Cria a tela
        self.root.title("Tela Admin")
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
        MenuAdminWorker()

    def lista(self):  # Cria o Treeview para visualizar todos os carros
        self.trv = ttk.Treeview(self.frame3,
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
        self.trv.column("#5", anchor="w", width=100, stretch=True)
        self.trv.column("#6", anchor="w", width=100, stretch=True)
        self.trv.column("#7", anchor="w", width=100, stretch=True)
        self.trv.column("#8", anchor="w", width=100, stretch=True)
        self.trv.column("#9", anchor="w", width=100, stretch=True)
        self.trv.column("#10", anchor="w", width=250, stretch=True)

        self.trv.place(relx=0, rely=0)

    def campos(self):  # Cria as labels e entries da tela
        self.nome_label = Label(
            self.frame2, text="Nome:", anchor='w')
        self.nome_label.place(relx=0, rely=0)
        self.nome_entry = Entry(self.frame2)
        self.nome_entry.place(relx=0.035, rely=0.01)

        self.idade_label = Label(self.frame2, text="Idade:", anchor='w')
        self.idade_label.place(relx=0.2, rely=0)
        self.idade_entry = Entry(self.frame2)
        self.idade_entry.place(relx=0.235, rely=0.01)

        self.dieta_label = Label(self.frame2, text="Dieta:", anchor='w')
        self.dieta_label.place(relx=0.38, rely=0)
        self.dieta_entry = Entry(self.frame2)
        self.dieta_entry.place(relx=0.42, rely=0.01)

        self.sexo_label = Label(self.frame2, text="Sexo:", anchor='w')
        self.sexo_label.place(relx=0.55, rely=0)
        self.sexo_entry = Entry(self.frame2)
        self.sexo_entry.place(relx=0.58, rely=0.01)

        self.porte_label = Label(self.frame2, text="Porte:", anchor='w')
        self.porte_label.place(relx=0.7, rely=0)
        self.porte_entry = Entry(self.frame2)
        self.porte_entry.place(relx=0.735, rely=0.01)

        self.limpo_label = Label(self.frame2, text="Limpo:", anchor='w')
        self.limpo_label.place(relx=0, rely=0.3)
        self.limpo_entry = Entry(self.frame2)
        self.limpo_entry.place(relx=0.035, rely=0.31)

        self.saude_label = Label(self.frame2, text="Saude:", anchor='w')
        self.saude_label.place(relx=0.2, rely=0.3)
        self.saude_entry = Entry(self.frame2)
        self.saude_entry.place(relx=0.235, rely=0.31)

        self.qualidadeTemperatura_label = Label(
            self.frame2, text="Qualidade/Temperatura:", anchor='w')
        self.qualidadeTemperatura_label.place(relx=0.38, rely=0.3)
        self.qualidadeTemperatura_entry = Entry(self.frame2)
        self.qualidadeTemperatura_entry.place(relx=0.5, rely=0.31)

        self.tipo_label = Label(self.frame2, text="Tipo:", anchor='w')
        self.tipo_label.place(relx=0.635, rely=0.3)
        self.tipo_entry = Entry(self.frame2)
        self.tipo_entry.place(relx=0.67, rely=0.31)

        self.codigo_label = Label(self.frame2, text="Codigo:", anchor='w')
        self.codigo_label.place(relx=0.8, rely=0.3)
        self.codigo_entry = Entry(self.frame2)
        self.codigo_entry.place(relx=0.845, rely=0.31)

    def buttonsFrame(self):  # Cria os botões da tela
        self.createAnimal_button = Button(
            self.frame2, text="Create", command=self.createAnimal)
        self.createAnimal_button.place(relx=0.46, rely=0.55, anchor='w')

        self.deleteAnimal_button = Button(
            self.frame2, text="Delete", command=self.deleteAnimal)
        self.deleteAnimal_button.place(relx=0.498, rely=0.55, anchor='w')

        self.edit_Animal_button = Button(
            self.frame2, text="Editar", command=self.editAnimal)
        self.edit_Animal_button.place(relx=0.425, rely=0.55, anchor='w')

        self.edit_Animal_button = Button(
            self.frame2, text="Buscar", command=self.buscarAnimal)
        self.edit_Animal_button.place(relx=0.425, rely=0.7, anchor='w')

        self.edit_Animal_button = Button(
            self.frame2, text="Mostrar", command=self.mostrarAnimal)
        self.edit_Animal_button.place(relx=0.498, rely=0.7, anchor='w')


class MenuAdminWorker(MenuAdmin):  # Classe referente a tela
    def __init__(self):
        self.usuarios = []
        self.root = Tk()
        self.tela()
        self.framesTela()
        self.changeWindowButton()
        self.campos()
        self.lista()
        self.lerJsonUsuario()
        self.loadTrvUsuario()
        self.buttonsFrame()
        self.root.mainloop()

    def tela(self):  # Cria a tela
        self.root.title("Tela Admin")
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
            self.frame1, text="Ver Animais", command=self.changeWindow)
        self.changeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    def changeWindow(self):
        self.root.destroy()
        MenuAdmin()

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
        self.nome_label = Label(
            self.frame2, text="Nome:", anchor='w')
        self.nome_label.place(relx=0, rely=0)
        self.nome_entry = Entry(self.frame2)
        self.nome_entry.place(relx=0.07, rely=0.01)

        self.cpf_label = Label(self.frame2, text="CPF:", anchor='w')
        self.cpf_label.place(relx=0.2, rely=0)
        self.cpf_entry = Entry(self.frame2)
        self.cpf_entry.place(relx=0.25, rely=0.01)

        self.senha_label = Label(self.frame2, text="Senha:", anchor='w')
        self.senha_label.place(relx=0.38, rely=0)
        self.senha_entry = Entry(self.frame2)
        self.senha_entry.place(relx=0.42, rely=0.01)

        self.tipo_label = Label(self.frame2, text="Tipo:", anchor='w')
        self.tipo_label.place(relx=0.55, rely=0)
        self.tipo_entry = Entry(self.frame2)
        self.tipo_entry.place(relx=0.59, rely=0.01)

    def buttonsFrame(self):  # Cria os botões da tela
        self.createUsuario_button = Button(
            self.frame2, text="Create", command=self.createUsuario)
        self.createUsuario_button.place(relx=0.46, rely=0.55, anchor='w')

        self.deleteUsuario_button = Button(
            self.frame2, text="Delete", command=self.deleteUsuario)
        self.deleteUsuario_button.place(relx=0.498, rely=0.55, anchor='w')

        self.edit_Usuario_button = Button(
            self.frame2, text="Editar", command=self.editUsuario)
        self.edit_Usuario_button.place(relx=0.425, rely=0.55, anchor='w')
