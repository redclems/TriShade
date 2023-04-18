import svgwrite
from math import *
import random

base = 255
nbBit = 8

pixel = True #pixeliser le dessin pour reduireau minimun la place

debutData = 18
finData = 19
sansData = 64
allColor = 65
position = 48

t = 10 #muttiplayer taille des pixel si = 1 la taille d'un pixel = 10/10

blanc = "#FFFFFF"
color = ['#777777', '#770000', '#007700', '#000077']

melange = {('#777777', '#777777'): '#000000', ('#777777', '#770000'): '#FF0000', ('#777777', '#007700'): '#00FF00', ('#777777', '#000077'): '#0000FF',
		   ('#770000', '#777777'): '#FF0000', ('#770000', '#770000'): '#FF7777', ('#770000', '#007700'): '#FFFF00', ('#770000', '#000077'): '#FF00FF',
		   ('#007700', '#777777'): '#00FF00', ('#007700', '#770000'): '#FFFF00', ('#007700', '#007700'): '#77FF77', ('#007700', '#000077'): '#00FFFF',
		   ('#000077', '#777777'): '#0000FF', ('#000077', '#770000'): '#00FFFF', ('#000077', '#007700'): '#00FFFF', ('#000077', '#000077'): '#7777FF'
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
	if(pixel):
		triangle1 = [(1*t,0*t), (3*t,0*t), (3*t,2*t), (2*t,2*t), (2*t,1*t), (1*t,1*t)]
		triangle2 = [(0*t,0*t), (1*t,0*t), (1*t,1*t), (2*t,1*t), (2*t,2*t), (0*t,2*t)]
		triangle3 = [(0*t,2*t), (2*t,2*t), (2*t,3*t), (1*t,3*t), (1*t,4*t), (0*t,4*t)]
		triangle4 = [(2*t,2*t), (3*t,2*t), (3*t,4*t), (1*t,4*t), (1*t,3*t), (2*t,3*t)]
		trans=(3*t)*ligne, (4*t)*colone
	else:
		trans=(10*t)*ligne, (10*t)*colone
		triangle1 = [(0*t,0*t) ,(10*t,5*t),(10*t,0*t) ]
		triangle2 = [(0*t,0*t) ,(0*t,5*t) ,(10*t,5*t) ]
		triangle3 = [(0*t,5*t) ,(0*t,10*t),(10*t,5*t) ]
		triangle4 = [(0*t,10*t),(10*t,5*t),(10*t,10*t)]

	#translate le triangle a la position souhaiter
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


		notFound = True

		e1 = 0
		c1 = None
		notFound1 = True
		while notFound1 and e1 < len(color):
			if(v1-4*e1 in tab):
				c1 = color[e1]
				notFound1 = False
			else:
				e1+=1

		e2 = 0
		c2 = None
		notFound2 = True
		while notFound2 and e2 < len(color):
			if(v2-4*e2 in tab):
				c2 = color[e2]
				notFound2 = False
			else:
				e2+=1

		if(notFound1 == False and notFound2 == False):

			draw.add(draw.polygon(triangle, fill=melange[(color[e1],color[e2])], stroke="#000000", opacity=1))
		elif(notFound1 == False):
			draw.add(draw.polygon(triangle, fill=color[e1], stroke="#000000", opacity=1))
		elif(notFound2 == False):
			draw.add(draw.polygon(triangle, fill=color[e2], stroke="#000000", opacity=1))
		elif(makeWhite):
			draw.add(draw.polygon(triangle, fill=blanc, stroke="#000000", opacity=1))


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
