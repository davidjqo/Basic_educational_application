import random


# Método que valida que la respuesta dada a una suma aleatoria sea la correcta
def sum(attempt, number_attempts, pts):
    if attempt <= number_attempts:  # Si el número de intentos es menor, continúa, de lo contrario, termina el programa
        # Cantidad de intentos restantes
        print("\nIntento " + str(attempt) + "/" + str(number_attempts))
        while True:  # Mientras que se haya ingresado un método de entrada
            try:
                random1 = random.randint(0, 99)  # Primer número random
                random2 = random.randint(0, 99)  # Segundo número random
                answer = random1 + random2  # Respuesta de la suma entre estos dos números
                # Solicita entrada al usuario
                user_answer = int(
                    input("¿Cuánto es " + str(random1) + " + " + str(random2) + "? "))
                if user_answer == answer:  # Si acertó el resultado, aumenta un intento y un punto
                    print("\n¡Excelente!")
                    attempt += 1
                    pts += 1
                    sum(attempt, number_attempts, pts)  # Llamada recursiva
                else:  # Si no acertó, únicamente aumenta un intento
                    print("\nNo tuvo suerte... " + "La respuesta correcta es: " + str(answer))
                    attempt += 1
                    sum(attempt, number_attempts, pts)  # Llamada recursiva
            except ValueError:  # Si no se ingresó el método de entrada, vuelva a ingresar
                print("\nIntento " + str(attempt) + "/" + str(number_attempts))
                print("\nIngresa un valor...")
                # Al validar que no se ingresó ningún tipo de entrada, vuelve al inicio,
                # sin aumentar el número de intentos
                # El programa lanza nuevos números aleatorios, aunque esto puede cambiar
                continue
    else:  # Si se acabará el número de intentos, muestra la nota
        nota = 100/number_attempts * pts
        print("\nSe acabó el número de preguntas...")
        print("\nNota: " + str(nota))
        exit()


def number_attempts():  # Método que solicita el número de intentos y llama a la función sum()
    while True:  # Se valida cualquier tipo de entrada
        try:
            number_attempts = int(input("¿Cuántas sumas? "))
            sum(1, number_attempts, 0)  # Inicie el método sum()
        except ValueError:
            print("\nIngresa un valor...")


number_attempts()  # Invocar método
