from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
from database import SessionLocal, engine
import models , crud



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Postgresql Relational Database")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/createparent/")
def create_parent(
    parentname :str, db: Session = Depends(get_db)):
    return crud.create_parent(db=db, parentname=parentname)


@app.post("/createchild/")
def create_child(
    childname :str,parent_id:int, db: Session = Depends(get_db)):
    return crud.create_child(db=db, parent_id=parent_id,childname=childname)


@app.get("/childlist/")
def chld_list(db: Session = Depends(get_db)):
    return crud.child_list(db = db)