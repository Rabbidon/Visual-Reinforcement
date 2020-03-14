import math

class NaiveLander:

    def __init__(self, canvas, planet, sun, acceleration_cap = 1, radius=10, x=960, y=300, mass = 0.001, **kwargs):

        self.x = x
        self.y = y
        self.sun = sun
        self.planet=planet
        self.radius = radius
        self.canvas = canvas
        self.shape = canvas.create_oval(x-radius,y-radius,x+radius,y+radius, **kwargs)
        self.acceleration_cap = acceleration_cap

        self.dx = 0
        self.dy = 0

    def update(self):

        dx=self.dx
        dy=self.dy

        xdist_planet = self.planet.x-self.x
        ydist_planet = self.planet.y-self.y
        distance_planet = math.sqrt(xdist_planet**2 + ydist_planet**2)

        if distance_planet!=0:
            dx+=(xdist_planet/distance_planet)*(self.acceleration_cap + self.planet.mass/(distance_planet**2))
            dy+=(ydist_planet/distance_planet)*(self.acceleration_cap + self.planet.mass/(distance_planet**2))

        xdist_sun = self.sun.x-self.x
        ydist_sun = self.sun.y-self.y
        distance_sun = math.sqrt(xdist_sun**2+ydist_sun**2)

        if distance_sun!=0:
            dx+=(xdist_sun/distance_sun)* self.sun.mass/(distance_sun**2)
            dy+=(ydist_sun/distance_sun)*self.sun.mass/(distance_sun**2)

        self.dx=dx
        self.dy=dy

        self.x+=dx
        self.y+=dy

        print(dy)
        
        self.canvas.move(self.shape,dx,dy)
