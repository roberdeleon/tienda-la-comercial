# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona
 
# lista de vendedores
ds = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]
 
def calc():
    tp = 0
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    # recorre la lista
    for d in ds:
        # si vendio mas de 30000
        if d[1] > 30000:
            # calcula la comision del 8%
            c = d[1] * 0.08
            c = round(c, 2)
            # el bono es de 300
            if d[1] > 50000:
                b = 500
            else:
                b = 0
            tot = round(c + b, 2)
            tp = tp + tot
            print(d[0] + ": Q " + str(tot))
        else:
            # calcula la comision del 5%
            c = d[1] * 0.05
            c = round(c, 2)
            b = 0
            tot = round(c + b, 2)
            tp = tp + tot
            print(d[0] + ": Q " + str(tot))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * 44)
    print("Total a pagar: Q " + str(round(tp, 2)))
 
calc()
