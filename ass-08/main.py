
# Importamos las bibliotecas que vamos a utilizar.

from sklearn import datasets
from sklearn import model_selection
from sklearn import preprocessing


def main():
    # Importamos conjunto de datos y almacenamos en variable.
    dataset = datasets.load_breast_cancer()
    # Imprimimos el conjunto de datos.
    print(f"{dataset}\n")
    # Informacion en el conjunto de datos.
    print(f"Llaves en el diccionario: {dataset.keys()}\n")
    # Descripcion del conjunto de datos.
    print(f"{dataset.DESCR}\n")
    # Seleccionar todas las muestras del conjunto de datos.
    X = dataset.data
    print(f"Muestras: {X}\n")
    # Obtener etiquetas del conjunto de datos.
    y = dataset.target
    print(f"Etiquetas: {y}\n")
    # Separar los datos para entrenamiento y pruebas
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    # Mostrar datos separados
    print(f"X train: {X_train}\n\n X test: {X_test}\n")
    print(f"y train: {y_train}\n\n y test: {y_test}\n")


main()
