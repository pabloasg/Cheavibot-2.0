import pygame
import math
import os
import random
import objetos
from pickle import NONE #se ocupa para poder usar la variable NONE
import csv

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
L=70 #separacion bots
nx=int(2*Lx/L)
ny=int(2*Ly/L)

s=10000
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
r=20

B=[]
for i in range(0, len(centro)):
    aux=objetos.bot(pantalla, centro[i], r, v[i], alpha[i], 'seguidor')
    B.append(aux)
    B[i].verestado()
    
pygame.key.set_repeat(1,1)
pygame.key.get_repeat()
#while True: 
with open('mov.csv', 'w', newline='') as f: 
   
    
    paso=1000  
    p=0
    while True:
        p=p+1
        contador=0
        cc=[]
        vc=[]
        ac=[]
        dirmov=[]
          
        my_clock = pygame.time.Clock()
        pantalla.fill(NEGRO)
        
        ev = pygame.event.poll() # Look for any event
        if ev.type == pygame.QUIT: # Window close button clicked?
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
            
        pasot='paso numero  '+str(p)
        pasof=font.render(pasot, True, (255,0,255))
        pantalla.blit(pasof, (600,50))
            
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
        
        
        #print(h,'valor h')
        #print(vecinos)
        
        #cor=B[h].getpos()
        
        #pygame.draw.circle(pantalla, (0,255,0), (int(cor[0]), int(cor[1])), 6*r, 1)
        #pygame.draw.circle(pantalla, (0,0,255), (int(cor[0]), int(cor[1])), 4*r, 1)
        #pygame.draw.circle(pantalla, (255,0,0), (int(cor[0]), int(cor[1])), 2*r, 1)
        #print(len(lvecinos[h][1]))
        
        for h in range(0, len(B)):    
            av=NONE
            print(2*r)
            print(lvecinosD[h][1])
            for d in lvecinosD[h][1]:
                if d < 2*r+r:
                    av=True
                    contador=contador+1
                    break
                    
                else:
                    av=False
                x=centro[lvecinos[h][0]][0]  
                y=centro[lvecinos[h][0]][1]       
                print(x,y,'corrdenadas centro')
                for d1 in range (0, len(lvecinos[h][1])):
                    print(d1)
                    x=x+centro[lvecinos[h][1][d1]][0]
                    y=y+centro[lvecinos[h][1][d1]][1]
                    print('coordenadas de los otros bots', centro[lvecinos[h][1][d1]][0],centro[lvecinos[h][1][d1]][1])
                                  
                pc=x/(len(lvecinos[h][1])+1),y/(len(lvecinos[h][1])+1)
                cc.append(pc)
                print(pc, 'centro de los bots')
                print(len(lvecinos[h][1])+1)
            
        #pygame.draw.circle(pantalla, (255,0,255), (int(pc[0]), int(pc[1])), 5, 0)
        
        for h in range(0, len(B)):
            v=B[h].getvel()
            an=B[h].getang()
            ax=math.cos(an)
            ay=math.sin(an)
            print(math.degrees(an), 'angulo del bot i')
            for d2 in range(0, len(lvecinos[h][1])):
                v=v+B[lvecinos[h][1][d2]].getvel()
                an=B[lvecinos[h][1][d2]].getang()
                ax=ax+math.cos(an)
                ay=ay+math.sin(an)
                print(math.degrees(B[lvecinos[h][1][d2]].getang()),'angulo del bot vecino', lvecinos[h][1][d2] , math.degrees(an),'angulo acumulado')
            vel=v/(len(lvecinos[h][1])+1)
            alpha=ax/(len(lvecinos[h][1])+1),ay/(len(lvecinos[h][1])+1)
            alpha=math.atan2(ay, ax)
            print(math.degrees(alpha),'angulo promedio', (len(lvecinos[h][1])+1),'numero de bot a considerar' )
            cos=math.cos(alpha)
            sin=math.sin(alpha)
            vx=int(pc[0])+int(10*vel*cos)
            vy=int(pc[1])+int(10*vel*sin)
            vc.append(vel)
            ac.append(alpha)
        #pygame.draw.line(pantalla, (255,0,0), (int(pc[0]), int(pc[1])), (vx, vy), 1)
        
        for h in range(0,len(B)):
            ang=B[h].getang()
            v=B[h].getvel()
            p1=50+10*v*math.cos(ang),50+10*v*math.sin(ang)
            p2=(50,50)
            p3=50+10*vel*math.cos(alpha), 50+10*vel*math.sin(alpha)
            pygame.draw.line(pantalla, (0,255,0), p2, p1, 1)
            pygame.draw.line(pantalla, (255,0,0), p2, p3, 1)
            print('valores de las lineas', math.degrees(ang), 'velocidad', vel)
            u=(p1[0]-p2[0], p1[1]-p2[1])
            v=(p3[0]-p2[0], p3[1]-p2[1])
            u2=(u[0]*u[0]+u[1]*u[1])**0.5
            v2=(v[0]*v[0]+v[1]*v[1])**0.5
            uv= u[0]*v[0]+u[1]*v[1] 
            alphacom=math.acos(uv/(u2*v2))
            det=u[0]*v[1]-u[1]*v[0]
            if det<0:
                alphacom=alphacom
                dirmov.append(-1)
            else:
                alphacom=2*math.pi-alphacom
                dirmov.append(1)
            '''
            alphacomd=int(math.degrees(alphacom))
            tang='angulo es  '+str(alphacomd)+'det es  '+ str(det)
            difang=font.render(tang, True, (255,0,255))
            pantalla.blit(difang,(50, 50))
            if det<0:
                rot='gira anti horario'
                dirrot =font.render(rot, True, (255,0,255))
                pantalla.blit(dirrot,(50, 80))
            else:
                rot='gira horario'
                dirrot =font.render(rot, True, (255,0,255))
                pantalla.blit(dirrot,(50, 80))
            '''
            
                
        #print(av, 'hay algun bot en el area de repulsion')
        #print(contador,'cantidad de bots en area de repulsion')
        
        #codigo para dibujar los bots 
        for i in range (0, len(B)):
            B[i].dibujar()
            B[i].dibujarvel()
            #codigo para aplicar reglas de movimiento
            if h==len(B)-1: #en esta aplicacion en particular esta linea hace que el codigo se aplique al principio de cada paso
                #p1=50+10*B[i].getvel()*math.cos(B[i].getang()),50+10*B[i].getvel()*math.cos(B[i].getang())
                #p2=(0,0)
                #p3=50+10*vc[i]*math.cos(ac[i]), 50+10*vc[i]*math.sin(ac[i])
                #pygame.draw.line(pantalla, BLANCO, p2, p1, 1)
                #pygame.draw.line(pantalla, BLANCO, p2, p3, 1)
                
                #alinear velocidades
                if dirmov[i]==-1:
                    B[i].rotar(0)
                    B[i].actvel(vc[i])
                    B[i].mover()
                elif dirmov[i]==1:
                    B[i].rotar(1)
                    B[i].actvel(vc[i])
                    B[i].mover()
                else:
                    B[i].actvel(vc[i])
                    B[i].mover()
                #print(h,'valor de h')
                #print(len(vc), len(ac), len(cc),'largo del vector central', len(B))
        
        
        name=('imagen N'+ str(h)+'.jpeg')
        #pygame.image.save(pantalla, name)
        pygame.display.flip()
        my_clock.tick(60) #FPS de la ventana y tambien de la actualizacion de los datos
    
        cor=[]
        for k in range(0, len(B)):
            c=B[k].getpos()
            v=B[k].getvel()
            a=B[k].getang()
            vx=v*math.cos(a)
            vy=v*math.sin(a)
            coordenadas=[c[0],c[1], vx, vy, v, a]
            for l in range (0, len(coordenadas)):
                cor.append(coordenadas[l])
        
        writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows([cor])
    
pygame.quit()