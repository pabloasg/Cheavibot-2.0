import math
import pygame
import figuras
import os
import bot
import random


#ajusta la aparicion de la ventana en las coordenadas x,y
x = 200
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

Lx=1000
Ly=1000
pygame.init()
dimensiones = [Lx, Ly]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('pruebas para la formacion de figuras')
NEGRO= (0,0,0)
BLANCO=(255,255,255)

font = pygame.font.SysFont("arial", 20)


f1=figuras.circulo(pantalla, (100,100), 800, 800)
f2=figuras.estrella5(pantalla, (100,100), 800,800, 1)
t1=figuras.Ctest(pantalla,(500,500), 50)

L=200 
nx=int(Lx/L)
ny=int(Ly/L)

B=[]
l=20
r=50
n2=20
nx=int(math.sqrt(n2))
ny=int(n2/nx)

'''
#arreglo ordenado de bots en reticula cuadrada
for i in range(0, ny):
    for j in range(0, nx):
        x=2*r*i+200
        y=2*r*j+200
        vel=random.uniform(0,10)
        alpha=random.uniform(0,2*math.pi)
        b1=bot.coin(pantalla, (x,y), r, vel, alpha, False, '1', 'fijo', 0)
        B.append(b1)
   
'''

#arreglo ordenado de bots en reticula hexagonal
dx=2*r
dy=int(2*r*math.sqrt(3)/2)
for i in range(0,ny):
    for j in range(0,nx):
        if i%2==0:
            coordenadas=(200+int(dx/2)+dx*j , 200+int(dy/2)+dy*i)
            vel=random.uniform(0,10)
            alpha=random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, False, '*', 'detenido', 0)
            B.append(b1)
        else:
            #coordenadas=(200+int(dx)+dx*j , 200+int(dy/2)+dy*i)#coloca los bots de la segunda liena a la derecha
            coordenadas=(200+dx*j , 200+int(dy/2)+dy*i)#coloca los bots de la segunda linea a la izquierda
            vel=random.uniform(0,10)
            alpha=random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, '123', '*', 'detenido', 0)
            B.append(b1)
            

'''
#arreglo aleatorio de bots
for i in range(0, nx):
    for j in range(0, ny):
        x=L*i+random.uniform(-l,l)
        y=L*j+random.uniform(-l,l)
        vel=random.uniform(0,10)
        alpha=random.uniform(0,2*math.pi)
        b1=bot.coin(pantalla, (x,y), r, vel, alpha, False, '1')
        B.append(b1)


'''
B[0].modseed(True)
#B[1].modseed(True)
B[nx].modseed(True)
B[nx+1].modseed(True)
B[2*nx].modseed(True)

B[0].modgrad(0)
#B[1].modgrad(0)
B[nx].modgrad(1)
B[nx+1].modgrad(1)
B[2*nx].modgrad(2)


B[0].modcontador('A')
B[2].modcontador('B')
B[4].modcontador('C')
B[1].modcontador('D')
B[3].modcontador('E')
B[5].modcontador('F')




'''
B[5].modseed(True)
B[8].modseed(True)
B[9].modseed(True)
B[13].modseed(True)
#B[2*nx+1].modseed(True)

B[5].modgrad(0)
B[9].modgrad(1)
B[10].modgrad(1)
B[13].modgrad(2)
#B[2*nx+1].modgrad(2)

'''




#definir vecinos
#codigo para obtener los centros de los bots   
A=[]
for i in range(0,len(B)):
    cen=B[i].getdatpos()
    A.append(cen[0])
  
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
        if distancia < 3*r:
            if i==j:
                pass
            #elif j>i-1:
                #   pass
            else:
                nn=[i,j, distancia]
                vecinos.append(nn) 

#ordena la lista vecinos para poder manejar los datos con mayor facilidad                
lvecinos=[]
lvecinosD=[]
for i in range(0,len(B)):
    b=[]
    bD=[]
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
   

#asignacion estado
    

print(vecinos)
print(len(vecinos))
print(lvecinos)
print(len(lvecinos))
print(lvecinosD)
print(len(lvecinosD))

#codigo para dar un valor adecuado al gradiente
for i in range(0, len(B)):
    B[i].compseed()
    B[i].compgrad(len(B))
    if B[i].getgrad()<2:
        pass
while True:    
    comp=[]
    for i in range(0, len(B)):
        H=[]
        
        for j in range(0, len(lvecinos[i][1])):
            a=B[lvecinos[i][1][j]].getgrad()
            H.append(a)
        b=min(H)
        if B[i].getgrad()<2:
            pass
        else:
            B[i].modgrad(b+1)
    
        a=B[i].getgrad()
        comp.append(a)
    c=max(comp)
    print(c, ' este es el valor maximo del gradiente')
    if c<len(B):
        break
    else:
        pass
            
        


for k in range(0, 10):
    for h in range(0, len(B)):
       
        my_clock = pygame.time.Clock()
        pantalla.fill(NEGRO)
        
        ev = pygame.event.poll() # Look for any event
        if ev.type == pygame.QUIT: # Window close button clicked?
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
        '''        
        f1.dibujar()        
        f1.dibujarcir()
        f2.dibstar5()
        t1.dibujar()
        pos=pygame.mouse.get_pos()
        t1.actualizarpos(pos[0], pos[1])
        a=t1.getpos()
        
        comparacion=f2.comp(a[0][0], a[0][1], a[1])
        
        if comparacion==True:
            print('el objeto esta dentro')
            pygame.draw.circle(pantalla, (255,0,0), (850,850), 25, 0)
        else:
            print('el objeto esta fuera')
            pygame.draw.circle(pantalla, (0,0,255), (850,850), 25, 0)
            
        '''
                
        #for i in range(0, len(B)):
        #    pygame.draw.circle(pantalla, (0,255,0), (int(A[h][0]), int(A[h][1])), 3*r, 1)
            
        for i in range(0, len(B)):
            B[i].dibujar()
            #B[i].dibvel(10)
            B[i].dibseed()
            B[i].dibgrad()
            #B[i].dibestado()
            #B[i].dibcontador()
            #imprime la ID del bot
            #bot=str(i)
            #grad=font.render(bot, True, (255,255,255))
            #a=B[i].getdatpos()
            #pantalla.blit(grad, (a[0][0]-15, a[0][1]-25))
        
        
        #c=(500,500)
        #r=100
        #pygame.draw.circle(pantalla, (255,255,255), c, r, 1)
        #pygame.draw.rect(pantalla, BLANCO, (750.0,800.0,50.0,50.0), 0)
        #pygame.draw.rect(pantalla, BLANCO, (150.0,800.0,50.0,50.0), 0)
        #pygame.draw.rect(pantalla, BLANCO, (750.0,400.0,50.0,50.0), 0)
        #pygame.draw.rect(pantalla, BLANCO, (150.0,400.0,50.0,50.0), 0)
        pygame.image.save(pantalla, 'self assembly.jpeg')
        pygame.display.flip()
        my_clock.tick(1) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()