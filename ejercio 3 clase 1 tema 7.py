#Comprobante ultimo ejercicio clase 1

def LeerProducto ():
    return input("Ingrese Nombre de Producto: ")
def LeerPrecio ():
    return float(input("Ingrese Precio del producto :"))
def LeerCantidad ():
    return int(input("Ingrese cantidad del producto :"))
def ImporteCompra (precio,cantidad):
    return precio*cantidad
def IGV (icompra):
    return icompra*0.18
def totalPagar (icompra,impuesto):
    return icompra+impuesto

#Programa Prinpical

producto = LeerProducto()
precio = LeerPrecio()
cantidad = LeerCantidad()
icompra = ImporteCompra (precio,cantidad)
impuesto = IGV (icompra)
tp = totalPagar (icompra,impuesto)

print()
print("----------------------------------")
print("Comprobante de Pago")
print("----------------------------------")
print("Producto          : ",producto)
print("Precio            : ",precio)
print("Cantidad          : ",cantidad)
print("----------------------------------")
print("Importe de Compra : ",icompra)
print("IGV               : ",impuesto)
print("Total a pagar     : ",tp)
