from vector import Vector, fromPolar
from particle import Particle
from math import floor
import pygame

class Field:
	def __init__(self):
		self.particles = []
		self.colors = {}
		self.rules = {}
		self.force = 0
	
	def addParticle(self, particle):
		self.particles.append(particle)
	
	def assocColor(self, key, color):
		self.colors[key] = color
	
	def setForceRule(self, color1, color2, force):
		l = [color1, color2]
		ruleKey = tuple(l)
		self.colors[ruleKey] = force
		
	def setForce(self, force):
		# An overall force field strength factor
		self.force = force
	
	def _getColorRule(self, ruleKey):
		if ruleKey not in self.colors:
			return 0
		return self.colors[ruleKey]
	
	def _getForce(self, p1, p2):
		distVector = p1.pos.sub(p2.pos)
		dist = distVector.len()
		angle = distVector.angle()
		
		# Reduces force by the inverse of distance
		distanceFactor = 0
		if dist != 0:
			distanceFactor = self.force / dist
		
		# Retrieves the color rule
		colorList = [p1.color, p2.color]
		colorRuleKey = tuple(colorList)
		colorForce = self._getColorRule(colorRuleKey)
		
		# Calculates force vector
		force = self.force * distanceFactor * colorForce
		forceVector = fromPolar(force, angle)
		return forceVector
	
	def update(self, time):
		# Applies force
		for p1 in self.particles:
			for p2 in self.particles:
				if p1 is not p2:
					p1.applyForce(self._getForce(p1, p2))
		
		# Updates particles
		for p in self.particles:
			p.update(time)
	
	def draw(self, surface):
		for p in self.particles:
			pygame.draw.line( \
				surface, \
				self.colors[p.color], \
				p.pos.tuple(), \
				p.prev.tuple(), \
				1)
