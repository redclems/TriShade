def hexa_for_each_char(message):
    list_hex = []
    for lettre in message:
        list_hex.append(format(ord(lettre), "x"))
    return list_hex

def matrice(list_hexa):
    # TODO
    pass
hexa_for_each_char("On vient pas de la street ?")
