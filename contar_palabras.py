def contar_palabras(palabras):
    palabras = palabras.split(" ")
    dict = {}
    for palabra in palabras:
        if palabra in dict:
            dict[palabra] += 1
        else:
            dict[palabra] = 1
    return dict


