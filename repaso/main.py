
from typing import List, Dict, Any


# Repaso de Python
# jueves 07 septiembre 2023

def string_overview() -> None:

    # cómo se define una cadena

    str1: str = "usando double quotes"
    str2: str = 'usando single quotes'
    str3: str = '''usando triple quotes'''

    # acceso a una cadena

    print(f" veamos toda la cadena: {str1}")
    print(f" veamos una parte: {str1[2:6]}")

    # modificación a una cadena

    print(f" las cadenas son inmutables, chin")

    ### Funciones de una cadena ###
    
    #Concatenación de cadenas
    str4: str = "podemos " + "agregar " + "cadenas " + "con +" #se pueden concatenar cadenas con +

    print(f" {str4} \n ") 

    #Longitud de una cadena
    print(f" la longitud de la cadena es: {len(str4)} \n ") #len() devuelve la longitud de la cadena

    #Indexación de cadenas
    print(f" el primer caracter de la cadena es: {str4[0]} \n ") #el primer caracter es el 0

    #Segmentacion de cadenas
    print(f" la cadena desde el caracter 2 al 5 es: {str4[2:6]} \n ") #el caracter 6 no se incluye

    #Busqueda de subcadenas
    contiene_subcadena: bool = "cadenas" in str4 #in devuelve true si la subcadena se encuentra en la cadena
    print(f" la subcadena 'cadenas' se encuentra en la cadena: {contiene_subcadena} \n ") 

    #Metodos de transfomacion 
    print(f" la cadena en mayusculas es: {str4.upper()} \n ") #upper() convierte la cadena a mayusculas
    print(f" la cadena en minusculas es: {str4.lower()} \n ") #lower() convierte la cadena a minusculas
    print(f" la cadena en mayusculas es: {str4.capitalize()} \n ") #capitalize() convierte la primera letra de la cadena a mayuscula

    #Busqueda
    indice = str4.find("cadenas") #find() devuelve el indice de la subcadena
    print(f" la subcadena 'cadenas' se encuentra en la posicion: {indice} \n ")

    #Reemplazo
    print(f" la cadena reemplazando 'cadenas' por 'strings' es: {str4.replace('cadenas', 'strings')} \n ") #replace() reemplaza la subcadena por otra

    #Eliminacion de espacios en blanco
    print(f" la cadena eliminando los espacios a la derecha es: {str4.rstrip()} \n ") #rstrip() elimina los espacios a la derecha

    #División de cadenas 
    print(f" la cadena separada por espacios es: {str4.split()} \n ") #split() separa la cadena por espacios

    #Union de cadenas
    print(f" la cadena unida por espacios es: {' '.join(str4.split())} \n ") #join() une la cadena por espacios
    pass

def list_overview() -> None:

    # cómo se define una lista

    list1: List[Any] = []  # de cualquier tipo
    list2: List[str] = ["yadira", "carlos", "benja", "naye", "antonio"]
    list3: List[List[int]] = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    # acceso a una lista

    print(f" veamos toda la lista: {list2}")
    print(f" veamos algunos elementos: primero={list2[0]}, tercero={list2[2]}")
    print(f" veamos una lista de listas: obtener el 2 = {list3[2][1]}")

    # modificación a una lista

    list2.append("mauricio")    # agregar elemento al final
    list2.reverse()             # invertir el orden
    list2.pop()                 # eliminar elemento al final

    print(f" {list2}")

    ### Funciones de una lista ###

    #Iterar en una lista
    for e in list2:             
        print(f" elemento = {e}")

    #Ordenar una lista
    list2.sort()                # sort() ordena la lista
    print(f" {list2}")

    #Longitud de una lista
    print(f" la longitud de la lista es: {len(list2)} \n ") #len() devuelve la longitud de la lista

    #Extender una lista
    list2.extend(list3)         # extend() extiende la lista con otra lista

    #Acceder al ultimo elemento de una lista
    print(f" el ultimo elemento de la lista es: {list2[-1]} \n ") #el ultimo elemento es el -1
    
    #Modificar un elemento de una lista
    list2[0] = "yadira"         #se puede modificar un elemento de la lista con el indice 
    print(f" {list2} \n ")

    #Eliminar un elemento de una lista
    list2.remove("yadira")      #remove() elimina el elemento de la lista
    print(f" {list2} \n ")

    #Adicionar otra lista a una lista
    list2.append(list3)         #append() agrega la lista al final de la lista
    print(f" {list2} \n ")

    pass

def dict_overview() -> None:

    # cómo se define un diccionario

    dict1: Dict[Any, Any] = {}  # cualquier tipo llave-valor
    dict2: Dict[str, int] = {"p1": 18, "p2": 20, "p3": 34}
    dict3: Dict[str, Dict[str, Any]] = {
        "ia": {
            "grupo": "6CV1",
            "alumnos": 20,
            "profesor": "Vannesa",
        },
        "sc": {
            "grupo": "6CV2",
            "alumnos": 13,
            "profesor": "Baltazar",
        }
    }

    # acceso a un diccionario

    print(f" veamos todo el diccionario: {dict2}")
    print(f" veamos algunos valores: 'p1'={dict2['p1']}, 'p3'={dict2['p3']}")
    print(f" veamos un diccionario de diccionarios: profesor-ia={dict3['ia']['profesor']}, alumnos-sc={dict3['sc']['alumnos']}")

    # modificación a un diccionario

    dict1[7] = "julio"              # agregamos una llave y su valor
    dict1["septiembre"] = 9         # en este diccionario no importa el tipo
    dict1["fibo"] = [1, 1, 2, 3, 5, 8, 13, 21]

    print(f" veamos todo el diccionario modificado: {dict1} ")

    ### Funciones de un diccionario ###

    # Iterar en un diccionario
    for k, v in dict2.items():      
        print(f" llave: {k} - valor: {v}")

    #Longitud de un diccionario
    print(f" la longitud del diccionario es: {len(dict2)} \n ") #len() devuelve la longitud del diccionario

    #Eliminar un elemento de un diccionario
    del dict2["p1"]                 #del elimina el elemento del diccionario
    print(f" {dict2} \n ")

    #Obtener las llaves de un diccionario
    print(f" las llaves del diccionario son: {dict2.keys()} \n ") #keys() devuelve las llaves del diccionario

    #Obtener los valores de un diccionario
    print(f" los valores del diccionario son: {dict2.values()} \n ") #values() devuelve los valores del diccionario

    #Obtener clave-valor de un diccionario
    print(f" las llaves y valores del diccionario son: {dict2.items()} \n ") #items() devuelve las llaves y valores del diccionario

    #Verificar si una llave se encuentra en un diccionario
    contiene_llave: bool = "p2" in dict2 #in devuelve true si la llave se encuentra en el diccionario
    print(f" la llave 'p2' se encuentra en el diccionario: {contiene_llave} \n ")

    #Copiar un diccionario
    dict4 = dict2.copy()            #copy() copia el diccionario
    print(f" {dict4} \n ")

    #Limpiar un diccionario
    dict4.clear()                   #clear() limpia el diccionario
    print(f" {dict4} \n ")

    pass

if __name__ == "__main__":

    # cadenas
    string_overview()

    # listas
    list_overview()

    # diccionarios
    dict_overview()
