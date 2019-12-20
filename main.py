from elasticsearch import Elasticsearch

from .src.metodos_borrar import borrar_datos_elasticsearch
from .src.metodos_crear import genera_index
from .src.metodos_consultar import query_elastic
from .src.metodos_actualizar import update_json

es = Elasticsearch()

delete_datos = borrar_datos_elasticsearch
create_datos = genera_index
consult_datos = query_elastic
update_datos = update_json


print("---------------------------------------------------------------------------------------------------------------")
print("---------------- MENU DE OPCIONES PARA CREAR O BORRAR JSON DE ELASTICSEARCH -----------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("------- 1. Para crear documentos en los indices                                                                ")
print("------- 2. Para borrar documentos de los indices, donde:                                                       ")
print("----------- a. Borrar Masivamente                                                                              ")
print("----------- b. Borrar por id                                                                                   ")
print("------- 3. Para actualizar id documentos de los indices                                                        ")
print("------- 4. Para consultar  id documentos de los indices                                                        ")
print("---------------------------------------------------------------------------------------------------------------")

num_opcion = int(input("Ingrese la opcion: "))

if num_opcion == 1:
    pass
elif num_opcion == 2:
    tipo_opcion = str(input("Ingrese el tipo de borrado: "))
    if tipo_opcion == "a":
        pass
    elif tipo_opcion == "b":
        pass
    else:
        print("debe ingresar una opcion valida, opcion a o opcion b.")
elif num_opcion == 3:
    pass
elif num_opcion == 4:
    pass