from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criação da Engine, Base e da Sessão 
Engine = create_engine('sqlite:///banco.db')
Base = declarative_base()
Session = sessionmaker(bind=Engine)
session = Session()


# Classe de Criação da tabela 'clienetes'
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(String(100))
    cidade = Column(String(100))
    data = Column(String(20))

    def __repr__(self):
        return f'{self.id} {self.nome} {self.cidade} {self.data}'


Base.metadata.create_all(Engine)

# Cadastrando os clientes
def cadastrar(nome, cidade, data):
    cliente = Cliente(nome=nome, cidade=cidade, data=data)
    session.add(cliente)
    session.commit()


# Listando os  clientes
def listar():
    return session.query(Cliente.id, Cliente.nome, Cliente.cidade, Cliente.data).all()


# Deletando os clientes
def deletar(nome):
    session.query(Cliente).filter(Cliente.nome == nome).delete()
    session.commit()

# Consultando os clientes
def consultar(nome):
    return session.query(Cliente).filter(Cliente.nome == nome).all()


# Atualizando os clientes
def atualizar(id, nome=Cliente.nome, cidade=Cliente.cidade):
    session.query(Cliente).filter(Cliente.id == id).update(
        {'nome': nome, 'cidade': cidade}
    )
    session.commit()


if __name__ == '__main__':
    #atualizar('Alex', 'alex', 'pereiro')
    #print(listar())
    print(pegarDadosAtualizar('Ana'))
