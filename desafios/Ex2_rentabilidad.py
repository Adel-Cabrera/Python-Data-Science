producto = 50
usuarios = 1000
gastos = 20000
utilidades = (producto * usuarios) - gastos
impuestos = utilidades * 0.35
total = utilidades * 0.65

# Emprendedor1.py

if (utilidades > 0):
  print(f"Las utilidades son de {total}.")
else:
  print("Las utilidades son inferiores a 0.")

gratuitos = 300
premium = 700 * 50 * 2
utilidades_dos = premium - gastos
total_dos = utilidades_dos * 0.65

# Emprendedor2.py

if (utilidades_dos > 0):
  print(f"Las utilidades son de {total_dos}")
else:
  ("Las utilidades son inferiores a 0.")

#Emprendedor3.py

last_year = 1000
final = (total_dos / last_year) * 100

if (utilidades_dos > 0):
  print(f"El porcentaje actual, respecto al anterior es de {final} %")
else:
  print("Las utilidades de este año son inferiores a 0.")



