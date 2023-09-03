# Juego de adivinar el numero
# El usuario piensa un numero entre los rangos a y b.
# El agente trata de adivinarlo, su respuesta es un numero entre los rangos a y b, tal que a <= respuesta <= b
# El usuario responde con "A" si el numero es mayor
# "B" si el numero es menor
# "C" si el numero es correcto
# Si el valor no es correcto, se ajusta el rango de busqueda a y b del agente utilizando el metodo de busqueda binaria

# Importa el modulo random para generar numeros aleatorios
import random

# Clase que representa al agente que adivina el numero
class GuessingAgent:
    # Constructor de la clase, requiere el rango de busqueda
    def __init__(self, min_range, max_range):
        # Acotaciones inferior del rango de busqueda
        self.min_range = min_range
        # Acotacion superior del rango de busqueda
        self.max_range = max_range
        # Respuesta actual del agente, sirve para actualizar el rango de busqueda
        self.current_guess = 0
        # Bandera que indica si el jugador ha mentido
        self.player_is_lying = False
    
    # Metodo que genera un numero aleatorio dentro del rango de busqueda, es la respuesta del agente
    def guess(self):
        # Verifica si el jugador ha mentido. Se concluye que el jugador ha mentido cuando el rango de busqueda no es coherente
        if self.min_range > self.max_range:
            self.player_is_lying = True
        # Genera un numero aleatorio dentro del rango de busqueda
        self.current_guess = random.randint(self.min_range, self.max_range)
        return self.current_guess
    
    # Metodo que actualiza el rango de busqueda del agente
    def update_ranges(self, is_higher):
        # Verifica si el jugador ha mentido, si es asi, no actualiza el rango de busqueda
        if self.player_is_lying:
            return
        # Actualiza el rango de busqueda dependiendo de la respuesta del jugador
        if is_higher:
            # Si el numero es demasiado alto, se actualiza la acotacion superior del rango de busqueda, la busqueda comenzara en el siguiente numero de la respuesta actual
            self.min_range = self.current_guess + 1
        else:
            # Si el numero es demasiado bajo, se actualiza la acotacion inferior del rango de busqueda, la busqueda terminara en el numero anterior a la respuesta actual
            self.max_range = self.current_guess - 1

# Funcion que solicita un numero entero al usuario, si el valor ingresado no es un numero entero, se solicita de nuevo. Termina  cuando el usuario ingresa un numero entero
def getDigitInput(message):
    while True:
        # Solicita el valor al usuario, elimina los espacios en blanco al inicio y al final del valor ingresado
        value = input(message).strip()
        # Verifica si el valor ingresado es un numero entero
        if not value.isdigit():
            # Si el valor no es un numero entero, se solicita de nuevo
            print("El valor debe ser un numero entero")
            continue
        return int(value)

# Funcion principal del programa, punto de entrada
def main():
    print("Bienvenido al juego \"Adivina el numero\"")
    min_range = getDigitInput("Ingrese el valor minimo del rango: ")
    max_range = getDigitInput("Ingrese el valor maximo del rango: ")
    # Verifica si el valor minimo y maximo son iguales. Si es asi, solo hay un numero posible, el agente ya lo ha adivinado
    if min_range == max_range:
        print("El valor minimo y maximo son iguales, el agente no puede adivinar el numero")
    # Verifica si el valor minimo es mayor al valor maximo
    if min_range > max_range:
        # Si el valor minimo es mayor al valor maximo, se intercambian los valores
        min_range, max_range = max_range, min_range
    # Crea una instancia de la clase GuessingAgent
    agent = GuessingAgent(min_range, max_range)
    # Ciclo infinito, termina cuando el agente adivina el numero o cuando el jugador miente
    while True:
        # El agente adivina el numero
        agent_guess = agent.guess()
        # Verifica si el jugador ha mentido
        if agent.player_is_lying:
            # Si el jugador ha mentido termina el programa
            print("El jugador ha mentido! :C. El agente no puede adivinar el numero")
            return
        # Verifica si el agente ha adivinado el numero
        else:
            while True:
                print(f"El agente adivina: {agent_guess}")
                # Solicita la pista del jugador
                user_response = input("Es demasiado alto (A), demasiado bajo (B) o correcto (C)? ").upper()
                # Verifica la respuesta del jugador
                if user_response == "A":
                    # Si el numero es demasiado alto, se actualiza el rango de busqueda del agente
                    agent.update_ranges(True)
                    break
                elif user_response == "B":
                    # Si el numero es demasiado bajo, se actualiza el rango de busqueda del agente
                    agent.update_ranges(False)
                    break
                elif user_response == "C":
                    # Si el numero es correcto, el agente ha ganado. Termina el programa
                    print("El agente ha ganado!")
                    return
                else:
                    # Si la respuesta no es valida, se solicita de nuevo
                    print("Respuesta no valida, por favor intente de nuevo")

# Verifica si el archivo actual es el archivo principal
if __name__ == "__main__":
    # Ejecuta la funcion principal
    main()