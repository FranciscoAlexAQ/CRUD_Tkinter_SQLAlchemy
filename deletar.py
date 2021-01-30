from tkinter import Toplevel
from tkinter import *
from orm import deletar


# Classe 'deletar'
class Delete:
    def __init__(self, root):
        self.root = Toplevel()
        self.criarEntriesLables()
        self.configurarJanela()
        
        self.root.transient(root)

    # Configurando janela
    def configurarJanela(self):
        self.root.title('Deletar de clientes')
        self.root.geometry('500x400+500+100')
        self.root.resizable(False, False)

    # Campos de textos e labels
    def criarEntriesLables(self):
        self.nome = Label(self.root, text='Nome do Cliente')
        self.nome.place(relx=0.1, rely=0.35)
        self.entryNome = Entry(self.root)
        self.entryNome.place(relx=0.1, rely=0.43)

        self.btn = Button(self.root, text='excluir', command=lambda: deletar(self.entryNome.get()))
        self.btn.place(relx=0.1, rely=0.52)
