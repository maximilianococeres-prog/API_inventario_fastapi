from fastapi import FastAPI
from database import *
from models import ProductoDB
from endpoints import productos, ventas, analisis , actualizar


app= FastAPI(title="Inventario de Productos", version="1.0.0")

#Creacion de la tabla mediante el modelo de models.py
Base.metadata.create_all(engine)




app.include_router(productos.router)
app.include_router(actualizar.router)
app.include_router(ventas.router)
app.include_router(analisis.router)
