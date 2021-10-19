from sqlalchemy.orm import Session
import models, schemas


def create_parent(db: Session,parentname:str):
    db_parent = models.Parent(parentname=parentname)
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent

def create_child(db: Session,childname:str,parent_id:int):
    db_child = models.Child(childname=childname,parent_id= parent_id)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child
    

def child_list(db):
    return db.query(models.Child).all()