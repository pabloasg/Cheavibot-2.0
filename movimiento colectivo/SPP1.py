import pygame
import math
import os
import random
import objetos
from pickle import NONE #se ocupa para poder usar la variable NONE

'''
este codigo prueba el while true, osea mueve los bots de manera continua
'''

#ajusta la aparicion de la ventana en las coordenadas x,y
x = 600
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

Lx=800
Ly=800
os=200 #offset total
pygame.init()
dimensiones = [Lx+os, Ly+os]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('SPP pruebas basicas')
NEGRO= (0,0,0)
BLANCO=(255,255,255)

#generar posiciones aleatorias de los bots
L=200 #separacion bots
nx=int(Lx/L)
ny=int(Ly/L)

s=100
random.seed(s)
font = pygame.font.SysFont("arial", 20)
    

centro=[]
for i in range (0,nx):
    for j in range (0,ny):
        x=os+L*i+int(random.uniform(-50,50))
        y=os+L*j+int(random.uniform(-50,50))
        c=x,y
        centro.append(c)
        
colr=[]
for i in range(0,3*len(centro)):
    a=int(random.uniform(0,255))
    colr.append(a)

#crea una lista con las magnitudes de las velocidades       
v=[]
for i in range(0,len(centro)):
    vel=random.uniform(0,10)
    v.append(vel)
    
alpha=[]
for i in range(0,len(centro)):
    ang=random.uniform(0,2*math.pi)
    alpha.append(ang)
        
print(len(centro), len(v), len(alpha), 'largo de las listas')
print(centro)
r=50

B=[]
for i in range(0, len(centro)):
    aux=objetos.bot(pantalla, centro[i], r, v[i], alpha[i], 'seguidor')
    B.append(aux)

while True:  

    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            break
        
            
        
        
    '''
    #codigo para comprobar radios de interaccion de los bots  
    ct=10  
    for k in range (0, len(centro)):
        pygame.draw.circle(pantalla, BLANCO, centro[k], r, 1)
        pygame.draw.circle(pantalla, (0,255,0), centro[k], 3*r, 1)
        pygame.draw.circle(pantalla, (colr[3*k],colr[3*k+1],colr[3*k+2]), centro[k], 6*r, 1)
        x=centro[k][0]+ct*v[k]*math.cos(alpha[k])
        y=centro[k][1]+ct*v[k]*math.sin(alpha[k])
        pygame.draw.line(pantalla, BLANCO, centro[k], (x,y), 1)
    '''
    
    #codigo para obtener los centros de los bots   
    A=[]
    for i in range(0,len(B)):
        cen=B[i].getpos()
        A.append(cen)
        
    #bloque que indica los vecinos, en otras palabras cuales bots interactuan entre si
    vecinos=[]
    for i in range(0,len(B)):
        x1=A[i][0]
        y1=A[i][1]
        j=0
        for j in range(0,len(B)):
            x2=A[j][0]
            y2=A[j][1]
            distancia=math.sqrt((x1-x2)**2+(y1-y2)**2)
            #codigo para verificar distancias e indices
            #print('valor i', i, 'valor j',j)
            #print('coordenadas i', A[i][0], A[i][1], 'coordenadas j', A[j][0], A[j][1])
            #print('distancia i, j', distancia, 'distancia de interaccion', dl)
            if distancia < 6*r:
                if i==j:
                    pass
                #elif j>i-1:
                    #   pass
                else:
                    nn=[i,j, distancia]
                    vecinos.append(nn) 
    
    #print('lista de los vecinos',vecinos)  
    
    #este bloque reordena los vecinos en una lista que muestra el indice del bot seguido de que vecinos tiene
    #adicionalmente se crea una lista similar que en lugar de contener el indice contiene la distancia, la cual sirve para detectar las colisiones
    lvecinos=[]
    lvecinosD=[]
    for i in range(0,len(B)):
        
        b=[]
        bD=[]
        #print('vecinos i',vecinos[i][0],'vecinos j', vecinos[j][0])
        for j in range(0,len(vecinos)):
            
            if vecinos[j][0]==i:
                a=vecinos[j][1]
                aD=vecinos[j][2]
                b.append(a)
                bD.append(aD)
            else:
                pass
        c=[i,b]
        lvecinos.append(c)
        cD=[i,bD]
        lvecinosD.append(cD)
        b=[]
        c=[]
        a=NONE
        bD=[]
        cD=[]
        aD=NONE
    print(lvecinos)
    print(lvecinosD)
    a=NONE
    
    #print('lista de distancia por bot', lvecinosD)
   
    #codigo para anotar numero de bot     
    for i in range(0,len(B)):
        text = font.render(str(i), True, (0, 128, 0))
        pantalla.blit(text,(A[i][0], A[i][1]))
    
        
   
    
    #codigo para dibujar los bots 
    for i in range (0, len(B)):
        B[i].dibujar()
        B[i].dibujarvel()
        B[i].rotar(1)
        B[i].mover()
            
    
    
    
    pygame.display.flip()
    my_clock.tick(10) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()