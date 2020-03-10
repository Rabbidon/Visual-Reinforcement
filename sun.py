class Sun:

    def __init__(self, canvas, mass, radius, x, y, **kwargs):

       self.x = x
       self.y = y
       self.radius = radius
       self.canvas = canvas
       self.shape = canvas.create_oval(x-radius,y-radius,x+radius,y+radius, **kwargs)

    def update(self):
        
        pass

    

    
        
