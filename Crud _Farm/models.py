from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

class productos(Database):
    __tablename__ = 'Productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    precio = Column(String(30))
    cantidad = Column(String(10))
    precio_mayoreo = Column(String(10))
    estatus = Column(String(10))
    
