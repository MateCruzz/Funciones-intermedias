matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

print("\n--- Actualizar valores en diccionarios y listas ---")
print("\n--- Actualizar el valor de la matriz ---")
matriz[1][0] = 6
print(matriz)

print("\n--- Cambiar el nombre del Cantante ---")
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes[0])

print("\n--- Cambia “Cancún” por “Monterrey” ---")
ciudades["México"][2] = "Monterrey"
print(ciudades)

print("\n--- Cambia el valor de “latitud” ---")
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

print("\n--- Iterar a través de una lista de diccionarios ---")
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for i in range(len(lista)):
        print(f"nombre: {lista[i]['nombre']}, pais: {lista[i]['pais']}")
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes) 


print("\n--- Obtener valores de una lista de diccionarios ---")

def iterarDiccionario2(llave, lista):
    for i in range(len(lista)):
        print(lista[i][llave])
iterarDiccionario2('nombre', cantantes)
iterarDiccionario2('pais', cantantes)

print("\n--- Iterar a través de un diccionario con valores de lista ---")

def imprimirInformacion(diccionario):
    for key in diccionario:
        print(f"{len(diccionario[key])} {key.upper()}")
        for i in range(len(diccionario[key])):
            print(diccionario[key][i])
    


costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)