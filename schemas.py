from pydantic import BaseModel, Field, EmailStr

# formato que o usuário deve enviar
class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_lenght=100, description="Nome completo do usuário")
    email: EmailStr

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool

    class Config:
        form_attributes = True