from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

# cria arquivo do banco de dados físico e tabelas (se não existirem) após ler models.py
models.Base.metadata.create_all(bind=engine)

# instancia principal de aplicação
app = FastAPI()

# função auxiliar para abrir e fechar conexão com o banco a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


# Rota POST para criar um usuário
@app.post("/usuarios/")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):

    # 1 preparação do dado (traduz do pydantic para SQLAlchemy)
    novo_usuario = models.Usuario(nome=usuario.nome, email=usuario.email)

    #2 adiciona na sessão
    db.add(novo_usuario)

    #3 salva no banco de dados
    db.commit()

    #4 atualiza a variavel com id que o banco gerou
    db.refresh(novo_usuario)

    #5 retorna o usuario criado para quem fez a requisição
    return novo_usuario


@app.get("/usuarios/", response_model=list[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    #1 busca no banco de dados
    usuarios = db.query(models.Usuario).all()

    #2 retorna lista de usuários
    return usuarios


@app.put("/usuarios/{usuario_id}", response_model=schemas.UsuarioResponse)
def atualizar_usuario(usuario_id: int, usuario:schemas.UsuarioCreate, db: Session = Depends(get_db)):
    #1 busca usuario específico no banco de dados
    usuario_db = db.query(models.Usuario).filter(models.Usuario. id == usuario_id).first()

    #2 se usuario não existir, trava a aplicação e devolve 404
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    #3 sobrescreve os dados velhos com os dados novos
    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email

    #4 salva a alteração no banco e atualiza a variável
    db.commit
    db.refresh(usuario_db)

    return usuario_db


@app.delete("/usuario/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session=Depends(get_db)):
    #1 busca o usuário específico no banco de dados
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id==usuario_id).first()

    #2 se o usuario não existir, devolve um erro 404
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    #3 da ordem de exclusão
    db.delete(usuario_db)

    #4 salva as alterações (remoção) no arquivo físico
    db.commit()

    #5 retorna mensagem de confirmação
    return {"mensagem": f"Usuário {usuario_db.nome}, id: {usuario_db.id} deletado com sucesso"}