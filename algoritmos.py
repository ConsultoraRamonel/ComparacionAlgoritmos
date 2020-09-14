# este programa  tiene la intencion de
from math import ceil


# funcion para cargar los datos de la empresa
def cargarDatos(filename):
    f = open(filename)
    datos = f.readlines()
    ids = []
    compras = []
    for d in datos:
        dato = d.replace("\n", "").split(",")
        i = int(dato[0])
        c = int(dato[1])
        ids.append(i)
        compras.append(c)
    return ids, compras


# el objetivo de este algoritmo, es encontrar a un cliente especifico
# entre la lista de mas de 10 millones de clientes
def algoritmo1(clienteID, data):
    clientesID, compras = data
    i = 0
    longitud = len(clientesID)
    while i < longitud:
        cliente = clientesID[i]
        if cliente == clienteID:
            return compras[i]
        i += 1


# el objetivo de este algoritmo, es encontrar a un cliente
# especifico entre la lista de mas de 10 millones de clientes
def algoritmo2(clienteID, data):
    clientesID, compras = data
    aumento = int(len(clientesID) / 2)
    pos = aumento
    while aumento:
        aumento = ceil(aumento / 2)
        cid = clientesID[pos]
        if cid == clienteID:
            return cid
        elif cid < clienteID:
            pos += aumento
        elif cid > clienteID:
            pos -= aumento
