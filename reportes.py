# -*- coding: utf-8 -*-
# Modulo de reportes de La Comercial

from inventario import PRODUCTOS, valor_inventario

def reporte_inventario():
    print("REPORTE DE INVENTARIO")
    print("-" * 40)
    for producto in PRODUCTOS:
        linea = producto["codigo"] + "  " + producto["nombre"]
        valor = "Q" + format(producto["precio"], ".2f")
        print(linea.ljust(32) + valor.rjust(8))
    print("-" * 40)
    print("Valor total del inventario: Q" + format(valor_inventario(), ".2f"))
    # pendiente: exportar a archivo

if __name__ == "__main__":
    reporte_inventario()
