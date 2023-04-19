import generatedMatrix as gen
import deCodeurMatrice as decodeur

import random

def tester(msg, nb_fausses_valeurs=0, affichage=False, indices_fausses_valeurs=None):
	mat = gen.makeMatrice(msg)

	mat = brouillerMatrice(mat, nb_fausses_valeurs, indices_fausses_valeurs)

	msgDecod = decodeur.decoderMatrice(mat)

	if(msgDecod == msg):
		if(affichage):
			print("decodage OK")
			print(msgDecod)
			print(msg)
		return True
	else:
		if(affichage):
			print("mauvais decodag")
			print(msgDecod)
			print(msg)
		return False



def brouillerMatrice(matrice, nb_fausses_valeurs=1, indices_fausses_valeurs=None):
	nb_total_elements = len(matrice) * len(matrice[0])

	# Indice des éléments à remplacer par des fausses valeurs
	if(indices_fausses_valeurs == None):
		indices_fausses_valeurs = random.sample(range(nb_total_elements), nb_fausses_valeurs)

	# Remplacement des éléments aux indices choisis par des fausses valeurs
	for i in indices_fausses_valeurs:
	    ligne = i // len(matrice[0])
	    colonne = i % len(matrice[0])
	    valeur = 10#random.randint(0, 64)
	    print(ligne, colonne, "- ", valeur)
	    matrice[ligne][colonne] = valeur

	return matrice

msg = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
print(tester(msg, 6, True, [33,34,35,36,37]))
