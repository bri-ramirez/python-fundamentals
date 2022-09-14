#Nota: Evita nombrar las variables y parámetros con palabras claves de clase como int, str, list y dict.#

#Actualizar valores en diccionarios y listas

# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
# En el directorio_deportes, cambia "Messi" por "Andrés".
# Cambia el valor 20 en z a 30.

from unicodedata import name


x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes[0]['last_name'] = 'Bryant'

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes['fútbol'][0] = 'Andrés'


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)

#Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
def iterateDictionary(some_list):
    for d in some_list:
        print("first_name -", d["first_name"] + ", last_name -", d["last_name"])


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(estudiantes) 


# #Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)


def printInfo(some_dict):
    for clave in some_dict:
        # contamos la cantidad de elementos que tiene la lista
        largo_lista = len(some_dict[clave])

        print(largo_lista, clave.upper())
        #print(some_dict[clave]) #imprime las listas

        for item in some_dict[clave]:
            print(item)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)