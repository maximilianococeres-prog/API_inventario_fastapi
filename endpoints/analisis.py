from services.analisis_services import levantar_sesion
import pandas as pd
from fastapi import APIRouter

router  = APIRouter()

@router.get("/analisis/producto-mas-vendido")



#ANALISIS DEL PRODUCTO MAS VENDIDO
def analizar_prod_mas_vendido():
    inventario, ventas = levantar_sesion()
    
    df_inventario = pd.DataFrame([{
        "id": i.id,
        "nombre": i.nombre,
        "precio": i.precio,
        "stock": i.stock
    } for i in inventario])
    
    df_ventas = pd.DataFrame([{
        "prod_id": v.producto_id,
        "cantidad": v.cantidad, 
    } for v in ventas])
    
    if df_inventario.empty:
        return {"mensaje": "No hay inventario para analizar"}
    
    df_inventario["nombre"] = df_inventario["nombre"].str.lower()
    
    
    id_mas_vendido = df_ventas.groupby("prod_id")["cantidad"].sum()
    
    cantidad_total_vendida = id_mas_vendido.max()
    
    nombre_producto = None
    
    for i in inventario:
        if int(id_mas_vendido.idxmax()) == i.id:
            nombre_producto = i.nombre
        
        
    
    resultado_prod_mas_vendido = {
        "El producto mas vendido es": {
        "Codigo"  : int(id_mas_vendido.idxmax()),
        "Cantidad vendida": int(cantidad_total_vendida),
        "Descripción": nombre_producto,
        },
    }
    
    
    
            
    return resultado_prod_mas_vendido

#ANALISIS PRODUCTOS BAJO STOCK
            
@router.get("/analisis/producto-bajo-stock")

def analizar_prod_bajo_stock():
    
    inventario, _ = levantar_sesion()
    resultado_bajo_stock = []
    
    for i in inventario:
        if i.stock < 5:
            resultado_bajo_stock.append({
                "bajo stock" : {
                    "id" : i.id,
                    "nombre": i.nombre,
                    "precio": i.precio,
                    "stock": i.stock,
                    "mensaje": f"Hay poco stock de {i.nombre}, priorizar reposición"
                }
            })
            
    return resultado_bajo_stock


#ANALISIS DE RANKING DE PRODUCTOS MAS VENDIDOS

@router.get("/analisis/ranking-productos-vendidos")

def analizar_ranking_prod_vendidos():
    
    inventario, ventas = levantar_sesion()
    
    df_ventas = pd.DataFrame([{
        "prod_id": v.producto_id,
        "cantidad": v.cantidad
    } for v in ventas])
    
    df_inventario = pd.DataFrame([{
        "id": i.id,
        "nombre": i.nombre,
        "precio": i.precio,
        "stock": i.stock
    } for i in inventario])
    
    df_ventas_inventario = pd.merge(df_inventario,df_ventas,left_on="id",right_on="prod_id",how="inner")
    
    id_mas_vendido = df_ventas_inventario.groupby("nombre")["cantidad"].sum().sort_values(ascending=False)
    ranking = id_mas_vendido.to_dict()
    
    return {"Descripción": "Ranking de los productos más vendidos",
            "Ranking": ranking,
            }
        

#ANALISIS DE PRODUCTOS POCO VENDIDOS

@router.get("/analisis/productos-menos-vendidos")

def productos_menos_vendidos():
    inventario, ventas = levantar_sesion()
    
    df_ventas = pd.DataFrame([{
        "prod_id": v.producto_id,
        "cantidad": v.cantidad
    } for v in ventas])
    
    df_inventario = pd.DataFrame([{
        "id": i.id,
        "nombre": i.nombre,
        "precio": i.precio,
        "stock": i.stock
    } for i in inventario])
    
    df_ventas_inventario = pd.merge(df_inventario,df_ventas,left_on="id",right_on="prod_id",how="inner", )
    
    df_ventas_inventario.fillna(0, inplace=True)
    
    
    id_menos_vendido = df_ventas_inventario.groupby("nombre")["cantidad"].sum().sort_values()
    
    ranking = id_menos_vendido.to_dict()
    
    return {"Descripción": "Ranking de los productos menos vendidos",
            "Ranking": ranking,
            
            }
    
    