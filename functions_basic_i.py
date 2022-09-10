#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) 
# imprime 5


#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# muestra un error, funcion no definida


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# imprime 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# imprime 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# imprime 5 / y luego no imprime nada

#6
def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))
# imprime 3
# imprime 5
# hay un error porque las funciones no retornan nada.



#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# imprime 25 

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# imprime 100
# imprime 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# imprime 7

print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imprime 14

print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imprime 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# imprime 8


#11
b = 500
print(b)

def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# imprime 500
# imprime 500
# imprime 300
# imprime 500



#12
b = 500
print(b)

def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# imprime 500
# imprime 500
# imprime 300
# imprime 500


#13
b = 500
print(b) #1 orden que imprime

def foobar():
    b = 300
    print(b) #3 orden que imprime
    return b
print(b) #2 orden que imprime
b=foobar()
print(b) #4 orden que imprime
# imprime 500
# imprime 500
# imprime 300
# imprime 300


#14
def foo():
    print(1) #1
    bar()
    print(2) #3
def bar():
    print(3) #2
foo()
# imprime 1
# imprime 3
# imprime 2


#15
def foo():
    print(1) #1
    x = bar() # x = 5
    print(x) # 3
    return 10
def bar():
    print(3) #2
    return 5
y = foo() # y = 10
print(y) #4
# imprime 1
# imprime 3
# imprime 5
# imprime 10