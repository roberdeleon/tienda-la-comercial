# -*- coding: utf-8 -*-
"""Calcula e imprime las comisiones mensuales de los vendedores."""

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500
DECIMALES_MONEDA = 2

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def obtener_tasa_comision(ventas_mensuales):
    """Devuelve la tasa aplicable según las ventas del mes."""
    # La regla vigente exige superar el umbral, no solamente alcanzarlo.
    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        return TASA_COMISION_ALTA

    return TASA_COMISION_BASE


def calcular_bono(ventas_mensuales):
    """Devuelve el bono adicional correspondiente al vendedor."""
    # El bono se concede únicamente cuando las ventas superan el umbral.
    if ventas_mensuales > UMBRAL_BONO:
        return MONTO_BONO

    return 0


def calcular_pago_vendedor(ventas_mensuales):
    """Calcula la comisión y el bono de un vendedor."""
    tasa_comision = obtener_tasa_comision(ventas_mensuales)
    comision = ventas_mensuales * tasa_comision
    comision = round(comision, DECIMALES_MONEDA)

    bono = calcular_bono(ventas_mensuales)

    return round(
        comision + bono,
        DECIMALES_MONEDA,
    )


def calcular_comisiones(vendedores):
    """Calcula los pagos individuales y el total mensual."""
    pagos_vendedores = []
    total_pagar = 0

    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas_mensuales)
        pagos_vendedores.append(
            (nombre_vendedor, total_vendedor)
        )
        total_pagar = total_pagar + total_vendedor

    return pagos_vendedores, total_pagar


def imprimir_reporte_comisiones():
    """Imprime el reporte mensual conservando el formato original."""
    pagos_vendedores, total_pagar = calcular_comisiones(VENDEDORES)

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos_vendedores:
        print(nombre_vendedor + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_pagar, DECIMALES_MONEDA))
    )


imprimir_reporte_comisiones()