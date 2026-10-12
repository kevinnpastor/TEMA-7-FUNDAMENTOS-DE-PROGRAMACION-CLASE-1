#Ejercio tema 7:1 (Modulo funcion def)
#esta funcion vuelve sin valor
#nececita un invocado
def miMensaje ():
    print("------------------------")
    print("Hola Bienvenida a IDAT")
    print("------------------------")
    print("Soy tu Docente")
    print("Curso Fundamentos de programacion")
    print("---------------------------------")

miMensaje()
print()
print()

#Funcion con retorno de valor (+ unidos)

def miMensajee():
    return "----------------------------\n" + \
           "Hola bienvenido a IDAT\n" + \
           "Soy tu docente de IDAT\n" + \
           "Curos de Fundamentos de programacion\n" + \
           "----------------------------"
#Como invocarlo  con return
recepcion= miMensajee()
print(recepcion)

