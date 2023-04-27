import generatedSVG.SVG4CouleurBase16 as generateur


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

def hexa_for_each_char(message, base=16, harmming=False):
    """
    transforme un message en une liste contenants les valeurs hexadecimal
    de chaque char du message. et place le debut et la fin
    """
    valHexaDual = [format(ord(c), "x") for c in message]
    res = list()
    res.append(generateur.debutData)

    #harmming variable
    n = 1
    sommeNB = 0
    sommeNBPonderee = 0
    if(base == 16):
        for dual in valHexaDual:
            for x in dual:
                res.append(int(x, 16))
                if(harmming):
                    sommeNB += int(x, 16)
                    sommeNBPonderee += int(x, 16) * n
                    if(n%3 == 0):
                        res.append(sommeNB//3)
                        res.append(sommeNB%3)
                        res.append(sommeNBPonderee//6)
                        res.append(sommeNBPonderee%6)
                        n = 0
                        sommeNB = 0
                        sommeNBPonderee = 0
                    n+=1


    elif(base == 255):
        for x in valHexaDual:
            res.append(int(x, 16))
            if(harmming):
                sommeNB += int(x, 16)
                sommeNBPonderee += int(x, 16) * n
                if(n%3 == 0):
                    res.append(sommeNB//3)
                    res.append(sommeNB%3)
                    res.append(sommeNBPonderee//6)
                    res.append(sommeNBPonderee%6)
                    n = 0
                    sommeNB = 0
                    sommeNBPonderee = 0
                n+=1
    else:
        print("Wrong base")
    res.append(generateur.finData)
    return res


def matriceNormal(ligne, colone, codeHexa, nbData):
    """
    generer la matrice avec les donnée mais sans systeme de
    verification ni dupication de donner
    """
    matrice = [[generateur.sansData for _ in range(colone)] for _ in range(ligne)]

    value = 0
    for j in range(ligne):
        for i in range(colone):
            if(value < len(codeHexa)):
                matrice[j][i] = codeHexa[value]
                value+=1
    return matrice

def matriceReverce(ligne, colone, codeHexa, nbData):
    """
    generer la matrice avec les donnée mais sans systeme de
    verification ni dupication de donner. sauf qu'elle tourner 
    de 90° en sens anti horaire et la meme nombre de ligne et de colone
    que la matrice normal
    """
    matrice = [[generateur.sansData for _ in range(colone)] for _ in range(ligne)]

    nbCaseVide = ligne*colone-nbData

    for t in range(nbCaseVide):
        codeHexa.insert(0, generateur.sansData)

    value = ligne-1
    for j in range(ligne):
        for i in range(colone):
            if(value < len(codeHexa)):
                matrice[j][i] = codeHexa[value]
                value+=ligne
        value = ligne-(1+j+1)
    return matrice

def matrice2DInfoTriShade(ligne, colone, codeHexa, nbData):
    """
    créer la bande en bas du QRCode qui verifie l'integriter des donnée
    """
    nbCaseVide = ligne*colone-nbData
    coloneCorriger = colone*2
    if(coloneCorriger < 5):
        print("trop Petit")
        return [generateur.sansData] * ((coloneCorriger*2))
    elif(coloneCorriger >= 5):
        return [generateur.position] + [ligne] + [colone] + [nbCaseVide] + [generateur.allColor] + [generateur.sansData] * ((coloneCorriger)-5) 

def makeMatrice(message, harmming=True):
    codeHexa = hexa_for_each_char(message, generateur.base, harmming)
    nbData = len(codeHexa)

    ligne, colone = trouverTailleMatrice(nbData)
    if(colone <= 3):
        colone = 3


    if(ligne >= 16 or colone >= 16):
        print("matrixOutOfRange")
        return None
    else:
        matN = matriceNormal(ligne, colone, codeHexa, nbData)

        matR = matriceReverce(ligne, colone, codeHexa, nbData)

        matV = matrice2DInfoTriShade(ligne, colone, codeHexa, nbData)


        combined_matrix = [row1 + row2 for row1, row2 in zip(matN, matR)]

        combined_matrix.insert(0, matV)
        combined_matrix.append(matV[::-1])

        #print(message, combined_matrix)

        return combined_matrix


mat = makeMatrice("ABCE")
generateur.drawTriShade(mat, "ABC")

