import svgwrite
from math import *
import random

t = 10 #muttiplayer taille des pixel si = 1 la taille d'un pixel = 10/10

blanc = '#FFFFFF'
noir  = '#000000'
rouge = '#FF0000'
vert  = '#00FF00'
bleu  = '#0000FF'


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
	print(v)
	if(v > 64):
		print("wrong value")
		return draw

	triangle1 = [(0*t,0*t) ,(10*t,5*t),(10*t,0*t) ]
	triangle2 = [(0*t,0*t) ,(0*t,5*t) ,(10*t,5*t) ]
	triangle3 = [(0*t,5*t) ,(0*t,10*t),(10*t,5*t) ]
	triangle4 = [(0*t,10*t),(10*t,5*t),(10*t,10*t)]

	trans=(10*t)*ligne, (10*t)*colone
	trans_triangle1 = [translater(sommet, trans) for sommet in triangle1]
	trans_triangle2 = [translater(sommet, trans) for sommet in triangle2]
	trans_triangle3 = [translater(sommet, trans) for sommet in triangle3]
	trans_triangle4 = [translater(sommet, trans) for sommet in triangle4]

	t1Noir = [3,16,19,33,34,35,49,50]
	t2Noir = [2,16,18,32,33,35,49,51]
	t3Noir = [1,16,18,32,33,34,48,50]
	t4Noir = [0,16,19,32,34,35,48,51]


	if(v in t1Noir):
		draw.add(draw.polygon(trans_triangle1, fill=noir, stroke="#000000", opacity=1))
	elif(v-4 in t1Noir):
		draw.add(draw.polygon(trans_triangle1, fill=rouge, stroke="#000000", opacity=1))
	elif(v-8 in t1Noir):
		draw.add(draw.polygon(trans_triangle1, fill=vert, stroke="#000000", opacity=1))
	elif(v-12 in t1Noir):
		draw.add(draw.polygon(trans_triangle1, fill=bleu, stroke="#000000", opacity=1))
	else:
		draw.add(draw.polygon(trans_triangle1, fill=blanc, stroke="#000000", opacity=1))

	if(v in t2Noir):
		draw.add(draw.polygon(trans_triangle2, fill=noir, stroke="#000000", opacity=1))
	elif(v-4 in t2Noir):
		draw.add(draw.polygon(trans_triangle2, fill=rouge, stroke="#000000", opacity=1))
	elif(v-8 in t2Noir):
		draw.add(draw.polygon(trans_triangle2, fill=vert, stroke="#000000", opacity=1))
	elif(v-12 in t2Noir):
		draw.add(draw.polygon(trans_triangle2, fill=bleu, stroke="#000000", opacity=1))
	else:
		draw.add(draw.polygon(trans_triangle2, fill=blanc, stroke="#000000", opacity=1))

	if(v in t3Noir):
		draw.add(draw.polygon(trans_triangle3, fill=noir, stroke="#000000", opacity=1))
	elif(v-4 in t3Noir):
		draw.add(draw.polygon(trans_triangle3, fill=rouge, stroke="#000000", opacity=1))
	elif(v-8 in t3Noir):
		draw.add(draw.polygon(trans_triangle3, fill=vert, stroke="#000000", opacity=1))
	elif(v-12 in t3Noir):
		draw.add(draw.polygon(trans_triangle3, fill=bleu, stroke="#000000", opacity=1))
	else:
		draw.add(draw.polygon(trans_triangle3, fill=blanc, stroke="#000000", opacity=1))

	if(v in t4Noir):
		draw.add(draw.polygon(trans_triangle4, fill=noir, stroke="#000000", opacity=1))
	elif(v-4 in t4Noir):
		draw.add(draw.polygon(trans_triangle4, fill=rouge, stroke="#000000", opacity=1))
	elif(v-8 in t4Noir):
		draw.add(draw.polygon(trans_triangle4, fill=vert, stroke="#000000", opacity=1))
	elif(v-12 in t4Noir):
		draw.add(draw.polygon(trans_triangle4, fill=bleu, stroke="#000000", opacity=1))
	else:
		draw.add(draw.polygon(trans_triangle4, fill=blanc, stroke="#000000", opacity=1))

	return draw




triShade = svgwrite.Drawing('TriShade/triShade.svg', size=(10*t*16,10*t*8))
value = 0
for j in range(0,8,2):
	for i in range(16):
		triShade = makePixel(j, i, value,triShade)
		value+=1


triShade.save()
