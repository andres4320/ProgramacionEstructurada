'''1.la palabra a adivinar se debe seleccionar aleatoriamente del listado disponible en un archivo de texto
2.el jugador tendrá 5 turnos para adivinar la palabra(independientemente si en cada jugada tieneun acierto o un fallo).
3. en cada turno tenemos lo siguiente:
-se debe mostrar al usuario la actualización de cada palabra que esta intentando adivinar y el alfabeto actualizado (es decir; las letras que se encuentren disponibles)
-se debe preguntar al usuario si desea adivinar la palabra y de ser así realizar la verificación correspondiente.
4. El juego termina:
cuando se completa los 5 turnos y el jugador no acierta
-El jugador decide adivinar la palabra y acierta.'''


import random

alfabeto="a b c d e f g h i j k l m n ñ o p q r s t u v x y z"

#Función para escoger una palabra random
def seleccionarPalabra(): # se escribe def y el nombre de la función
  lineas = open("frutas_verduras.txt").readlines()   #instrucciones-abre todas las lineas del archivo y se van guardando en esa variable
  palabra = random.choice(lineas).rstrip() #retorno de esa funcion-selecciona sin datos extraños
  return palabra

palabra = seleccionarPalabra() # - no se identa porque no pertenece a la función , se llama 
#print(palabra) #imprimo la variable para que funcione



# Funcion entrada del teclado
def entradaUsuario():
  letra = input("Introduzca una letra: ")
  return letra.lower()

#letra= entradaUsuario()
#print (letra)



#Funcion actualizar jugada
def actualizarJugada(palabra, letra, jugada): #quiere decir que esos parametros esten dentro de la funcion
  n_letras = len(palabra)

  
  for i in range (0,n_letras):
    if palabra [i] == letra:
      jugada[i] = letra
    
  return jugada  #retornar una variable que se llame jugada # el len permite mirar el tamaño de un string contraccion de longitud.

  
#palabra = seleccionarPalabra()
#letra =entradaUsuario()
#jugada =["_"]*len(palabra)
#jugada = actualizarJugada (palabra, letra, jugada)
#print(jugada)



def  actualizarAlfabeto(letra,alfabeto): #vamos a actualizar el alfabeto, quiere decir si yo seleccione la a en el deben quedar las otras
  alfabeto = alfabeto.replace(letra," ")


  return alfabeto
  #nos salimos de la función y le colocamos:

#alfabeto = actualizarAlfabeto(letra, alfabeto)
#print(alfabeto)

# Imprimir resultado de la jugada en pantalla 
def imprimirActualizacion(alfabeto, jugada):
  print(f"Jugada: {jugada}") # la f toma lo de las llaves, lo evalua para luego imprimir
  print(f"letras disponibles: {alfabeto}")
#imprimirActualizacion(alfabeto, jugada)



#vamos a verificar jugada, comparar la que hizo el usuario con la palabra que esta adivinando
def verificarJugada(suposicion, palabra):
  success = False # varaiable donde puede retornar 2 valores verdaderoo falso 
  if suposicion == palabra:
    success = True
  return success 
#success = verificarJugada("tomate", palabra)
#print(success)