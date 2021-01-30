from tkinter import *
from tkinter import ttk
from cadastro import Cadastro
from deletar import Delete
from orm import listar, consultar
from atualizar import Update


root = Tk()


# Classe principal
class Main:
    def __init__(self):
        self.configurarJanela()
        self.criarMenu()
        self.criarAbas()
        self.labelsEntries()
        self.criarTabelaListar()
        self.criarTabelaConsultar()
        root.mainloop()

    # Configuração da janela  
    def configurarJanela(self):
        root.title('Sistema de Cadastro de Clientes')
        root.geometry('500x400+500+100')
        root.resizable(False, False)

    # Criação do Menu
    def criarMenu(self):
        self.menuPrincipal = Menu(root)

        self.cadastrar = Menu(self.menuPrincipal)
        self.menuPrincipal.add_command(label='Cadastrar', command=lambda: Cadastro(root))

        self.deletar = Menu(self.menuPrincipal)
        self.menuPrincipal.add_command(label='Deletar', command=lambda: Delete(root))

        self.atualizar = Menu(self.menuPrincipal)
        self.menuPrincipal.add_command(label='Atualizar', command=lambda: Update(root))

        root.config(menu=self.menuPrincipal)

    # Criação das abas da tela
    def criarAbas(self):
        self.listar = ttk.Notebook(root, height=400, width=490)
        self.listar.pack(pady=10)

        self.frameListar = Frame(self.listar)
        self.frameListar.pack()
        self.frameConsultar = Frame(self.listar)
        self.frameConsultar.pack()

        self.listar.add(self.frameListar, text='Lista de Clientes')
        self.listar.add(self.frameConsultar, text='Consulta de Clientes')

    # Criação da tabela de listagem dos clientes
    def criarTabelaListar(self):
        self.tabela = ttk.Treeview(self.frameListar, column=(
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

        # Inserindo na tabela os dados vindos do método 'listar'
        self.tabela.delete(*self.tabela.get_children())
        for i in listar():
            self.tabela.insert('', END, values=(i))

        self.tabela.place(relx=0.01, rely=0.1, width=480, height=500)

    # Criando tabela da aba de consultar clientes
    def criarTabelaConsultar(self):
        self.tabela = ttk.Treeview(self.frameConsultar, column=(
            'col1', 'col2', 'col3', 'col4'))

        self.tabela.column("#0", width=0)
        self.tabela.column("#1", width=100)
        self.tabela.column("#2", width=50)
        self.tabela.column("#3", width=100)
        self.tabela.column("#4", width=100)

        self.tabela.heading("#0", text='')
        self.tabela.heading("#1", text='código')
        self.tabela.heading("#2", text='nome')
        self.tabela.heading("#3", text='cidade')
        self.tabela.heading("#4", text='data cadastro')

        # Inserindo os dados vindo do método 'listar'
        self.tabela.delete(*self.tabela.get_children())
        for i in listar():
            self.tabela.insert('', END, values=i)

        self.tabela.place(relx=0.01, rely=0.2, width=480, height=400)
    
    # Criação dos campos de texto e das lebels
    def labelsEntries(self):
        self.nome = Label(self.frameConsultar, text='consultar por cliente')
        self.nome.place(relx=0.02, rely=0.04)
        self.nomeEntry = Entry(self.frameConsultar)
        self.nomeEntry.place(relx=0.02, rely=0.11)

        self.btn = Button(self.frameConsultar, text='consultar', command=lambda: [consultar, self.btnBuscar()])
        self.btn.place(relx=0.37, rely=0.1)

        self.btn = Button(self.frameListar, text='atualizar dados', command=lambda: self.criarTabelaListar())
        self.btn.place(relx=0.37, rely=0.0)

        self.btn = Button(self.frameConsultar, text='atualizar dados', command=lambda: self.criarTabelaConsultar())
        self.btn.place(relx=0.37, rely=0.0)

    # Método do campos buscar clientes
    def btnBuscar(self):
        self.tabela.delete(*self.tabela.get_children())
        for i in consultar(self.nomeEntry.get()):
            self.tabela.insert('', END, values=i)


Main()
