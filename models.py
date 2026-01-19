#Modelo de producto DB
from database import Base
from sqlalchemy import Column, Float, Integer, String,DateTime, ForeignKey
from datetime import datetime

class ProductoDB(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer,nullable=False)
    descripcion = Column(String,nullable = False)
    
    
    
class VentasDB(Base):
    __tablename__ = "ventas"
    id = Column(Integer,primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable= False)
    fecha = Column(DateTime, default=datetime.utcnow)
    

class ActualizarDB(Base):
    __tablename__ = "actualizacion_stock"
    id = Column(Integer, primary_key = True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable = False)
    cantidad = Column(Integer, nullable= False)