from tkinter import Toplevel
from tkinter import *
from orm import listar, atualizar


# Classe 'atualizar'
class Update:
    def __init__(self, root):
        self.root = Toplevel()
        self.criarEntriesLables()
        self.criarTabelaListar()
        self.configurarJanela()
        
        self.root.transient(root)

    # Coonfiguração da janela
    def configurarJanela(self):
        self.root.title('Deletar de clientes')
        self.root.geometry('500x400+500+100')
        self.root.resizable(False, False)

    # Criação dos campos de texto e das labels
    def criarEntriesLables(self):
        self.id = Label(self.root, text='Código do Cliente')
        self.id.place(relx=0.1, rely=0.35)
        self.entryId = Entry(self.root)
        self.entryId.place(relx=0.1, rely=0.4)

        self.nome = Label(self.root, text='Nome do Cliente')
        self.nome.place(relx=0.1, rely=0.5)
        self.entryNome = Entry(self.root)
        self.entryNome.place(relx=0.1, rely=0.55)

        self.cidade = Label(self.root, text='Cidade do Cliente')
        self.cidade.place(relx=0.1, rely=0.65)
        self.entryCidade = Entry(self.root)
        self.entryCidade.place(relx=0.1, rely=0.7)
        
        # Bitão atualizar
        self.btn = Button(self.root, text='atualizar', 
            command=lambda: atualizar(self.entryId.get(), self.entryNome.get(), self.entryCidade.get()))
        self.btn.place(relx=0.1, rely=0.76)

    # Função que realizar o duplo-click na tabela 'tabela'
    def duploClick(self, event):
        self.tabela.selection()

        for i in self.tabela.selection():
            col1, col2, col3, col4 = self.tabela.item(i, 'values')
            self.entryId.insert(END, col1)
            self.entryNome.insert(END, col2)
            self.entryCidade.insert(END, col3)

    # Tabela de listagem dos clientes
    def criarTabelaListar(self):
        self.tabela = ttk.Treeview(self.root, column=(
            'col1', 'col2', 'col3', 'col4'))

        self.tabela.column("#0", width=0)
        self.tabela.column("#1", width=100)
        self.tabela.column("#2", width=100)
        self.tabela.column("#3", width=100)
        self.tabela.column("#4", width=100)

        self.tabela.heading("#0", text='')
        self.tabela.heading("#1", text='código')
        self.tabela.heading("#2", text='nome')
        self.tabela.heading("#3", text='cidade')
        self.tabela.heading("#4", text='data cadastro')

        # envento duplo-click
        self.tabela.bind('<Double-1>', self.duploClick)

        # Inserindo dados
        self.tabela.delete(*self.tabela.get_children())
        for i in listar():
            self.tabela.insert('', END, values=(i))
           
        self.tabela.place(relx=0.01, rely=0.0, width=480, height=130)
