from fastapi import APIRouter
from schemas import Producto
from database import SessionLocal
from models import ProductoDB


router = APIRouter()

@router.post("/productos")

def crear_producto(producto: Producto):
    db = SessionLocal()
    producto_db = ProductoDB(nombre = producto.nombre, precio = producto.precio, stock = producto.stock)
    try:
        db.add(producto_db)
        db.commit()
        db.refresh(producto_db)
    finally:
        db.close()
    return producto_db



@router.get("/productos")

def leer_inventario():
    db = SessionLocal()
    inventario = db.query(ProductoDB).all()
    db.close()
    return inventario