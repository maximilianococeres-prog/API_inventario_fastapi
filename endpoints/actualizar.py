from fastapi import APIRouter, HTTPException
from schemas import Actualizar
from database import SessionLocal
from models import ProductoDB, ActualizarDB


router = APIRouter()

@router.post("/actualizar-stock")


def actualizar_stock(actualizar: Actualizar):
    db = SessionLocal()
    
    
    producto = db.query(ProductoDB).filter(ProductoDB.id == actualizar.producto_id).first()
    
    if not producto:
        db.close()
        raise HTTPException(status_code= 404, detail = "Producto no encontrado")
    
    
    producto.stock += actualizar.cantidad
    
    actualizar_db = ActualizarDB(producto_id = actualizar.producto_id, cantidad = actualizar.cantidad)
    
    try:
        db.add(actualizar_db)
        db.commit()
        db.refresh(actualizar_db)
    finally:
        db.close()
    
    return f"Stock producto {actualizar.producto_id} actualizado"