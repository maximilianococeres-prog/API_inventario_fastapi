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
    
    
    #actualizacion de la cantidad del stock
    
    cantidad_actual = actualizar.cantidad
    
    
    producto.stock += cantidad_actual
    
    if producto.stock + cantidad_actual < 0:
        raise HTTPException(400, "Stock insuficiente")

    
    actualizar_db = ActualizarDB(producto_id = actualizar.producto_id, cantidad = cantidad_actual)
    
    
    
    try:
        db.add(actualizar_db)
        db.commit()
        db.refresh(actualizar_db)
    finally:
        db.close()
    
    return f"Stock producto {actualizar.producto_id} actualizado"