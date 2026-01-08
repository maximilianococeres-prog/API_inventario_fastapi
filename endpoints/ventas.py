from fastapi import APIRouter, HTTPException
from schemas import Venta
from database import SessionLocal
from models import VentasDB, ProductoDB


router = APIRouter()


@router.post("/ventas")

def registrar_venta(venta: Venta):
    db = SessionLocal()
    
    
    producto = db.query(ProductoDB).filter(ProductoDB.id == venta.producto_id).first()
    
    if not producto:
        db.close()
        raise HTTPException(status_code= 404, detail = "Producto no encontrado")
    
    if producto.stock < venta.cantidad:
        db.close()
        raise HTTPException(status_code=400, detail="No hay stock suficiente")
    
    producto.stock -= venta.cantidad
    
    venta_db = VentasDB(producto_id=venta.producto_id, cantidad = venta.cantidad)
    
    
    try:
        db.add(venta_db)
        db.commit()
        db.refresh(venta_db)
    finally:
        db.close()
    
    return venta_db

