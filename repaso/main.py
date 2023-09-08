
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

    # funciones de una cadena

    str4: str = "podemos " + "agregar " + "cadenas " + "con +"

    print(f" {str4} \n ")


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

    # funciones de una lista

    for e in list2:             # iterar en una lista
        print(f" elemento = {e}")


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

    # funciones de un diccionario

    for k, v in dict2.items():      # iterar en un diccionario
        print(f" llave: {k} - valor: {v}")


if __name__ == "__main__":

    # cadenas
    string_overview()

    # listas
    list_overview()

    # diccionarios
    dict_overview()
