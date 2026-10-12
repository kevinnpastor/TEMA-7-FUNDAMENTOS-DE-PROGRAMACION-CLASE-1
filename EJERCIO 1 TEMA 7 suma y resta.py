#Ejericico 2
#uso de parametros en las funciones:
#Son varibales asociadas a una funcion que son los parametros

def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    return a/b

#Pograma principal solo funcionan si tienen un programa principal
x = float(input("Ingrese Primer valor: "))
y= float(input("Ingrese segundo valor: "))
s = suma(x, y)
r = resta(x, y)
m = multiplicacion(x, y)
d = division(x, y)
print("------------------------------")
print("Operaciones basicas:")
print("------------------------------")
print("Primer valor      :",x)
print("Segundo valor      :",y)
print("------------------------------")
print("Suma             :",s)
print("Resta             :",r)
print("Multiplicacion            :",m)
print("Division             :",d)
print("------------------------------")
