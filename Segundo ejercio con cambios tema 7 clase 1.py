#Ejericico 2(cambios)
#uso de parametros en las funciones:
#Son varibales asociadas a una funcion que son los parametros
def primerValor():
    return  float(input("Ingrese Primer valor: "))
def SegundoValor():
    return float(input("Ingrese segundo valor: "))

def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    return a/b

#Pograma principal solo funcionan si tienen un programa principal
x = primerValor()
y=  SegundoValor()
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
