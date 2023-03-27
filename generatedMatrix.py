def trouverTailleMatrice(n):
    """
    trouve avec le nombre de donner la taille de la matrice
    """
    v1 = [2,2]
    v2 = [2,2]

    while v1[0]*v1[1] < n and v2[0]*v2[1] < n :

        v1[1] = v1[1] + 1 if v1[1] <= v1[0] else v1[1]
        v1[0] = v1[0] + 1 if v1[1] >  v1[0] else v1[0]

        v2[1] = v2[1] + 1 if v2[1] <= v2[0]+1 else v2[1]
        v2[0] = v2[0] + 1 if v2[1] >  v2[0]+1 else v2[0]

    if(v2[0]*v2[1] >= n and v1[0]*v1[1] >= n):
        if(v2[0]*v2[1] <= v1[0]*v1[1]):
            return v2
        else:
            return v1
    elif(v1[0]*v1[1] >= n):
        return v1
    elif(v2[0]*v2[1] >= n):
        return v2
    else:
        print("erreur imposible !")
        return 2, 2

def hexa_for_each_char(message):
    """
    transforme un message en une liste contenants les valeurs hexadecimal
    de chaque char du message. et place le debut et la fin
    """
    valHexaDual = [format(ord(c), "x") for c in message]

    return [18] + [int(x, 16) for dual in valHexaDual for x in dual] + [19]


def matrice(message):

    codeHexa = hexa_for_each_char(message)
    nbData = len(codeHexa)
    print(codeHexa)

    ligne, colone = trouverTailleMatrice(nbData)

    matrice = [[64 for _ in range(colone)] for _ in range(ligne)]

    value = 0
    for j in range(ligne):
        for i in range(colone):
            if(value < len(codeHexa)):
                matrice[j][i] = codeHexa[value]
                value+=1

            
    return matrice

mat = matrice("Salut a tous c'est daVide l'afar@ge pokemon")
print(mat)

import generatedSVG

generatedSVG.drawTriShade(mat, "Salut a tous c'est daVide l'afar@ge pokemon")
