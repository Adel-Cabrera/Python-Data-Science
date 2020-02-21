# No funciona from desafios import * , opr lo que lo haré manualmente
# Para ejecutar el cóódigo, remover todas las comillas triples

import pandas as pd

"""


#DataFrame => df

my_file = 'nations.csv'

df = pd.read_csv(my_file)

print(pd.read_csv(my_file))
print(df.shape) # Ver filas y columnas
print(df.head()) # 5 primeras líneas del documento
print(df.head(2)) # Primeras 2 lííneas
df = df.drop(columns = "Unnamed: 0") # Editar Dataframe
print(df.head())

print(df.loc[8, "life"])
print(type(df.loc[8, "life"])) # => float

df_subset = df.reindex(["gdp", "school", "adfert", "chidmort"])
print(type(df_subset))
print(df_subset)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#deprecate-loc-reindex-listlike

# Series

print(df["region"]) # => columna (key, value)
print(type(df["region"]))
print(df["region"].value_counts())
print(df["region"].value_counts().mean())
"""



"""
from desafios import Ex1_escape
from desafios import Ex2_rentabilidad
from desafios import Ex3_ppt
from desafios import Ex4_mayor_de_tres
from desafios import Ex5_desafios
from desafios import Ex6_funciones
from desafios import Ex7_funciones_y_listas as ex7
from desafios import Ex8_juegos_olimpicos
from desafios import Ex9_ventas


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,11, 11, 12, 12, 12, 12, 13, 13,13, 13, 14, 14, 14, 14, 15, 15,15, 16, 16, 17, 17, 17, 18, 18,18, 18, 19, 19, 19, 20, 20, 20,20, 20, 22, 23, 24, 24, 24, 24, 25]

prom = ex7.promedio(velocidad)
print(prom)

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

nested_list = [auto1, auto2, auto3, auto4, auto5, auto6]

mean = ex7.all_mean(nested_list)
print(mean)

avg = ex7.average_velocity(nested_list)
print(avg)

bool_car = ex7.filter_bool_car(nested_list)
print(bool_car)

car_float = ex7.float_car(nested_list)

print(car_float)

velocidad_dos = [4, 4, 7, 7, 8, 9, 10, 10, 10,11, 11, 12, 12, 12, 12, 13, 13,13, 13, 14, 14, 14, 14, 15, 15,15, 16, 16, 17, 17, 17, 18, 18,18, 18, 19, 19, 19, 20, 20, 20,20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia_dos = [2, 10, 4, 22, 16, 10, 18, 26, 34,17, 28, 14, 20, 24, 28, 26, 34, 34,46, 26, 36, 60, 80, 20, 26, 54, 32,40, 32, 40, 50, 42, 56, 76, 84, 36,46, 68, 32, 48, 52, 56, 64, 66, 54,70, 92, 93, 120, 85]

print(ex7.zip_vel_dis(velocidad_dos, distancia_dos))

from desafios import Ex11_API_Prueba as ex11

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&page=1&api_key='
api_key = 'LxiLXqbPbbACk2VrKaeiisyDTa5c8xfiqg2P7anJ'


resp = ex11.request(url, api_key)
ex11.build_web_page(resp)
ex11.photos_count(resp)



from desafios import Ex10_API as ex10

url_2= 'https://reqres.in/api/users'
payload = ""

resp_uno = ex10.request(url_2, 'GET', payload)
print(resp_uno)

payload = "{\r\n\t\"data\": [\r\n    {\r\n    \"id\": 1,\r\n    \"email\": \"george.bluth@reqres.in\",\r\n    \"first_name\": \"George\",\r\n    \"last_name\": \"Bluth\",\r\n    \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg\"\r\n    }\r\n  ]\r\n}\r\n"

resp_dos = ex10.request(url_2, 'POST', payload)
print(resp_dos)

payload = "{\r\n\t\"data\": [\r\n    {\r\n    \"id\": 1,\r\n    \"email\": \"darkonnen.master@Adel.com\",\r\n    \"first_name\": \"George\",\r\n    \"last_name\": \"Bluth\",\r\n    \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg\"\r\n    }\r\n  ]\r\n}\r\n"


resp_tres = ex10.request(url_2, 'PUT', payload)
print(resp_tres)

payload = "{\r\n\t\"data\": [\r\n    {\r\n    \"id\": 1,\r\n    \"email\": \"darkonnen.master@Adel.com\",\r\n    \"first_name\": \"George\",\r\n    \"last_name\": \"Bluth\",\r\n    \"avatar\": \"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg\"\r\n    }\r\n  ]\r\n}\r\n"

resp_cuatro = ex10.request(url_2, 'DELETE', payload)
print(resp_cuatro)

"""
