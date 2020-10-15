import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma():
    result = 2 + 4
    return result


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""


# start-->
def multiplicacion():
    result = 2 * 4 * 5
    return result


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""


# start-->
def sumarLista():
    result = 0
    for contador in numerosLista:
        result += contador
    return result


numerosLista = [2, 5, 4, 6, 9, 12]


"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    result = "https://github.com/sofiadenice/Pre-Parcial.git"
    return result
