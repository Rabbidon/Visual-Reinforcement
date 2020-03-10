import math

class Planet:

    def __init__(self, canvas, speed, sun, mass, radius, x, y, **kwargs):

        self.x = x
        self.y = y
        self.sun = sun
        self.radius = radius
        self.speed = speed
        self.canvas = canvas
        self.shape = canvas.create_oval(x-radius,y-radius,x+radius,y+radius, **kwargs)
        
        xdist = self.x-self.sun.x
        ydist = self.y-self.sun.y
        self.distance = math.sqrt(xdist**2 + ydist**2)
        self.angle = (1/4 if ydist>0 else 3/4) if xdist==0 else ((1/2 if xdist<0 else 0) + math.atan(ydist/xdist)/(2*math.pi))
        print(self.angle)

    def update(self):

        self.angle=math.modf(self.angle+self.speed)[0]

        print(self.x)

        dx = self.sun.x+self.distance*math.cos(2*math.pi*self.angle)-self.x
        dy = self.sun.y+self.distance*math.sin(2*math.pi*self.angle)-self.y
                      
        self.x+=dx
        self.y+=dy        
        self.canvas.move(self.shape,dx,dy)

        
