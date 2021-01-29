from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///banco.db')
Base = declarative_base()
Session = sessionmaker(bind=Engine)
session = Session()


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100))
    cidade = Column(String(100))
    data = Column(String(20))

    def __repr__(self):
        return f'{self.nome}'


Base.metadata.create_all(Engine)


def cadastrar(nome, cidade, data):
    cliente = Cliente(nome=nome, cidade=cidade, data=data)
    session.add(cliente)
    session.commit()
