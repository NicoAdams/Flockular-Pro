import math
import pygame
from random import random
import sys
from field import Field
from particle import Particle
from vector import Vector, fromPolar

"""Initializes and runs the game
"""

pygame.init()

pygame.display.set_caption("Flockular Pro - A Particle Interaction Engine")
clock = pygame.time.Clock()

# The bounds of the screen 
maxPt = Vector(600,600)
center = maxPt.mul(.5)

# Opens window
windowSurface = pygame.display.set_mode(maxPt.tuple())

# Configures the field
f = Field()
f.assocColor(0, pygame.Color(255,0,0))
f.assocColor(1, pygame.Color(0,255,0))
f.assocColor(2, pygame.Color(0,0,255))
f.setForce(1)
for colorKey in range(3):
	f.setForceRule(colorKey, colorKey, -.5) # Self
	f.setForceRule(colorKey, (colorKey+1)%3, .5) # Other 1
	f.setForceRule(colorKey, (colorKey+2)%3, .5) # Other 2

# Some basic particle setups

def particleRandom():
	particles = 150
	for i in range(particles):
		x = random() * maxPt.x
		y = random() * maxPt.y
		color = int(random() * 3)
		p = Particle(color, Vector(x, y))
		f.addParticle(p)

def particleCircle():
	angleSteps = 3 * 20
	radius = 200
	center = maxPt.mul(.5)
	for i in range(angleSteps):
		angle = float(i) / angleSteps * 2 * math.pi
		pos = fromPolar(radius, angle).add(center)
		vel = fromPolar(1, 3*angle)
		color = i % 3
		p = Particle(color, pos, vel=vel)
		f.addParticle(p)

# Adds particles
particleRandom()

# FPS
fps = 25

while True:
	# Handles events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() # Closes window
			sys.exit() # Exits program
		if event.type == pygame.MOUSEBUTTONDOWN:
			pass # Have fun with this
	
	# Draws and updates
	f.update(1)
	clock.tick(fps) # Pauses execution as needed to attain desired fps
	f.draw(windowSurface)
	pygame.display.update() # Updates the display
	