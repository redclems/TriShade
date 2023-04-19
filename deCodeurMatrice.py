import generatedSVG.SVG4CouleurBase16 as generateur#il faut que se soit le même que utiliser pour encoder

def decoderMatrice(matrice, str=True):
	erreur = ""
	nbLigne = None
	nbColone = None
	nbBit = None
	res = list()

	if(matrice[0][0] == generateur.position or matrice[-1][-1] == generateur.position):#verifier si les position iu haut et dus bas sont bien la
		pass
	else:
		erreur = "manque la position"

	if((matrice[0][1] >= 0 or matrice[0][1] < generateur.base) and (matrice[-1][-2] >= 0 or matrice[-1][-2] < generateur.base)): #verifier nbligne du bas et du haut bien present et entre 0 et la base
		if(matrice[-1][-2] == matrice[0][1]):#si les deux sont similaire
			nbLigne = matrice[0][1]
	else:
		erreur = "manque le nombre de ligne"
	
	if((matrice[0][2] >= 0 or matrice[0][2] < generateur.base) and (matrice[-1][-3] >= 0 or matrice[-1][-3] < generateur.base)): #verifier nbColonne du bas et du haut bien present et entre 0 et la base
		if(matrice[-1][-3] == matrice[0][2]):#si les deux sont similaire
			nbColone = matrice[0][2]
	else:
		erreur = "manque le nombre de colone"

	if(matrice[0][3] == generateur.allColor and matrice[-1][-4] == generateur.allColor):
		pass
	else:
		erreur = "manque le bit de toute les couleur"

	if(matrice[0][4] == generateur.nbBit and matrice[-1][-5] == generateur.nbBit):
		if(matrice[-1][-5] == matrice[0][4]):
			nbBit = matrice[0][4]
	else: 
		erreur = "manque la nombre de bit"

	if(matrice[0][5] == generateur.debutData and matrice[-1][-6] == generateur.debutData):
		pass
	else:
		erreur = "manque le debut data"

	matrice1 = list()
	if(matrice[1][0] == generateur.debutData):
		for ligne in range(1, nbLigne+1):
			for colone in range(0, nbColone):
				if(matrice[ligne][colone] != generateur.debutData and matrice[ligne][colone] != generateur.finData and matrice[ligne][colone] != generateur.sansData):
					if(matrice[ligne][colone] >= 0 and matrice[ligne][colone] < generateur.base):
						matrice1.append(matrice[ligne][colone])
					else:
						erreur = "valeur or base matrice1" + str(ligne) + " - " + str(colone)
	else:
		print("mauvais debut matrice1")
	print(matrice1)

	matrice2 = list()
	if(matrice[nbLigne][nbColone] == generateur.debutData):
		for colone in range(nbColone, nbColone*2, 1):
			for ligne in range(nbLigne, 0, -1):
				if(matrice[ligne][colone] != generateur.debutData and matrice[ligne][colone] != generateur.finData and matrice[ligne][colone] != generateur.sansData):
					if(matrice[ligne][colone] >= 0 and matrice[ligne][colone] < generateur.base):
						matrice2.append(matrice[ligne][colone])
					else:
						erreur = "valeur or base matrice2" + str(ligne) + " - " + str(colone)
	else:
		 print("mauvais debut matrice2")
	print(matrice2)
	#print("liste Identique sans Harmingue : ", verif_listes_identiques(matrice1, matrice2))

	verifMat1 = verrifierEtCoorigerHarmming(matrice1)
	print(verifMat1)
	verifMat2 = verrifierEtCoorigerHarmming(matrice2)
	print(verifMat2)

	if(verif_listes_identiques(verifMat1, verifMat2)):
		#print("liste Identique : ", True)
		valNegativ = False
		for valeur in verifMat1:
			if(valeur < 0):
				valNegativ = True
				break
		if not valNegativ:
			res = verifMat1
		else:
			erreur = "il y a une erreur similaire dans les deux matrice imposible a corriger"
	elif(len(verifMat1) <= 0):
		valNegativ = False
		for valeur in verifMat2:
			if(valeur < 0):
				valNegativ = True
				break
		if not valNegativ:
			res = verifMat2
		else:
			erreur = "perte de donner imposible a récuperer"
	elif(len(verifMat2) <= 0):
		valNegativ = False
		for valeur in verifMat1:
			if(valeur < 0):
				valNegativ = True
				break
		if not valNegativ:
			res = verifMat1
		else:
			erreur = "perte de donner imposible a récuperer"
	else:
		u = 0
		while u < len(verifMat1):
			if(verifMat1[u] > -1):
				if(verifMat1[u] == verifMat2[u]):
					res.append(verifMat1[u])
				else:
					erreur = "la corection de Harmingue n'a pas detecter l'erreur et n'a pas mit -1"
			elif(verifMat2[u] <= -1):
				print(u, " -> ", verifMat2[u] )
				erreur = "perte de donner imposible a récuperer"
			else:
				res.append(verifMat2[u])
			u+=1

	if(erreur != ""):
		return "erreur : " + erreur
	else:
		if(str):
			return ''.join([chr(res[t]*16+res[t+1]) for t in range(0, len(res), 2)])
		else:
			return res


def verif_listes_identiques(liste1, liste2):
    if len(liste1) != len(liste2):
        return False
    for i in range(len(liste1)):
        if liste1[i] != liste2[i]:
            return False
    return True

def verrifierEtCoorigerHarmming(listeMatrice):
	sommeNB = 0
	sommeNBPonderee = 0
	result = list()
	n = 1
	i = 0
	while i < len(listeMatrice):
		sommeNB += listeMatrice[i]
		sommeNBPonderee += listeMatrice[i] * n
		if(n%3 == 0 and i+3 < len(listeMatrice)):
			sommeNBCal = listeMatrice[i+1]*3 + listeMatrice[i+2]
			sommeNBPondereeCal = listeMatrice[i+3]*6 + listeMatrice[i+4]

			if(sommeNBCal == sommeNB):
				if(sommeNBPondereeCal == sommeNBPonderee):
					result.append(listeMatrice[i-2])
					result.append(listeMatrice[i-1])
					result.append(listeMatrice[i])
				else:
					#print(i, " - incorrect sommeNBPonderee")
					result.append(-2)
					result.append(-2)
					result.append(-2)
			else:
				#print("correction", i)
				if(sommeNBPondereeCal != sommeNBPonderee):
					#result.append(-3)
					#result.append(-3)
					#result.append(-3)
					
					diference = sommeNB - sommeNBCal
					positionDiference = int((sommeNBPonderee - sommeNBPondereeCal)/4)
					print(diference)
					print(positionDiference)
					iCorecteur = 3
					t = 1
					while iCorecteur >= 1:
						if(t == positionDiference):
							print(t)
							print(listeMatrice[i - (iCorecteur-1)] - diference)
							result.append(listeMatrice[i - (iCorecteur-1)] - diference)
						else:
							result.append(listeMatrice[i - (iCorecteur-1)])
						iCorecteur-=1
						t+=1
					
				else:
					#print(i, " -  fausse Harmingue")
					result.append(-4)
					result.append(-4)
					result.append(-4)

			i+=4
			n=0
			sommeNB = 0
			sommeNBPonderee = 0
		elif(i+3 >= len(listeMatrice)):
			if(i<len(listeMatrice)):
				result.append(listeMatrice[i])
		n+=1
		i+=1
	return result
