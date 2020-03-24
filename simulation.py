import tkinter as tk
from tkinter.ttk import *
from sun import Sun
from planet import Planet
from naive_lander import NaiveLander
  
class GraphicalEngine:
    
    def __init__(self, root = None): 


        self.canvas = tk.Canvas(root)
 
        self.canvas.pack(expand = True,fill = "both")

        sun = Sun(engine = self, mass = 1000)
        sun_graphic =  self.canvas.create_oval(sun.x-sun.radius ,sun.y-sun.radius, sun.x+sun.radius, sun.y+sun.radius, fill="yellow")
        planet = Planet(engine = self, sun = sun)
        planet_graphic = self.canvas.create_oval(planet.x-planet.radius ,planet.y-planet.radius, planet.x+planet.radius, planet.y+planet.radius, fill="green")
        lander  = NaiveLander(engine = self, sun = sun, planet = planet, acceleration_cap = 0.5)
        lander_graphic = self.canvas.create_oval(lander.x-lander.radius ,lander.y-lander.radius, lander.x+lander.radius, lander.y+lander.radius, fill="grey")
        self.graphic_dict  = {sun:sun_graphic, planet:planet_graphic, lander:lander_graphic}
        self.update()


    def registerMovement(self, object, dx, dy):

       self.canvas.move(self.graphic_dict[object], dx, dy)
      
    def update(self): 
  
        for object in self.graphic_dict:
            object.update()
  
        self.canvas.after(1000//60, self.update) 
  
if __name__ == "__main__": 
  
    root = tk.Tk()
    root.attributes("-zoomed",True)

    gfg = GraphicalEngine(root)

    root.mainloop() 
