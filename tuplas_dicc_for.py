"""
Uso de diccionarios con tuplas
Requerimiento: Dado el diccionario {("a", 1): "Letra A",
 ("b", 2): "Letra B"}, imprime el valor
asociado a la clave ("a", 1).
Salida esperada:

Letra A
"""

diccionario = {
    ("a", 1):
    "Letra z",
    ("b", 2):
    "Letra B"
}

new_1 = diccionario.items()

new_3 = list(new_1)

nueva = new_3[0:1]

for i in nueva:
    print(i[1])