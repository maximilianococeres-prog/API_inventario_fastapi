from database import engine, SessionLocal
from models import ProductoDB, VentasDB


def levantar_sesion():
    db = SessionLocal()
    inventario = db.query(ProductoDB).all()
    ventas = db.query(VentasDB).all()
    db.close()
    
    return inventario, ventas