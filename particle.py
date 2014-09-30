from vector import Vector

class Particle:
	def __init__(self, color, pos, vel=None, mass=1):
		self.color = color
		self.pos = pos
		self.prev = pos
		self.vel = (Vector(0,0) if vel is None else vel)
		self.force = Vector(0,0)
		self.mass = mass
		self.radius
	
	def __str__(self):
		return "P("+str(self.pos.x)+", "+str(self.pos.y)+")"
	
	def applyForce(self, force):
		self.force = self.force.add(force)
	
	def update(self, time):
		self.prev = self.pos.copy()
		
		accel = self.force.mul(1/self.mass)
		self.force = Vector(0,0)
		self.vel = self.vel.add(accel.mul(time))
		self.pos = self.pos.add(self.vel.mul(time))
		
		