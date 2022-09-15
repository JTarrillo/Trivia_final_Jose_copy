# imports
import os
import time
import random

# Declaración de constantes
CONTRASEÑA_SECRETA = "HOLA MUNDO"
# número de veces que se empleó la respuesta secreta
total_de_preguntas_secretas = 0
posibles_respuestas = ("A", "B", "C", "D", CONTRASEÑA_SECRETA)
rondas = 1  # numero de rondas jugadas
maximo_puntaje = 0  # Tomará al final el puntaje más alto presente en puntaciones_acumuladas
total_de_preguntas = 10  # total de preguntas de 1 ronda de trivia
puntaciones_acumuladas = []  # Es el listado de puntajes acumulados


########################### FUNCIONES VARIAS ###################################
def entrada_numerica(name, tiempo_de_espera=3):
    # Pregunta: define la cadena para solicitud de datos al usuario
    # Type: define el tipo de numero que debe aceptarse (1: Solo Enteros; 2: Decimales (y enteros, pero siempre retorna un decimal))
    # Incorrecto: define la cadena para mostrar al usuario al ingresar un parámetro invalido
    # Tarrineitor .:)
    pregunta = f"Vamos {name}, ingresa tu número (1-6): "
    pregunta2 = f"Vamos {name}, el número ingresado debe estar en el rango 1 a 6, sino es inválido, prueba otra vez: "
    incorrecto = "El valor ingresado no es un número correcto, espera unos segundos para intentarlo de nuevo."
    # numero a retornar (dependerá del tipo solicitado)
    numero_registrado = None

    while True:
        if numero_registrado == None:
            entry = input(
                pregunta
            )  # Se solicita el ingreso de un valor con la cadena dada como parámetro

            try:
                numero_registrado = int(
                    entry
                )  # Se intenta registrar como entero, de lo contrario pasa al except

            except ValueError:
                print(incorrecto + "\n")
                numero_registrado = None
                time.sleep(tiempo_de_espera)

        elif numero_registrado >= 0 and numero_registrado <= 6:
            break

        else:
            entry = input(
                pregunta2
            )  # Se solicita el ingreso de un valor con la cadena dada como parámetro

            try:
                numero_registrado = int(
                    entry
                )  # Se intenta registrar como entero, de lo contrario pasa al except

            except ValueError:
                print(incorrecto + "\n")
                numero_registrado = 8
                time.sleep(tiempo_de_espera)

    return numero_registrado


def cuentaRegresiva(tiempo=5):
    for i in range(tiempo, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    limpiar()


def cuentaRegresivaN(tiempo=5):
    for i in range(tiempo, 0, -1):
        print(f"{i}...")
        time.sleep(1)


def limpiar():  # Función para limpiar consola según so
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def setColour(text, color):  # Función que retorna texto coloreado
    BLACK = '\033[30m'  # b
    RED = '\033[31m'  # r
    GREEN = '\033[32m'  # g
    YELLOW = '\033[33m'  # y
    BLUE = '\033[34m'  # bl
    MAGENTA = '\033[35m'  # mg
    CYAN = '\033[36m'  # c
    WHITE = '\033[37m'  # w
    RESET = '\033[39m'

    if color == "b":
        text = BLACK + text + RESET
    elif color == "r":
        text = RED + text + RESET
    elif color == "g":
        text = GREEN + text + RESET
    elif color == "y":
        text = YELLOW + text + RESET
    elif color == "bl":
        text = BLUE + text + RESET
    elif color == "mg":
        text = MAGENTA + text + RESET
    elif color == "c":
        text = CYAN + text + RESET
    elif color == "w":
        text = WHITE + text + RESET

    return text


def imprimirTitulos(
    color="w",
    *args,
):  # Función para imprimir textos menores a 80char centrados
    BLACK = '\033[30m'  # b
    RED = '\033[31m'  # r
    GREEN = '\033[32m'  # g
    YELLOW = '\033[33m'  # y
    BLUE = '\033[34m'  # bl
    MAGENTA = '\033[35m'  # mg
    CYAN = '\033[36m'  # c
    WHITE = '\033[37m'  # w
    RESET = '\033[39m'

    for i in range(0, len(args)):
        if color == "b":
            print(BLACK + args[i].center(60, ' ') + RESET)
        elif color == "r":
            print(RED + args[i].center(60, ' ') + RESET)
        elif color == "g":
            print(GREEN + args[i].center(60, ' ') + RESET)
        elif color == "y":
            print(YELLOW + args[i].center(60, ' ') + RESET)
        elif color == "bl":
            print(BLUE + args[i].center(60, ' ') + RESET)
        elif color == "mg":
            print(MAGENTA + args[i].center(60, ' ') + RESET)
        elif color == "c":
            print(CYAN + args[i].center(60, ' ') + RESET)
        elif color == "w":
            print(WHITE + args[i].center(60, ' ') + RESET)


############################ PREGUNTAS #################################
questions = [  # Hay15Preguntas - [Pregunta, Respuesta Correcta, Otra1, Otra2, Otra3]
    [
        "Una de estas obras no es de Mozart. ¿Cuál de ellas?",
        "La flauta mágica",
        "La falsa jardinera",
        "Las bodas de Fígaro",
        "Madama Butterfly"
    ],
    [
        "¿Cuál de los siguientes cantantes pronunció la frase 'Prefiero que me odien por lo que soy a que me admiren por lo que nunca seré'?",
        "Freddie Mercury",
        "John Lennon",
        "Jim Morrison",
        " Kurt Cobain"
    ],
    [
        "Las bandas sonoras de este compositor le dieron un vuelco al spaguetti western. Hablamos de...",
        "John Williams", "Howard Shore", "Ennio Morricone", "James Horner"
    ],
    [
        "¿Cuál de estas canciones no es del grupo inmortal Queen?",
        "Don't Stop me now",
        "Tie your mother down",
        "These are the days of our lives"
    ],
    [
        "¿Cuál fue la primera grabación de Rock and Roll?",
        "Una canción de Elvis Presley",
        "Una canción de Little Richard",
        "Una canción de Bill Haley",
        "Una canción de Chuck Berry"
    ],
    [
        "Europe y su 'The final countdown' siguen despertando emociones. ¿Recuerdas de qué país era el grupo?",
        "Dinamarca", "Noruega", "Alemania", "Suecia"
    ],
    [
        "Nos remontamos mucho más atrás para preguntaros, ¿quién fue el primer trovador de la historia?",
        "Bernart de Ventadorn", "Guillermo IX de Aquitania", "Chrétien de Troyes", "Martín de Codax"
    ],
    [
        "¿De quién es la archiconocida canción 'All I have to do is dream'?",
        "Johnny Cash", "The Teenagers", "The Platters", "The Everly Brothers"
    ],
    [
        "¿Sabías que el director de cine Pedro Almodóvar también tuvo su propia banda? Se llamaba...",
        "Los Guardianes", "Almodóvar y McNamara", "Los Satana", "Almodóvar y los Pegamoides"
    ],
    [
        "¿A qué familia de instrumentos pertenece el saxo?",
        "Viento madera", "Viento metal", "Cuerda percutida", "Otros"
    ],
    [
        "¿En qué año se suicidó Kurt Cobain?",
        "1987", "1991", "1991", "2000"
    ],
    [
        "¿Cuál de estos grupos tiene una baterista femenina?",
        "Florence + The Machine", "Arctic Monkeys", "The White Stripes", "Otros"
    ],
    [
        "¿Cuándo nació el rap?",
        "Finales de los 50/principios de los 60",
        "Finales de los 60/principios de los 70",
        "Finales de los 70/principios de los 80",
        "Finales de los 80/principios de los 90"
    ],
    [
        "Un actor de películas de terror puso la voz al videoclip 'Thriller' de Michael Jackson. ¿Quién fue?",
        "Christopher Lee", "Vincent Price", "Mickey Rooney", "Boris Karloff"
    ],
    [
        "¿Cómo se llama el dúo formado por Beyoncé y su marido Jay Z?",
        "The Fierces", "The Knowles", "The Carters", "Otros"
    ]
]
########################### PRESENTACIÓN ###################################
tituloA = "Bienvenido a mi juego de TRIVIA"
tituloB = "en donde pondrás a prueba tus conocimientos"
tituloC = "sobre la música "

imprimirTitulos("bl", tituloA, tituloB, tituloC)
name = input("\nPor favor, dime cuál es tu nombre: ")


limpiar()  # Prueba

########################### INSTRUCCIONES ###################################

insA = f"Muy bien {name}, saldrán en pantalla un total de {total_de_preguntas} preguntas"
insB = "y tu deberás responder con la letra de aquella respuesta que creas correcta"
insC = "presionando finalmente el botón 'enter' para enviarla, si aciertas, "
insD = "ganarás 5 puntos, sino, perderás puntos de forma aleatoria"
insE = "en un rango de 1 a 5 puntos (influirá mucho tu suerte)\n"
insF = "¡Esfuérzate para demostrar todos tus conocimientos!"

imprimirTitulos("bl", insA, insB, insC, insD, insE, insF)
print(
    setColour(
        "\nNota: hay una respuesta secreta que podría ayudarte, intenta probar aleatoriamente a ver si aciertas y ganas muchos puntos extras ;)\n",
        "c"))
input(setColour("\nSi estás listo para jugar, aprieta enter.", "mg"))

limpiar()

########################### CÓDIGO MAIN ########################################
while True:
    puntaje = random.randint(0, 10)
    contraseña_usada = 0  # passUsages
    ruptura = False

    # Mensaje personalizado según el puntaje inicial aleatorio obtenido
    if puntaje == 0:
        print(
            f"Jugarás esta ronda con un puntaje inicial de {puntaje} puntos.\n")
    elif puntaje <= 5:
        print(
            f"Tienes algo de suerte {name}, iniciarás esta ronda con un puntaje inicial de {puntaje} puntos, ¡aprovéchalos!\n"
        )
    else:
        print(
            f"Tienes mucha suerte {name}, iniciarás esta ronda con un increíble puntaje inicial de {puntaje} puntos, ¡sácale provecho!\n"
        )

    # Conteo de suspenso inicial
    time.sleep(1.5)
    print("Prepárate, comenzaremos en: ")
    cuentaRegresiva()

    # Tomo el set de preguntas que se jugarán esta ronda:
    conjuntodePreguntas = random.sample(questions, k=total_de_preguntas)

    # Ejecuto la presentación y respuesta del usuario para dicha respuesta
    numerodePregunta = 0
    for preguntaSeleccionada in conjuntodePreguntas:
        numerodePregunta += 1  # numero de pregunta
        respuestaConjunto = ["", "", "", ""]
        lugaresRestantes = [0, 1, 2, 3]
        posicionVerdadera = None  # Ubicación de la respuesta verdadera luego del mixeo
        verdaderaRespuesta = None

        # Se plantea el orden aleatorio de respuestas (y se guarda la correcta)
        for i in range(1, 5):
            # Primero ubico la posición de la respuesta correcta
            if i == 1:
                posicionVerdadera = random.choice(lugaresRestantes)
                respuestaConjunto[posicionVerdadera] = preguntaSeleccionada[i]
                lugaresRestantes.remove(posicionVerdadera)

            # Luego ubico los demás elementos
            else:
                other = random.choice(lugaresRestantes)
                respuestaConjunto[other] = preguntaSeleccionada[i]
                lugaresRestantes.remove(other)

        # Se establece la condición de respuesta correcta (para comparar con el ingreso del usuario)
        if posicionVerdadera == 0:
            verdaderaRespuesta = "A"
        elif posicionVerdadera == 1:
            verdaderaRespuesta = "B"
        elif posicionVerdadera == 2:
            verdaderaRespuesta = "C"
        elif posicionVerdadera == 3:
            verdaderaRespuesta = "D"

        # Se imprime para la vista de usuario
        print(
            setColour(
                f"Pregunta #{numerodePregunta} :  " +
                preguntaSeleccionada[0] + "\n",
                "mg"))
        print("a) " + respuestaConjunto[0] + "\n")
        print("b) " + respuestaConjunto[1] + "\n")
        print("c) " + respuestaConjunto[2] + "\n")
        print("d) " + respuestaConjunto[3] + "\n")

        # Pedimos respuesta y nos aseguramos que sea una respuesta válida
        reply = input("\nTu respuesta es: ")
        while reply.upper() not in posibles_respuestas:
            reply = input(
                f"\nRespuesta invalida, por favor {name}, ingresa una respuesta adecuada: "
            )

        # Evaluamos la certeza de la respuesta
        if reply.upper() == verdaderaRespuesta:  # SI LA RESPUESTA ES CORRECTA...
            puntaje += 5
            print(
                setColour(
                    f"\nRespuesta correcta {name}, felicidades, ganaste 5 puntos. Tienes un puntaje acumulado de {puntaje} puntos.\n",
                    "g"))

            # Si estamos en la última no hacemos el tiempo
            if preguntaSeleccionada != conjuntodePreguntas[len(conjuntodePreguntas) - 1]:
                time.sleep(1.5)
                print("Prepárate, pasaremos a la siguiente pregunta en: ")

                cuentaRegresiva()
            else:
                print("En unos segundos pasarás a la pantalla final.")
                time.sleep(3)
                limpiar()

        elif reply.upper() == CONTRASEÑA_SECRETA:  # SI SE USÓ LA PALBRA SECRETA...
            if contraseña_usada == 0:
                plusPuntaje = random.randint(35, 78)
                puntaje += plusPuntaje
                print(
                    setColour(
                        f"\n¡Increíble {name}!, veo que conoces la llave secreta del conocimiento, por ello se te han otorgado {plusPuntaje} puntotes, para un total de {puntaje} puntos acumulados. Recuerda no abusar de esto, o podrías tener consecuencias negativas o.o!\n",
                        "y"))
                contraseña_usada += 1
                total_de_preguntas_secretas += 1

                if preguntaSeleccionada != conjuntodePreguntas[len(conjuntodePreguntas) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    cuentaRegresiva(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    limpiar()

            elif contraseña_usada == 1:
                plusPuntaje = random.randint(50, 106)
                puntaje += plusPuntaje
                print(
                    setColour(
                        f"\n¡Sorprendente {name}!, sigues demostrando ser portador del conocimiento absoluto, por ello los dioses te bendicen con {plusPuntaje} puntotes, para un total de {puntaje} puntos acumulados. Sin embargo, te aconsejo no emplearlo más, o podrías desatar un castigo scorístico sobre ti u-ú. \n",
                        "y"))
                contraseña_usada += 1
                total_de_preguntas_secretas += 1

                if preguntaSeleccionada != conjuntodePreguntas[len(conjuntodePreguntas) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    cuentaRegresiva(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    limpiar()
            else:
                plusPuntaje = random.randint(-96, -12)
                puntaje += plusPuntaje
                print(
                    setColour(
                        f"\nOh no, lamentablemente has abusado mucho de este poder, y se te ha penalizado con {plusPuntaje} puntos menos :(, quedándote solo {puntaje} puntos. Te advertí de ello {name}. Te aconsejo no usarlo más y seguir solo con tus conocimientos.\n",
                        "r"))
                contraseña_usada += 1
                total_de_preguntas_secretas += 1

                if preguntaSeleccionada != conjuntodePreguntas[len(conjuntodePreguntas) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    cuentaRegresiva(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    limpiar()

        else:  # SI RESPONDIÓ INCORRECTAMENTE...
            # Si estamos en la última no hacemos el tiempo
            if preguntaSeleccionada != conjuntodePreguntas[len(conjuntodePreguntas) - 1]:
                subPuntaje = random.randint(-5, -1)
                puntaje -= subPuntaje
                print(
                    setColour(
                        f"\nRespuesta incorrecta {name}, tu Puntaje disminuirá en {subPuntaje} puntos, quedando en un total de  {puntaje} puntos.\n",
                        "r"))
                # IMPRIMIR RESPUESTA CORRECTA
                print(
                    f"La respuesta correcta era la letra {verdaderaRespuesta.lower()}) "
                    + respuestaConjunto[posicionVerdadera] +
                    ". Mejor suerte en la siguiente :(.\n")

                input("Presiona cualquier tecla para continuar.\n")

                print("Prepárate, pasaremos a la siguiente pregunta en: ")
                cuentaRegresiva()
            else:
                subPuntaje = random.randint(-5, -1)
                puntaje -= subPuntaje
                print(
                    setColour(
                        f"\nRespuesta incorrecta {name}, has perdido {subPuntaje} puntos. No has podido ganar más :(.\n",
                        "r"))
                print(
                    f"La respuesta correcta era la letra {verdaderaRespuesta.lower()}) "
                    + respuestaConjunto[posicionVerdadera] +
                    ". Presiona cualquier tecla para pasar a la pantalla final.\n"
                )
                input()
                limpiar()

    # Damos terminada la ronda
    print(
        setColour(
            f"La ronda ha terminado {name}, y has logrado obtener un total de {puntaje} puntos.",
            "c"))

    # APOSTAR PARA GANAR O PERDER MÁS PUNTOS
    ganaroPerder = input(
        "\n¡Sin embargo, nos gustaría darte la oportunidad de probar tu suerte e intentar ganar muchos más puntos!... o perderlos cof* cof*. \n\nSi quieres apostar contra nosotros, responde Y, de lo contrario, responde N para quedarte con tus puntos actuales: "
    )
    while True:
        if not (ganaroPerder.upper() == "Y" or ganaroPerder.upper() == "N"):
            ganaroPerder = input(
                f"\nTienes que responde Y o N para poder entenderte correctamente {name}. ¿Deseas probar tu suerte para ganar (cof* o perder cof*) más puntos?: "
            )
        elif ganaroPerder.upper() == "Y":
            print(
                "\n¡Está decidido! El juego será lanzar el dado; Nosotros elegiremos un número y tú otro, y luego el dado sacará aleatoriamente un número (el rango de elección será del 1 al 6), gana el que acierte el número del dado, y repetiremos hasta que suceda. Si nosotros ganamos, tu puntaje se dividirá en 2, pero si tú ganas, tu puntaje será multiplicado por 2!. Aprieta enter para continuar."
            )
            input()

            numerodeusuarioSeleccionado = entrada_numerica(
                name)  # FUERZA AL USUARIO A REGISTRAR UN NUMERO DEL 1 AL 6
            cpuNumberSelect = random.randint(1, 6)  # El valor del cpu
            while True:
                if cpuNumberSelect != numerodeusuarioSeleccionado:
                    break
                else:
                    cpuNumberSelect = random.randint(1, 6)

            print(
                f"\nMi elección es el número {cpuNumberSelect}, tu elección {name} es el número {numerodeusuarioSeleccionado}. Ahora veamos qué sale en el dado, cruza los dedos:"
            )

            dadoSeleccionado = random.randint(1, 6)

            cuentaRegresivaN()

            print(f"\nEl dado ha sacado el número {dadoSeleccionado}.\n")

            if ((dadoSeleccionado == numerodeusuarioSeleccionado)
                    or (dadoSeleccionado == cpuNumberSelect)):
                if dadoSeleccionado == numerodeusuarioSeleccionado:
                    puntaje *= 2
                    print(
                        setColour(
                            f"\nEnhorabuena {name}, has tenido mucha suerte esta vez y tu puntaje se ha multiplicado por 2, quedando en un total de {puntaje} puntos.",
                            "g"))
                    break

                elif dadoSeleccionado == cpuNumberSelect:
                    puntaje /= 2
                    print(
                        setColour(
                            f"\nEs una lástima {name}, no has tenido suerte y tu puntaje se ha reducido a la mitad, quedando en un total de {puntaje} puntos. Mejor suerte la próxima :(",
                            "r"))
                    break

            else:
                while True:
                    print(
                        "\nNinguno de los dos ha acertado, ¡hay que volver a intentarlo!"
                    )
                    numerodeusuarioSeleccionado = entrada_numerica(
                        name
                    )  # FUERZA AL USUARIO A REGISTRAR UN NUMERO DEL 1 AL 6
                    cpuNumberSelect = random.randint(1, 6)  # El valor del cpu
                    while True:
                        if cpuNumberSelect != numerodeusuarioSeleccionado:
                            break
                        else:
                            cpuNumberSelect = random.randint(1, 6)

                    print(
                        f"\nMi elección es el número {cpuNumberSelect}, tu elección {name} es el número {numerodeusuarioSeleccionado}. Ahora veamos qué sale en el dado, cruza los dedos:"
                    )

                    dadoSeleccionado = random.randint(1, 6)

                    cuentaRegresivaN()

                    print(
                        f"\nEl dado ha sacado el número {dadoSeleccionado}.\n")

                    if ((dadoSeleccionado == numerodeusuarioSeleccionado)
                            or (dadoSeleccionado == cpuNumberSelect)):
                        if dadoSeleccionado == numerodeusuarioSeleccionado:
                            puntaje *= 2
                            print(
                                setColour(
                                    f"\nEnhorabuena {name}, has tenido mucha suerte esta vez y tu puntaje se ha multiplicado por 2, quedando en un total de {puntaje} puntos.",
                                    "g"))
                            break

                        elif dadoSeleccionado == cpuNumberSelect:
                            puntaje /= 2
                            print(
                                setColour(
                                    f"\nEs una lástima {name}, no has tenido suerte y tu puntaje se ha reducido a la mitad, quedando en un total de {puntaje} puntos. Mejor suerte la próxima :(",
                                    "r"))
                            break
                break
        elif ganaroPerder.upper() == "N":
            print(
                f"\nEntendemos que hoy te sientes sin suerte {name}, tu puntaje final esta ronda fue de {puntaje} puntos."
            )
            break

    # Preguntamos si quiere volver a jugar hasta que responda adecuadamente

    # Guardamos el puntaje obtenido en esta ronda
    puntaciones_acumuladas.append(puntaje)
    decision = input("\n¿Deseas volver a jugar? Y/N: ")
    while True:

        if not (decision.upper() == "Y" or decision.upper() == "N"):
            decision = input(
                f"Tienes que responde Y o N para poder entenderte correctamente {name}. ¿Deseas volver a jugar?: "
            )
        elif decision.upper() == "Y":
            print("¡Está decidido! Volveremos a jugar, prepárate.")
            cuentaRegresiva()
            rondas += 1
            break
        elif decision.upper() == "N":
            ruptura = True
            break

    # Rompemos el ciclo general
    if ruptura == True:
        break

# Limpiamos pantalla y damos el mensaje de despedida, con el puntaje máximo de los acumulados
limpiar()
maximo_puntaje = max(puntaciones_acumuladas)
puntajeAcumulado = sum(puntaciones_acumuladas)

if contraseña_usada == 0:

    print(
        f"Muchas gracias por jugar {name}, has completado un total de {rondas} rondas con un puntaje máximo de {maximo_puntaje} puntos. Además, el puntaje acumulado de todas las rondas es de {puntajeAcumulado} puntos\n"
    )

    imprimirTitulos("bl", "Esperamos verte pronto por aquí :)")
else:
    print(
        f"Muchas gracias por jugar {name}, has completado un total de {rondas} rondas con un puntaje máximo de {maximo_puntaje} puntos; además, el puntaje acumulado de todas las rondas jugadas es de {puntajeAcumulado}. Sin embargo, has empleado la respuesta secreta un total de {contraseña_usada} veces, asegurate de confiar solo en tus conocimientos la próxima vez ;). \n"
    )

    imprimirTitulos("bl", "Esperamos verte pronto por aquí :)")

input("Aprieta enter para finalizar.")
limpiar()
