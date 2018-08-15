import math
import pygame


NEGRO=(0,0,0)
BLANCO=(255,255,255)

class fig():
    def __init__(self, surface, origen, largo, ancho):
        self.surface=surface
        self.origen=origen
        self.largo=largo
        self.ancho=ancho
        
    def dibujar(self):
        origen=self.origen
        rect=(origen[0], origen[1], self.largo, self.ancho)
        pygame.draw.rect(self.surface, BLANCO, rect, 1)
        
        
class circulo(fig):
    def __init__(self, surface, origen, origenseed, radioseed):
        self.surface=surface
        self.origen=origen
        self.origenseed=origenseed
        self.radioseed=radioseed
       
        
        
    def circulo(self):
        or2=self.origen
        or1=self.origenseed
        r=self.radioseed
        centro=or2[0], or2[1]
        radio=int(math.sqrt((or2[0]-or1[0])**2+(or2[1]-or1[1])**2)-r*2)
        return centro, radio
        
        
    def dibujarcir(self):
        datosc=circulo.circulo(self)
        centro=int(datosc[0][0]), int(datosc[0][1])
        r=int(datosc[1])
        pygame.draw.circle(self.surface, BLANCO, centro, r, 1)
        
    def compC(self, x, y, r): #x, y representan el centro del objeto a comparar
        datosc=circulo.circulo(self)
        centro=datosc[0]
        r=datosc[1]
        distancia2=(x-centro[0])**2+(y-centro[1])**2
        r2=(r)**2
        if distancia2 <r2:
            return True
        else:
            return False
           
        
class estrella5(fig):
    def __init__(self, surface, origen, largo, ancho, escala):
        self.surface=surface
        self.origen=origen
        self.largo=largo
        self.ancho=ancho
        self.escala=escala
        
    def datos(self):
        origen=self.origen
        l=self.largo
        centro=origen[0]+l/2, origen[1]+l/2
        r0=l/5
        r1=r0/2
        r2=r1/2
        return centro, r0, r1, r2
    
    def dibujarS(self):
        origen=self.origen
        rec=[origen[0], origen[1], self.largo, self.ancho]
        pygame.draw.rect(self.surface, BLANCO, rec, 1)
    
    def dibstar5(self):
        datos=estrella5.datos(self)
        centro=int(datos[0][0]), int(datos[0][1])
        r0=(datos[1])
        r1=(datos[2])
        r2=(datos[3])
        #d0=0
        d1=(r0+r1)
        d2=(r0+2*r1+r2)
        pygame.draw.circle(self.surface, BLANCO, centro, int(r0), 2)
        #pygame.draw.circle(self.surface, BLANCO, (centro[0],centro[1]-int(r0+r1)), int(r1), 2)
        #pygame.draw.circle(self.surface, BLANCO, (centro[0],centro[1]-int(r0+2*r1+r2)), int(r2), 2)
        puntos=[]
        for i in range(0,5):
            ang=2*math.pi/5
            fi=-math.pi/2
            x1=d1*math.cos(ang*i+fi)
            y1=d1*math.sin(ang*i+fi)
            x2=d2*math.cos(ang*i+fi)
            y2=d2*math.sin(ang*i+fi)
            pygame.draw.circle(self.surface, (255,0,0), (centro[0]+int(x1),centro[1]+int(y1)), int(r1), 2)
            pygame.draw.circle(self.surface, (0,0,255), (centro[0]+int(x2),centro[1]+int(y2)), int(r2), 2)
            aux=(centro[0]+x2, centro[1]+y2)
            puntos.append(aux)
        #codigo para comprobar que la figura esta bien representada por los circulos
        pygame.draw.line(self.surface, (0,255,0), puntos[0], puntos[2], 1)
        pygame.draw.line(self.surface, (0,255,0), puntos[2], puntos[4], 1)
        pygame.draw.line(self.surface, (0,255,0), puntos[4], puntos[1], 1)
        pygame.draw.line(self.surface, (0,255,0), puntos[1], puntos[3], 1)
        pygame.draw.line(self.surface, (0,255,0), puntos[3], puntos[0], 1)
        
    def datostar5(self):
        ls=[]
        datos=estrella5.datos(self)
        e0=(datos[0][0], datos[0][1], datos[1])
        d1=(datos[1]+datos[2])
        d2=(datos[1]+2*datos[2]+datos[3])
        ls.append(e0)
        for i in range(0,5):
            ang=2*math.pi/5
            fi=-math.pi/2
            x1=datos[0][0]+d1*math.cos(ang*i+fi)
            y1=datos[0][1]+d1*math.sin(ang*i+fi)
            aux=x1, y1, datos[2]
            ls.append(aux)
        for i in range(0,5):
            ang=2*math.pi/5
            fi=-math.pi/2
            x1=datos[0][0]+d2*math.cos(ang*i+fi)
            y1=datos[0][1]+d2*math.sin(ang*i+fi)
            aux=x1, y1, datos[3]
            ls.append(aux)     
        return ls   
    
    def comp(self, x, y, r): #x, y representan el centro del objeto a comparar
        ls=estrella5.datostar5(self)
        lcomp=[]
        for i in range(0, len(ls)):
            distancia2=(x-ls[i][0])**2+(y-ls[i][1])**2
            r2=(ls[i][2])**2
            if distancia2 <r2:
                lcomp.append(True)
            else:
                lcomp.append(False)
        v=True in lcomp
        if v==True:
            return True
        else:
            return False       
        

        
class Ctest():
    def __init__(self, surface,pos, radio):
        self.surface=surface
        self.pos=pos
        self.radio=radio
        
    def dibujar(self):
        centro=self.pos
        pygame.draw.circle(self.surface, (0,255,255), (int(centro[0]), int(centro[1])), int(self.radio), 0)
        
    def actualizarpos(self, x, y):
        aux=x,y
        self.pos=aux
        
    def getpos(self):
        aux=self.pos, self.radio
        return aux
    
    
    
    
    



        