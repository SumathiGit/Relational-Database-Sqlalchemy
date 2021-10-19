from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os

from sqlalchemy.sql.sqltypes import String
from database import Base
#One to many
#many to one
class Parent(Base):
    __tablename__= 'parent'
    id = Column(Integer,primary_key = True)
    parentname = Column(String)
    # child_id = Column(Integer, ForeignKey('child.id'))
    children = relationship("Child", back_populates ="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    childname = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")