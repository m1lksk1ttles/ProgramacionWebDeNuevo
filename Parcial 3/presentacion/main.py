from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/")
def crear_usuario(usuario: crud.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/usuarios/")
def leer_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)