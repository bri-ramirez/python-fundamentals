
#Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
from multiprocessing.sharedctypes import Value


def countdown(num):
    numList = []
    
    # el segundo argumento es -1 para que incluya el cero en la lista
    # el tercer argumento es -1 para que vaya hacia atrás de uno en uno
    for i in range(num, -1, -1): 
        numList.append(i)

    return numList

print(countdown(5))



#Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
def printAndReturn(list): #recibimos como parametro una lista
    print(list[0]) # imprimimos el primer elemento
    return list[1]# retornamos el segundo elemento

x = printAndReturn([1,2]) # ejecuto la funcion y le envio el listado
print(x)



#Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
def firstSumLength(list):
    return list[0] + len(list)

x = firstSumLength([1,2,3,4,5])
print(x)


#Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
def greaterThanSecond(list):
    # contamos si la cantidad de elemntos es menor a 2
    if len(list) < 2:
        return False

    x = list[1]

    newList = []
    for item in list:
        if item > x:
            newList.append(item)
    # imprimiendo la cantidad de newList
    print(len(newList))
    return newList

x = greaterThanSecond([5,2,3,2,1,4])
print(x)
x = greaterThanSecond([3])
print(x)


#Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
def lengthAndValue(len,val):

    newList = []
    for i in range(0, len):
        newList.append(val)
    return newList

x = lengthAndValue(4,7)
print(x)

x = lengthAndValue(6,2)
print(x)