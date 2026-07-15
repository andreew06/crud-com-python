from pydantic import BaseModel

# formato que o usuário deve enviar
class UsuarioCreate(BaseModel):
    nome: str
    email: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool

    class Config:
        form_attributes = True