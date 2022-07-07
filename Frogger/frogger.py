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

#Declaramos las dimensiones de la pantalla del videojuego
g_vars = {}
g_vars['width'] = 416
g_vars['height'] = 416
g_vars['fps'] = 30
g_vars['grid'] = 32
g_vars['window'] = pygame.display.set_mode( [g_vars['width'], g_vars['height']], pygame.HWSURFACE)

#Clase App
class App:

	#Métodos de incicialización
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Frogger")
		
		self.running = None
		self.state = None
		self.frog = None
		self.score = None
		self.lanes = None

		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont('Courier New', 16)

	def init(self):
		self.running = True
		self.state = 'START'
		
		self.frog = Frog(g_vars['width']/2 - g_vars['grid']/2, 12 * g_vars['grid'], g_vars['grid'])
		self.frog.attach(None)
		self.score = Score()

		self.lanes = []
		self.lanes.append( Lane( 1, c=( 50, 192, 122) ) )
		self.lanes.append( Lane( 2, t='log', c=(153, 217, 234), n=2, l=6, spc=350, spd=1.2) )
		self.lanes.append( Lane( 3, t='log', c=(153, 217, 234), n=3, l=2, spc=180, spd=-1.6) )
		self.lanes.append( Lane( 4, t='log', c=(153, 217, 234), n=4, l=2, spc=140, spd=1.6) )
		self.lanes.append( Lane( 5, t='log', c=(153, 217, 234), n=2, l=3, spc=230, spd=-2) )
		self.lanes.append( Lane( 6, c=(50, 192, 122) ) )
		self.lanes.append( Lane( 7, c=(50, 192, 122) ) )
		self.lanes.append( Lane( 8, t='car', c=(195, 195, 195), n=3, l=2, spc=180, spd=-2) )
		self.lanes.append( Lane( 9, t='car', c=(195, 195, 195), n=2, l=4, spc=240, spd=-1) )
		self.lanes.append( Lane( 10, t='car', c=(195, 195, 195), n=4, l=2, spc=130, spd=2.5) )
		self.lanes.append( Lane( 11, t='car', c=(195, 195, 195), n=3, l=3, spc=200, spd=1) )
		self.lanes.append( Lane( 12, c=(50, 192, 122) ) )
