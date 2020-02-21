from itertools import groupby
import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

for monto in ventas.values():
    if monto > 45000:
        print(monto)

for mes, monto in ventas.items():
    if monto > 45000:
        print(mes)

def filter(ventas, limite):
    return {month: amount for month, amount in ventas.items() if amount > limite}        

valores = [int(valor) for valor in sys.argv[1:]]

for valor in valores:
    mes_encontrado = False

    for mes, venta in ventas.items():
        if venta == valor:
            mes_encontrado = True
            print(mes)

    if not mes_encontrado:
        print('no encontrado')

quarters = {
    'Q1': [],
    'Q2': [],
    'Q3': [],
    'Q4': [],
}

quarters_data = [
    ["Enero", "Febrero", "Marzo"],
    ["Abril", "Mayo", "Junio"],
    ["Julio", "Agosto", "Septiembre"],
    ["Octubre", "Noviembre", "Diciembre"],
]

for index, meses in enumerate(quarters_data):
    quarter = index + 1
    for mes in meses:
        quarters['Q{}'.format(quarter)].append(ventas[mes])

print(quarters)

resultado = {}
for venta in ventas.values():
    if not venta in resultado:
        resultado[venta] = 0
    resultado[venta] += 1


print(resultado)