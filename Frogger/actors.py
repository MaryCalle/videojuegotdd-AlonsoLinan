""""
AUTORES:	
		Mary Anne Calle Davies
		Victor Hugo Hinojosa Pinto
		Manuel Rodrigo Ramos Sánchez
		Adriana Raquel Linares Garrafa
		Gustavo Alonso Liñán Salinas
"""

#Librerías a importar
import random
import pygame
from pygame.locals import *


#Clase Rectángulo (forma de todos los objetos)
class Rectangle:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def intersects(self, other):
		left = self.x
		top = self.y
		right = self.x + self.w
		bottom = self.y + self.h

		oleft = other.x
		otop = other.y
		oright = other.x + other.w
		obottom = other.y + other.h

		return not (left >= oright or right <= oleft or top >= obottom or bottom <= otop)

#Clase Lane (Carriles de fondo)
class Lane(Rectangle):

	def __init__(self, y, c=None, n=0, l=0, spc=0, spd=0):
		super(Lane, self).__init__(0, y * g_vars['grid'], g_vars['width'], g_vars['grid'])
		self.type = t
		self.color = c
		self.obstacles = []
		offset = random.uniform(0, 200)
		if self.type == 'car':
			o_color = (128, 128, 128)
		if self.type == 'log':
			o_color = (185, 122, 87)
		for i in range(n):
			self.obstacles.append(Obstacle(offset + spc * i, 
				y * g_vars['grid'], l * g_vars['grid'], g_vars['grid'], spd, o_color))