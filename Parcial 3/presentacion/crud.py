from models import Usuario
from sqlalchemy.orm import Session
from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo = Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
