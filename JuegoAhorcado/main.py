from funciones import*

def main():
  palabra = seleccionarPalabra()
  alfabeto = 'a b c d e f g h i j k l m n ñ o p q r s t u v w x y z'
  jugada = ["-"]*len(palabra)
  
  for turno in range(5):
    print(f"\nTurno: {turno+1}")
    print("-" * 20)
    #Imprimir alfabeto y jugada
    imprimirActualizacion(alfabeto, jugada)
    #Entrada usuario
    letra = entradaUsuario()
    #Actualizarjugada y alfabeto
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
  
    # imprimir actualizacion
    imprimirActualizacion(alfabeto, jugada)
    # preguntar al usuario si desea adivinar o no la palabra
    check = input("desea adivinar la palabra? (s/n):")
    if check.lower() == "s":
      suposicion = input("Introduzca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
    
      if success:
        print("+" * 20)
        print("SIUUU GANOOO")
        print("+" * 20)
        break
      else:
        print("+" * 20)
        print("la suposicion es incorrecta")
        print("+" * 20)
  
    if turno == 4:
      print("-" * 20)
      print("=( AHORCADOOO NOOOO")
      print("-" * 20)
      
      
if __name__=="__main__":
  main()