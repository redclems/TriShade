import svgwrite
from math import *
import random

base = 255
nbBit = 8

debutData = 18
finData = 19
sansData = 64
allColor = 65
position = 48

t = 10 #muttiplayer taille des pixel si = 1 la taille d'un pixel = 10/10

blanc = "#FFFFFF"
color = ['#000000', '#FF0000', '#00FF00', '#0000FF']

melange = {('#000000', '#FF0000'): '#eeeeee', ('#000000', '#00FF00'): '#eeeeee', ('000000', '0000FF'): '#eeeeee',
		   ('#FF0000', '#000000'): '#eeeeee', ('#FF0000', '#00FF00'): '#FFFF00', ('FF0000', '0000FF'): '#FF00FF',
		   ('#00FF00', '#000000'): '#eeeeee', ('#00FF00', '#FF0000'): '#FFFF00', ('00FF00', '0000FF'): '#00FFFF',
		   ('#0000FF', '#000000'): '#eeeeee', ('#0000FF', '#FF0000'): '#00FFFF', ('0000FF', '00FF00'): '#00FFFF'
}


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
	if(v > 255):
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
	t1Noir = [3]
	t2Noir = [2]
	t3Noir = [1]
	t4Noir = [0]

	def foundColorTriangle(v, color, draw, triangle, tab, makeWhite=False):
		"""
		return draw avec l'ajout d'un triangle de la bonne couleur
		"""

		v1 = v%16
		v2 = v//16


		e = 0
		notFound = True
		while notFound and e < len(color):
			v1InTab = v1-4*e in tab
			v2InTab = v2-4*e in tab
			if(v1InTab and v2InTab):	
				draw.add(draw.polygon(triangle, fill=melange[e][e], stroke="#000000", opacity=0.5))
				notFound = False
				draw.add(draw.polygon(triangle, fill=color[e], stroke="#000000", opacity=0.5))
				notFound = False

			elif(v1InTab):
				draw.add(draw.polygon(triangle, fill=color[e], stroke="#000000", opacity=1))
				notFound = False
			elif(v2InTab):
				draw.add(draw.polygon(triangle, fill=color[e], stroke="#000000", opacity=1))
				notFound = False
			e+=1

		if(notFound and makeWhite):
			print(v, tab)
			draw.add(draw.polygon(triangle, fill=blanc, stroke="#000000", opacity=0.5))
		return draw


	draw = foundColorTriangle(v, color, draw, trans_triangle1, t1Noir)
	draw = foundColorTriangle(v, color, draw, trans_triangle2, t2Noir)
	draw = foundColorTriangle(v, color, draw, trans_triangle3, t3Noir)
	draw = foundColorTriangle(v, color, draw, trans_triangle4, t4Noir)

	return draw



def drawTriShade(matrice, name="trishade"):
	"""
	dessine une un TriShade grace a une matrice d'entier de 0 a 64 non comprit
	"""
	n = len(matrice[0])
	m = len(matrice)


	triShade = svgwrite.Drawing('TriShade/' + name + "_16_255.svg", size=(10*t*n,10*t*m))

	for j in range(m):
		for i in range(n):
			triShade = makePixel(j, i, matrice[j][i], triShade)

	triShade.save()

"""
m = random.randint(3, 15)#ligne
n = random.randint(3, 15)#colonne

matrice = [[random.randint(0, 15) for j in range(m)] for i in range(n)]
print(matrice)

drawTriShade(matrice, name="trishade.svg")
"""


triShade = svgwrite.Drawing('TriShade/triShade.svg', size=(10*t*16,10*t*16))

#genere tout les pixel possible du protocol
value = 0
for j in range(0,16):
	for i in range(16):
		triShade = makePixel(j, i, value, triShade)
		value+=1

triShade.save()
