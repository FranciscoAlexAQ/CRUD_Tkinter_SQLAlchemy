from tkinter import Toplevel
from datetime import datetime
from tkinter import *
from orm import cadastrar


class Cadastro:
    def __init__(self, root):
        self.root = Toplevel()
        self.configurarJanela()
        self.criarEntriesLables()
        self.pegarData()
        self.root.transient(root)

    def configurarJanela(self):
        self.root.title('Cadastro de clientes')
        self.root.geometry('500x400+500+100')
        self.root.resizable(False, False)

    def criarEntriesLables(self):
        self.nome = Label(self.root, text='nome')
        self.nome.place(relx=0.1, rely=0.2)
        self.entryNome = Entry(self.root)
        self.entryNome.place(relx=0.1, rely=0.27)

        self.cidade = Label(self.root, text='cidade')
        self.cidade.place(relx=0.1, rely=0.35)
        self.entryCidade = Entry(self.root)
        self.entryCidade.place(relx=0.1, rely=0.43)

        self.data = Label(self.root, text='data')
        self.data.place(relx=0.1, rely=0.5)
        self.entryData = Entry(self.root)
        self.entryData.place(relx=0.1, rely=0.55)

        self.btn = Button(self.root, text='cadastrar', 
                command=lambda: cadastrar(str(self.entryNome.get()).strip(), str(self.entryCidade.get()).strip(), str(self.entryData.get()).strip()))
        self.btn.place(relx=0.1, rely=0.62)

    def pegarData(self):
        self.tempo = datetime.now()
        self.dia = self.tempo.day
        self.mes = self.tempo.month
        self.ano = self.tempo.year

        if self.mes <= 9:
            self.data = f'{self.dia}/0{self.mes}/{self.ano}'
        
        self.entryData.insert(END, self.data)
