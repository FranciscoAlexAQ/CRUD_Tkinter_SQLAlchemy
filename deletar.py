from tkinter import Toplevel


class Delete:
    def __init__(self, root):
        self.root = Toplevel()
        self.configurarJanela()
        self.root.transient(root)

    def configurarJanela(self):
        self.root.title('Deletar de clientes')
        self.root.geometry('500x400+500+100')
        self.root.resizable(False, False)
