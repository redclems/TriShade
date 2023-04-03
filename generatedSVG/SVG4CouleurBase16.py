import svgwrite
from math import *
import random

base = 16
nbBit = 4

debutData = 18
finData = 19
sansData = 64
allColor = 65
position = 48

t = 10 #muttiplayer taille des pixel si = 1 la taille d'un pixel = 10/10

blanc = "#FFFFFF"
color = ['#000000', '#FF0000', '#00FF00', '#0000FF']

def translater(input, vecTrans):
    x,y=input
    tx,ty=vecTrans
    return ((tx+x, ty+y))


def makePixel(colone, ligne, v, draw):
	"""
	Créer un pixel composer de 4 triangle quand la ligne = 0 et la colone = 0 le pixel se trouve en haut a gauche
	v    -> corepond a un entier qui qui permet de definire la valeur stocker dans le pixel.
	draw -> corepond au svgwrite.Drawing créer par une librairy 
	"""
	if(v > 65):
		print("wrong value")
		return draw

	#créer le pixel
	triangle1 = [(0*t,0*t) ,(10*t,5*t),(10*t,0*t) ]
	triangle2 = [(0*t,0*t) ,(0*t,5*t) ,(10*t,5*t) ]
	triangle3 = [(0*t,5*t) ,(0*t,10*t),(10*t,5*t) ]
	triangle4 = [(0*t,10*t),(10*t,5*t),(10*t,10*t)]

	#translate le triangle a la position souhaiter
	trans=(10*t)*ligne, (10*t)*colone
	trans_triangle1 = [translater(sommet, trans) for sommet in triangle1]
	trans_triangle2 = [translater(sommet, trans) for sommet in triangle2]
	trans_triangle3 = [translater(sommet, trans) for sommet in triangle3]
	trans_triangle4 = [translater(sommet, trans) for sommet in triangle4]

	#coder les couleur en fonction de la valeur
	t1Noir = [3,16,19,33,34,35,49,50]
	t2Noir = [2,16,18,32,33,35,49,51]
	t3Noir = [1,16,18,32,33,34,48,50]
	t4Noir = [0,16,19,32,34,35,48,51]

	def foundColorTriangle(v, color, draw, triangle, tab):
		"""
		return draw avec l'ajout d'un triangle de la bonne couleur
		"""
		e = 0
		notFound = True
		while notFound and e < len(color):
			if(v-4*e in tab):
				draw.add(draw.polygon(triangle, fill=color[e], stroke="#000000", opacity=1))
				notFound = False
			e+=1
		#if(notFound):
		#	draw.add(draw.polygon(triangle, fill=blanc, stroke="#000000", opacity=1))

		return draw
	if(v < 64):
		draw = foundColorTriangle(v, color, draw, trans_triangle1, t1Noir)
		draw = foundColorTriangle(v, color, draw, trans_triangle2, t2Noir)
		draw = foundColorTriangle(v, color, draw, trans_triangle3, t3Noir)
		draw = foundColorTriangle(v, color, draw, trans_triangle4, t4Noir)
	elif(v == 64):
		#draw.add(draw.polygon(trans_triangle1, fill="#FFFFFF", stroke="#000000", opacity=1))
		#draw.add(draw.polygon(trans_triangle2, fill="#FFFFFF", stroke="#000000", opacity=1))
		#draw.add(draw.polygon(trans_triangle3, fill="#FFFFFF", stroke="#000000", opacity=1))
		#draw.add(draw.polygon(trans_triangle4, fill="#FFFFFF", stroke="#000000", opacity=1))
		pass
	elif(v == 65):
		draw.add(draw.polygon(trans_triangle1, fill=color[0], stroke="#000000", opacity=1))
		draw.add(draw.polygon(trans_triangle2, fill=color[1], stroke="#000000", opacity=1))
		draw.add(draw.polygon(trans_triangle3, fill=color[2], stroke="#000000", opacity=1))
		draw.add(draw.polygon(trans_triangle4, fill=color[3], stroke="#000000", opacity=1))		

	return draw



def drawTriShade(matrice, name="trishade"):
	"""
	dessine une un TriShade grace a une matrice d'entier de 0 a 64 non comprit
	"""
	n = len(matrice[0])
	m = len(matrice)


	triShade = svgwrite.Drawing('TriShade/' + name + "_16_4.svg", size=(10*t*n,10*t*m))

	for j in range(m):
		for i in range(n):
			triShade = makePixel(j, i, matrice[j][i], triShade)

	triShade.save()

"""
m = random.randint(3, 15)#ligne
n = random.randint(3, 15)#colonne

matrice = [[random.randint(0, 15) for j in range(m)] for i in range(n)]
#print(matrice)

drawTriShade(matrice, name="trishade16.svg")
"""


triShade = svgwrite.Drawing('TriShade/triShade16.svg', size=(10*t*16,10*t*4))

#genere tout les pixel possible du protocol
value = 0
for j in range(0,4):
	for i in range(16):
		triShade = makePixel(j, i, value, triShade)
		value+=1

triShade.save()