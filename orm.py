from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///banco.db')
Base = declarative_base()
Session = sessionmaker(bind=Engine)
session = Session()


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(String(100))
    cidade = Column(String(100))
    data = Column(String(20))

    def __repr__(self):
        return f'{self.id} {self.nome} {self.cidade} {self.data}'


Base.metadata.create_all(Engine)


def cadastrar(nome, cidade, data):
    cliente = Cliente(nome=nome, cidade=cidade, data=data)
    session.add(cliente)
    session.commit()


def listar():
    clientes = session.query(Cliente).all()
    return clientes


def deletar(nome):
    session.query(Cliente).filter(Cliente.nome == nome).delete()
    session.commit()


def consultar(nome):
    dados = session.query(Cliente).filter(Cliente.nome.like(f'%{nome}%')).all()
    return dados


if __name__ == '__main__':
    deletar('João ')
    print(listar())
