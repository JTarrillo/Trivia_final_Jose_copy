import random  # Importamos la librería random
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
print (YELLOW+"Empecemos!!"+RESET )
time.sleep(2)
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (BLUE+"Bienvenido a mi trivia sobre música"+RESET)
print (BLUE+"Pondremos a prueba tus conocimientos"+RESET)
print (BLUE+"Tienes", puntaje, "puntos"+RESET)

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input (MAGENTA+"Ingresa tu nombre: "+RESET)
print ("Iniciando...")
time.sleep(2)

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print (CYAN+"\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")


# Pregunta 1
  print ("1) Una de estas obras no es de Mozart. ¿Cuál de ellas?")
  print ("a) La flauta mágica")
  print ("b) La falsa jardinera")
  print ("c) Las bodas de Fígaro")
  print ("d) Madama Butterfly")
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")


  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  print (MAGENTA+"Tu respuesta es..."+RESET)
  time.sleep(2)
  if respuesta_1 == "a":
    print (RED+"Totalmente incorrecta! ..."+RESET)
    puntaje = puntaje / 2
  elif respuesta_1 == "b":
    print (RED+"...Incorrecta"+RESET)
    puntaje = puntaje + 5
  elif respuesta_1 == "c":
    print (RED+"Incorrecta! ..."+RESET)
    puntaje = puntaje - 5
  else:
    print (GREEN+"Correcta! ..."+RESET)
    puntaje = puntaje * 2
  
  
  
  print(nombre, "llevas", puntaje, "puntos")


  # Pregunta 2
  print ("\n2) ¿Cuál de los siguientes cantantes pronunció la frase 'Prefiero que me odien por lo que soy a que me admiren por lo que nunca seré'?")
  print ("a) Freddie Mercury")
  print ("b) John Lennon")
  print ("c) Jim Morrison")
  print ("d) Kurt Cobain")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  print (MAGENTA+"Tu respuesta es..."+RESET)
  time.sleep(2)
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    print (RED+"Incorrecta!", nombre, "Su famosa frase es No me importa morir mañana. He vivido, en toda la extensión de la palabra"+RESET)
    puntaje = puntaje / 2
  elif respuesta_2 == "b":
    print (RED+"Incorrecta!", nombre, "Su famosa frase es Cada persona es el reflejo de la música que escucha"+RESET)
    puntaje = puntaje + 5
  elif respuesta_2 == "c":
    print (RED+"Incorrecta!", nombre, "Su famosa frase es Soy el hombre de la libertad, esa es toda la fortuna que tengo"+RESET)
    puntaje = puntaje - 5
  else:
    puntaje += 10
    print (GREEN+"Correcta!", nombre, "!"+RESET)
  
  print(nombre, "llevas", puntaje, "puntos")
  
  # Pregunta 3
  print ("\n3) ¿Cuál de estas canciones no es del grupo inmortal Queen?")
  print ("a) Don't Stop me now")
  print ("b) Tie your mother down")
  print ("c) These are the days of our lives")
  print ("d) Where are we now")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  print (MAGENTA+"Tu respuesta es..."+RESET)
  time.sleep(2)
  if respuesta_3 == "a":
    print (RED+"Totalmente incorrecta! ..."+RESET)
    puntaje = puntaje / 2
  elif respuesta_3 == "b":
    print (RED+"...Incorrecta"+RESET)
    puntaje = puntaje + 5
  elif respuesta_3 == "c":
    print (RED+"Incorrecta! ..."+RESET)
    puntaje = puntaje - 5
  else:
    print (GREEN+"Correcta! ..."+RESET)
    puntaje = puntaje * 2
  
  # Pregunta 3
  print ("\n4) ¿Cuál fue la primera grabación de Rock and Roll?")
  print ("a) Una canción de Elvis Presley")
  print ("b) Una canción de Little Richard")
  print ("c) Una canción de Bill Haley")
  print ("d) Una canción de Chuck Berry")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input("\nTu respuesta: ")
  
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  print (MAGENTA+"Tu respuesta es..."+RESET)
  time.sleep(2)
  if respuesta_4 == "a":
    print (RED+"Totalmente incorrecta! ..."+RESET)
    puntaje = puntaje / 2
  elif respuesta_4 == "b":
    print (RED+"...Incorrecta"+RESET)
    puntaje = puntaje + 5
  elif respuesta_4 == "c":
    print (RED+"Incorrecta! ..."+RESET)
    puntaje = puntaje - 5
  else:
    print (GREEN+"Correcta! ..."+RESET)
    puntaje = puntaje * 2
  
  
  print ("Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")
  
 
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
