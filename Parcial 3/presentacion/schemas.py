# schemas.py
from pydantic import BaseModel

# Esquema base con datos comunes
class UsuarioBase(BaseModel):
    nombre: str
    email: str

# Esquema para recibir datos al crear (igual al base por ahora)
class UsuarioCreate(UsuarioBase):
    pass

# Esquema para devolver datos (incluye el ID)
class Usuario(UsuarioBase):
    id: int

    class Config:
        # Esto permite a Pydantic leer datos de objetos SQLAlchemy
        from_attributes = True