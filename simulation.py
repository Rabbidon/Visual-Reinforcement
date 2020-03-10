import tkinter as tk
from tkinter.ttk import *
from sun import Sun
from planet import Planet
  
class Engine: 
    def __init__(self, root = None): 


        self.canvas = tk.Canvas(root)

        self.canvas.pack(expand = True,fill = "both")
  
        self.objects = []

        sun = Sun(self.canvas, 1,100,960,540,fill="yellow")
        self.objects.append(sun)
        self.objects.append(Planet(self.canvas, 0.01, sun, 1, 20,500,200,fill="green"))
        
        self.update() 
      
    def update(self): 
  
        for object in self.objects:
            object.update()
  
        self.canvas.after(1000//60, self.update) 
  
if __name__ == "__main__": 
  
    root = tk.Tk()
    root.attributes("-zoomed",True)

    gfg = Engine(root)
      
    # Infnite loop breaks only by interrupt 
    root.mainloop() 
