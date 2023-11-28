import random
import time

def generar_contraseña():
    contraseñas = ['123456', 'password', 'qwerty', 'letmein', 'admin']
    return random.choice(contraseñas)

def intento_hackeo():
    contraseña_objetivo = generar_contraseña()
    intentos_restantes = 3
    tiempo_limite = 10

    print("Bienvenido al minijuego de hacking. Tienes 3 intentos para adivinar la contraseña.")
    print(f"Tienes {tiempo_limite} segundos por intento. ¡Buena suerte!\n")

    while intentos_restantes > 0:
        print(f"Intentos restantes: {intentos_restantes}")
        inicio_tiempo = time.time()
        intento = input("Ingresa tu contraseña: ")
        fin_tiempo = time.time()
        tiempo_transcurrido = fin_tiempo - inicio_tiempo

        if tiempo_transcurrido > tiempo_limite:
            print("¡Tiempo agotado! Has excedido el tiempo permitido.")
            intentos_restantes -= 1
        elif intento == contraseña_objetivo:
            print("¡Contraseña correcta! Has hackeado exitosamente.")
            break
        else:
            print("Contraseña incorrecta. ¡Sigue intentando!\n")
            intentos_restantes -= 1

    if intentos_restantes == 0:
        print("Se acabaron los intentos. Has fallado en hackear la contraseña.")

if __name__ == "__main__":
    intento_hackeo()
