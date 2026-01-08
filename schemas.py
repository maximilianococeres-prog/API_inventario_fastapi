from pydantic import BaseModel


class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    
    
class Venta(BaseModel):
    producto_id: int
    cantidad: int
    
    
class Actualizar(BaseModel):
    producto_id : int
    cantidad : int