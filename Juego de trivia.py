#Juego de trivia de Minecraft

preguntas = [
{"numero": "1", "Pregunta": "El Creeper es un mob que explota al acercarse al jugador.", "Respuesta": True},
{"numero": "2", "Pregunta": "Se puede fabricar un pico de madera usando troncos sin convertir en tablas.", "Respuesta": False},
{"numero": "3", "Pregunta": "Las vacas se pueden alimentar con trigo para que se reproduzcan.", "Respuesta": True},
{"numero": "4", "Pregunta": "El sol en Minecraft sale por el oeste y se pone por el este.", "Respuesta": False},
{"numero": "5", "Pregunta": "Si caes al agua desde cualquier altura, no recibes daño por caída.", "Respuesta": True}
]



def bienvenida(nombre="Jugador"):
    mensaje = f"==== Bienvenido {nombre} ====\n\n Estas son las reglas, leelas con mucha atencion {nombre}\n\n=================================================================================\n- 1. Lee cada pregunta con mucha ATENCION\n=================================================================================\n- 2. Cada pregunta tiene una respuesta de \n verdadero o falso, contestaras con 1 o con 2 \n (1 Es verdadero 2 es falso)\n=================================================================================\n- 3. Cada respuesta sumara un punto, al final del juego se dira tu puntuacion\n=================================================================================\n\nEso es todo Diviertete {nombre}."
    return mensaje
print(bienvenida(nombre=input("Ingresa tu nombre: ")))
while True:

    print("Empezamos en 3, 2, 1...")
    print()
    input("Pulsa cualquier tecla para continuar: ")
    total = 0
    
    #1
    print(f"Pregunta #{preguntas[0]['numero']}: {preguntas[0]['Pregunta']}")
    
    respuesta = int(input("| 1. Verdadero | 2. Falso | : "))
    
    if respuesta == 1: respuesta = True
    elif respuesta == 2: respuesta = False
    
    if respuesta == preguntas[0]['Respuesta']:
        print("Bien lo respondiste bien")
        total += 1
   
    else:
        print("La fallaste")
    
    #2
    print(f"Pregunta #{preguntas[1]['numero']}: {preguntas[1]['Pregunta']}")
    
    respuesta = int(input("| 1. Verdadero | 2. Falso | : "))
    
    if respuesta == 1: respuesta = True
    elif respuesta == 2: respuesta = False
    
    if respuesta == preguntas[1]['Respuesta']:
        print("Bien lo respondiste bien")
        total += 1
   
    else:
        print("La fallaste")
    
    #3
    print(f"Pregunta #{preguntas[2]['numero']}: {preguntas[2]['Pregunta']}")
    
    respuesta = int(input("| 1. Verdadero | 2. Falso | : "))
    
    if respuesta == 1: respuesta = True
    elif respuesta == 2: respuesta = False
    
    if respuesta == preguntas[2]['Respuesta']:
        print("Bien lo respondiste bien")
        total += 1
   
    else:
        print("La fallaste")
    
    #4
    print(f"Pregunta #{preguntas[3]['numero']}: {preguntas[3]['Pregunta']}")
    
    respuesta = int(input("| 1. Verdadero | 2. Falso | : "))
    
    if respuesta == 1: respuesta = True
    elif respuesta == 2: respuesta = False
    
    if respuesta == preguntas[3]['Respuesta']:
        print("Bien lo respondiste bien")
        total += 1
   
    else:
        print("La fallaste")

    #5
    print(f"Pregunta #{preguntas[4]['numero']}: {preguntas[4]['Pregunta']}")
    
    respuesta = int(input("| 1. Verdadero | 2. Falso | : "))
    
    if respuesta == 1: respuesta = True
    elif respuesta == 2: respuesta = False
    
    if respuesta == preguntas[4]['Respuesta']:
        print("Bien lo respondiste bien")
        total += 1
   
    else:
        print("La fallaste")

    print(f"Felicidades has llegado al final")
    print("¿Listo para ver tu puntuacion?")
    print()
    input("Presiona cualquier tecla: ")
    print()
    print(f"Tu puntuacion es de {total}!!")

    decision = int(input("¿Deseas seguir jugando? (1. Si 2. No): "))

    if decision == 1:
        continue
    
    elif decision == 2:
        break
