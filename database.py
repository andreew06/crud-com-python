from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# cria arquivo local chamado meubanco.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./meubanco.db"

# o 'engine' é o motor que vai executar comandos no banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# A 'SessionLocal' é o que usaremos para conversar com o banco ex: salvar, deletar, etc

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()