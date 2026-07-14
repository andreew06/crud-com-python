from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios" #Nome da tabela no banco 

    #definindo colunas
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)