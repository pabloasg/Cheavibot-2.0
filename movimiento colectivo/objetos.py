import pygame
import math


NEGRO= (0,0,0)
BLANCO=(255,255,255)

class bot():
    def __init__(self, surface, centro, radio, velocidad, angulo, estado):
        self.surface=surface
        self.centro=centro
        self.radio=radio
        self.velocidad=velocidad
        self.angulo=angulo
        self.estado=estado
    
    def getestado(self):
        return (self.estado)
        
    def modestado(self, nestado):#cambia estado actual por un nuevo estado
        self.estado=nestado
        
    def verestado(self): #verifica que el estado del bot es valido
        if self.estado=='seguidor' or self.estado=='lider':
            pass
        else:
            self.estado='seguidor'
        
    def dibujar(self):
        r=int(self.radio)
        centro=(int(self.centro[0]),int(self.centro[1]))
        pygame.draw.circle(self.surface, BLANCO, centro, r, 3)
        
    def dibujarvel(self):
        r=10#parametro que amplifica el valor de v
        centro=self.centro[0],self.centro[1]
        v=self.velocidad
        a=self.angulo
        c=math.cos(a)
        s=math.sin(a)
        x=centro[0]+v*c*r
        y=centro[1]+v*s*r
        pygame.draw.line(self.surface, (255,0,0), centro, (x,y), 3)
        
    def getpos(self):
        centro=self.centro
        return centro
    
    def getvel(self):
        vel=self.velocidad
        return vel
    def getang(self):
        ang=self.angulo
        if ang > 2*math.pi:
            return ang-2*math.pi
        else:
            return ang
    
    def actvel(self, vp):
        v=1 #corresponde a 1/10 del maximo valor que puede tomar la velocidad 
        vel=self.velocidad
        if vel < vp:
            self.velocidad=vel+v
        elif vel > vp:
            self.velocidad=vel-v
        else:
            self.velocidad=self.velocidad           
        
    def mover(self):
        alpha=self.angulo
        c=math.cos(alpha)
        s=math.sin(alpha)
        vel=self.velocidad
        cx=vel*c+self.centro[0]
        cy=vel*s+self.centro[1]
        cen=(cx,cy)
        self.centro=cen
        
    def rotar(self, dirmov):#0 es direccion anti horaria, 1 es direccion horaria
        paso=math.radians(5)
        if dirmov==0:
            self.angulo=self.angulo-paso
        elif dirmov==1:
            self.angulo=self.angulo+paso
        else:
            self.angulo=self.angulo+paso
            print('se entrego un valor no valido y por defecto se cambio a 1')
            
        
    
    