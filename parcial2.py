
#1.Desarrollar un programa que determine si en una lista no existen elementos repetidos.
lista = [1, 2, 3, 4, 5, 6, 6]
def ejercicio1():
    vistos = []  
    for i in lista:
        if i in vistos:   
            print("Hay elementos repetidos")
            return
        vistos.append(i)  
    print("No hay elementos repetidos")

#2.Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con 2 o mas vocales. 
#Si en la cadena existe debe imprimirla y si no existe imprime no existe
lista = ["hola", "uno", "dos", "tres"]
def ejercicio2():
    for palabra in lista:
        contador = (
            palabra.count("a") + palabra.count("e") +
            palabra.count("i") + palabra.count("o") +
            palabra.count("u") + palabra.count("A") +
            palabra.count("E") + palabra.count("I") +
            palabra.count("O") + palabra.count("U")
        )
        if contador >= 2:
            print("La palabra con 2 o más vocales es:", palabra)
            return
    print("No existe")

#3.Desarrollar un programa que dada 2 listas determine que elementos tiene la primera lista que no tenga la segunda lista 
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 6]
def ejrcicio3():
    resultado = []
    for elemento in lista1:
        if elemento not in lista2:
            resultado.append(elemento)
    return resultado

print("Elementos que están en la primera lista y no en la segunda:", ejrcicio3())

#4.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales 
def ejercicio4():
  n = int(input("Ingrese la cantidad de números: "))
  numeros = []

  for i in range(n):
      valor = float(input(f"Ingrese el número: "))
      numeros.append(valor)

  promedio = sum(numeros) / n
  print("El promedio es:", promedio)

def main():
     ejercicio1()
     ejercicio2()
     ejrcicio3()
     ejercicio4()
if __name__== __name__:
    main()
 
