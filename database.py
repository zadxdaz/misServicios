from lib2to3.pgen2.token import STRING
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    def __init__(self) -> None:
        pass

    id = Column(Integer,primary_key = True)
    name = Column(String)


class Servicios(Base):
    __tablename__ = "servicios"
    def __init__(self) -> None:
        pass

    id = Column(Integer,primary_key = True)
    userId = Column(Integer,ForeignKey(User.id))
    nombre = Column(String)
    monto = Column(Float)
    vencimiento = Column(Date)
