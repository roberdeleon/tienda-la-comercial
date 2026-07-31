# -*- coding: utf-8 -*-
# programa de cierre de caja
# hecho por kevin
 
# lista de ventas del dia
vs = [
    ("EF", 150.00),
    ("TJ", 89.50),
    ("EF", 45.25),
    ("TJ", 210.00),
    ("EF", 78.00),
    ("TJ", 156.75),
    ("EF", 92.50),
    ("EF", 34.00),
    ("TJ", 67.25),
    ("EF", 125.00),
]
 
def proc():
    # variables para los totales
    a = 0
    b = 0
    # recorre la lista de ventas
    for v in vs:
        if v[0] == "EF":
            # suma al total
            a = a + v[1]
        else:
            # suma al total
            b = b + v[1]
    # aqui se calcula el iva del 10%
    x = a - (a / 1.12)
    x = round(x, 2)
    y = b - (b / 1.12)
    y = round(y, 2)
    # la comision
    c = b * 0.05
    c = round(c, 2)
    # t = a + b + c
    # print("total", t)
    print("=" * 42)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * 42)
    print("Ventas en efectivo:      Q " + str(round(a, 2)))
    print("IVA incluido (efectivo): Q " + str(x))
    print("Ventas con tarjeta:      Q " + str(round(b, 2)))
    print("IVA incluido (tarjeta):  Q " + str(y))
    print("Comisión del POS:        Q " + str(c))
    print("-" * 42)
    print("Total del día:           Q " + str(round(a + b, 2)))
    print("Depósito neto:           Q " + str(round(a + b - c, 2)))
 
proc()
