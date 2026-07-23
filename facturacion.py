# -*- coding: utf-8 -*-
# Modulo de facturacion de La Comercial
# Calcula subtotales, descuentos e IVA de cada venta

from inventario import buscar_producto, hay_stock
from descuentos import descuento_cliente_frecuente

NOMBRE_TIENDA = "Repuestos Robert"
IVA = 0.10

def calcular_subtotal(items):
    # items es una lista de tuplas (codigo, cantidad)
    subtotal = 0
    for codigo, cantidad in items:
        producto = buscar_producto(codigo)
        if producto and hay_stock(codigo, cantidad):
            subtotal = subtotal + producto["precio"] * cantidad
    return subtotal

def calcular_total(subtotal, descuento):
    base = subtotal - descuento
    impuesto = base * IVA
    return base + impuesto, impuesto

def imprimir_factura(cliente, items, frecuente):
    subtotal = calcular_subtotal(items)
    descuento = 0
    if frecuente:
        descuento = descuento_cliente_frecuente(subtotal)
    total, impuesto = calcular_total(subtotal, descuento)
    print("=" * 40)
    print(NOMBRE_TIENDA.center(40))
    print("Quetzaltenango, Guatemala".center(40))
    print("=" * 40)
    print("Cliente: " + cliente)
    for codigo, cantidad in items:
        producto = buscar_producto(codigo)
        if producto:
            linea = producto["nombre"] + " x" + str(cantidad)
            precio = producto["precio"] * cantidad
            print(linea.ljust(28) + ("Q" + format(precio, ".2f")).rjust(10))
    print("-" * 40)
    print("Subtotal:".ljust(28) + ("Q" + format(subtotal, ".2f")).rjust(10))
    print("Descuento:".ljust(28) + ("Q" + format(descuento, ".2f")).rjust(10))
    print("IVA (12%):".ljust(28) + ("Q" + format(impuesto, ".2f")).rjust(10))
    print("TOTAL:".ljust(28) + ("Q" + format(total, ".2f")).rjust(10))
    print("*** PROMOCIÓN DEL MES: 2x1 en escobas ***")
    print("Gracias por su compra. Vuelva pronto.")

if __name__ == "__main__":
    venta = [("A001", 2), ("B003", 2), ("C002", 5)]
    imprimir_factura("Juana Morales", venta, True)
