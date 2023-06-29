import json
from tkinter import *
from funcionarios.funcionario import Funcionario
from admin.administrador import Administrador
from funcionarios.menuTerrestre import MenuTerrestre
from funcionarios.menuAve import MenuAve
from funcionarios.menuAquatico import MenuAquatico
from veterinarios.menuVet import MenuVet
from admin.menuAdmin import MenuAdmin
from veterinarios.ultimaConsulta import ultimaConsulta


nomeVet = ''
cpfVet = ''
data = ''
remedio = ''
dadosAnimias = []
dadosUsuarios = []


def login_text():  # Função referente ao texto que será retornado quando um usuário tentar fazer login
    print("Por favor, faça o login.")
    temp_usuario = {'nome': '', 'senha': ''}
    temp_usuario['nome'] = input("Nome de usuário: ")
    temp_usuario['senha'] = input("Senha: ")
    return temp_usuario


# Função que confere se o login utilizado existe
def check_usuario(usuarios, temp_usuario):
    for usuario in usuarios:
        if usuario['nome'] == temp_usuario['nome']:
            if usuario['senha'] == temp_usuario['senha']:
                return usuario
            else:
                print("Senha incorreta\n")
                return False
    print('Não há um usuário com esse nome\n')


def check_Worker(usuario):  # Função que confere se um usuário é funcionário
    global nomeVet
    global cpfVet

    if usuario['tipo'] == "administrador":
        MenuAdmin()
    elif usuario['tipo'] == "terrestre":
        MenuTerrestre()
    elif usuario['tipo'] == "ave":
        MenuAve()
    elif usuario['tipo'] == "aquatico":
        MenuAquatico()
    elif usuario['tipo'] == "veterinario":
        MenuVet()


def main():  # Função main que chama o menu
    FirstWindow()


class FirstWindowFuncs():
    def login(self):
        usuarios: list = []
        temp_usuario = {'nome': '', 'senha': ''}
        with open("./usuarios.json", "r") as f:
            usuarios = json.load(f)

        temp_usuario['nome'] = self.nome_entry.get()
        temp_usuario['senha'] = self.senha_entry.get()

        usuario = check_usuario(usuarios, temp_usuario)
        self.root.destroy()
        check_Worker(usuario)


class FirstWindow(FirstWindowFuncs):
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.title("Tela de Login")
        self.root.configure(background='gray')
        self.root.geometry("300x150")
        self.root.resizable(False, False)

    def widgets(self):

        self.nome_label = Label(text="Nome")
        self.nome_label.place(relx=0.15, rely=0.09)

        self.senha_label = Label(text="Senha")
        self.senha_label.place(relx=0.15, rely=0.25)

        self.login_button = Button(text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.nome_entry = Entry()
        self.nome_entry.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.senha_entry = Entry(show="*")
        self.senha_entry.place(relx=0.5, rely=0.3, anchor=CENTER)


if __name__ == "__main__":  # Início do código
    main()
