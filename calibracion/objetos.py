import pygame
import math

BLANCO=(255,255,255)

class rectangulo:
    def __init__(self, surface, x, y, w, h): #(x=posicion x, y= posicion y, w=width, h=heigth)
        self.surface=surface
        self.x=x
        self.y=y
        self.w=w
        self.h=h
                
        
    def dibujar(self):
        xr=self.x
        yr=self.y
        wr=self.w
        hr=self.h
        pygame.draw.rect(self.surface, BLANCO, (xr,yr,wr,hr), 0)
        
    def getdat(self):
        return (self.x, self.y, self.w, self.h)
        
    def modificarx(self, xp):
        self.x=self.x+xp
        
    def modificary(self, yp):
        self.y=self.y+yp
        
    def modificarw(self, wp):
        self.w=self.w+wp
    
    def modificarh(self, hp):
        self.h=self.h+hp
    