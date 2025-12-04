from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud
from schemas import GuitarraCreate, Guitarra 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/guitarras/", response_model=Guitarra)
def agregar_guitarra(guitarra: GuitarraCreate, db: Session = Depends(get_db)):
    # Verifica si ya existe una guitarra con el mismo idGuitarra
    if db.query(models.Guitarra).filter(models.Guitarra.idGuitarra == guitarra.idGuitarra).first():
        raise HTTPException(status_code=400, detail="Ya existe una guitarra con este ID")
    
    nueva_guitarra = crud.crear_guitarra(db, guitarra)
    return nueva_guitarra

@app.get("/guitarras/", response_model=list[Guitarra])
def leer_guitarras(db: Session = Depends(get_db)):
    guitarras = crud.obtener_guitarras(db)
    return guitarras

@app.delete("/guitarras/")
def eliminar_guitarra_por_id(idGuitarra: int = Query(..., description="ID de la guitarra a eliminar"), db: Session = Depends(get_db)):
    if crud.eliminar_guitarra(db, idGuitarra):
        return {"mensaje": f"Guitarra con ID {idGuitarra} eliminada con éxito"}
    raise HTTPException(status_code=404, detail=f"No se encontró la guitarra con ID {idGuitarra}")

@app.put("/guitarras/", response_model=Guitarra)
def actualizar_guitarra_por_id(guitarra: GuitarraCreate, db: Session = Depends(get_db)):
    guitarra_actualizada = crud.actualizar_guitarra(db, guitarra)
    if guitarra_actualizada:
        return guitarra_actualizada
    raise HTTPException(status_code=404, detail=f"No se encontró la guitarra con ID {guitarra.idGuitarra} para actualizar")