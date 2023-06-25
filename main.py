import json
from tkinter import *


global dadosRoupas
global dadosUsuario

dadosRoupas = []
dadosUsuarios = []


def login_text():  # Função referente ao texto que será retornado quando um usuário tentar fazer login
    print("Por favor, faça o login.")
    temp_usuario = {'username': '', 'password': ''}
    temp_usuario['username'] = input("Nome de usuário: ")
    temp_usuario['password'] = input("Senha: ")
    return temp_usuario


# Função que confere se o login utilizado existe
def check_usuario(usuarios, temp_usuario):
    for usuario in usuarios:
        if usuario['username'] == temp_usuario['username']:
            if usuario['password'] == temp_usuario['password']:
                return usuario
            else:
                print("Senha incorreta\n")
                return False
    print('Não há um usuário com esse nome\n')


def check_isWorker(usuario):  # Função que confere se um usuário é funcionário
    if usuario['isWorker'] == True:
        return True
    else:
        return False


def main():  # Função main que chama o menu
    FirstWindow()


class FirstWindowFuncs():
    def login(self):
        usuarios: list = []
        temp_usuario = {'username': '', 'password': ''}
        with open("./usuario.json", "r") as f:
            usuarios = json.load(f)

        temp_usuario['username'] = self.nome_entry.get()
        temp_usuario['password'] = self.senha_entry.get()

        usuario = check_usuario(usuarios, temp_usuario)

        if check_isWorker(usuario):
            funcionario = Funcionario(
                usuario['username'], usuario['password'])
            self.root.destroy()
            AplicationWorker()
            # menuWorker(funcionario)
        else:
            usuario = Usuario(usuario['username'], usuario['password'])
            self.root.destroy()
            Aplication()
            # menuUsuario(usuario)


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
