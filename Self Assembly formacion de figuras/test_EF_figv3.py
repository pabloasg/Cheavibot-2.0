import pygame
import math
import os
import bot

'''
pruebas para correr el algoritmo de edge-following
'''


#ajusta la aparicion de la ventana en las coordenadas x,y
x = 200
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

Lx=1400
Ly=1000
pygame.init()
dimensiones = [Lx, Ly]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('pruebas para edge-following y entrar a la figura')
NEGRO= (0,0,0)
BLANCO=(255,255,255)

font = pygame.font.SysFont("arial", 20)

pos=[]
L=200
B=[]
r=50
for i in range(0,3):
    for j in range(0,3):
        x=300+L*i
        y=300+L*j
        pos.append((x,y))
        rob=bot.coin(pantalla, (x,y),r, 5,math.radians(90), True, 9, 'detenido', 0)
        B.append(rob)
        
        
B[2].modestado('fijo')
B[2].modgrad(10)

c1=bot.coin(pantalla, (700,0),(r),5,math.radians(90), False, 10, 'moviendose', 0)
c2=bot.coin(pantalla, (600,0),(r),5,math.radians(90), False, 10, 'moviendose', 0)
c3=bot.coin(pantalla, (100,100),(r),5,math.radians(90), False, 11, 'moviendose', 0)
c4=bot.coin(pantalla, (100,500),(r),5,math.radians(90), False, 11, 'moviendose', 0)
c5=bot.coin(pantalla, (-500,500),(r),5,math.radians(90), False, 11, 'moviendose', 0)

B.append(c1)
B.append(c2)
B.append(c3)
B.append(c4)
B.append(c5)


contador=[]
cfigura=[]
for i in range(0, len(B)):
    contador.append(0)
    cfigura.append('1')

centro=500,500


mul=2.7
while True:
    
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO)
    
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        pygame.quit()
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            pygame.quit()
            
    bf=[]
    bm=[]
    for i in range (0, len(B)):
        if B[i].getestado()=='fijo' or B[i].getestado()=='detenido':
            indicef=i
            bf.append(indicef)
        elif B[i].getestado()=='moviendose' or B[i].getestado()=='figura':
            indice=i
            bm.append(indice)
    
    for i in bf:
        posb=B[i].getdatpos()
        pygame.draw.circle(pantalla, BLANCO, (int(posb[0][0]), int(posb[0][1])), r, 1)
        pygame.draw.circle(pantalla, (0,255,0), (int(posb[0][0]), int(posb[0][1])), int(mul*r), 1)
        bot=str(i)
        grad=font.render(bot, True, (255,255,255))
        a=posb[0]
        pantalla.blit(grad, (a[0]-15, a[1]-25))

    #pygame.draw.circle(pantalla, BLANCO, (centro), r, 1)
    #pygame.draw.circle(pantalla, (0,255,0), (centro), 3*r, 1)
    for z in range(0, len(B)):  
        B[z].dibujar()
        B[z].dibestado()
        B[z].dibgrad()
        B[z].dibseed()
        B[z].dibvel(10)
    c2=(100,800)
    R=50
    #pygame.draw.circle(pantalla, BLANCO, (c2), R, 1)
    pygame.draw.circle(pantalla, (255,0,0), (c2), 4*R, 1)
    
    #codigo para comprobar si c1 ha entrado a la figura
    for z in bm:
        c1pos=B[z].getdatpos()
        distancia=math.sqrt((c1pos[0][0]-c2[0])**2+(c1pos[0][1]-c2[1])**2)
        
        if distancia<4*R and cfigura[z]=='out':
            contador[z]=contador[z]+1
        elif distancia<4*R and cfigura[z]=='in':
            contador[z]=contador[z]
        if distancia<4*R and B[z].getestado()!='fijo':
            cfigura[z]='in'
            B[z].modestado('figura')
        else:
            cfigura[z]='out'
            if B[z].getestado()=='fijo':
                pass
            else:
                B[z].modestado('moviendose')
        B[z].modcontador(contador[z])
        
        aux=B[z].getestado()
        pos1=B[z].getdatpos()
        pos2=B[z-1].getdatpos()
        distanciavec=math.sqrt((pos1[0][0]-pos2[0][0])**2+(pos1[0][1]-pos2[0][1])**2)
        #print(cfigura[z], ',contador = ', contador[z], B[z].getestado(), 'antes, bot ', z)
        if aux=='moviendose' and B[z].getcontador()==1:
            B[z].modestado('fijo')
            print('1')
        
        elif aux=='figura' and B[z].getcontador()==1 and distanciavec <=(mul-1)*r:
            B[z].modestado('fijo')
            print('2')
            
        elif aux=='figura' and B[z].getcontador()==1 and B[z].getgrad()==B[z-1].getgrad() and distanciavec<=mul*r:
            B[z].modestado('fijo')
            print('3')
        else:
            pass
    
        #print(cfigura[z], ',contador = ', contador[z], B[z].getestado(), 'despues, bot',z)
        
        if aux=='fijo':
            pass
        else:
            comp=[]
            for j in bf:
                posbf=B[j].getdatpos()
                centroc1=B[z].getdatpos()
                distanciacp=math.sqrt((posbf[0][0]-centroc1[0][0])**2+(posbf[0][1]-centroc1[0][1])**2)
                comp.append((distanciacp,j))
            l=min(comp)
            m=l[1]
                
                
            centroc1=B[z].getdatpos()
            vl=B[z].getvel()
            ang=B[z].getang()
            p1=(vl*math.cos(ang)+centroc1[0][0], vl*math.sin(ang)+centroc1[0][1])
            p2=centroc1[0][0], centroc1[0][1]
            #print(pos, 'posicion')
            posbf=B[m].getdatpos()
            p3=posbf[0]#centro
            
            
            u=(p1[0]-p2[0], p1[1]-p2[1])
            v=(p3[0]-p2[0], p3[1]-p2[1])
            u2=(u[0]*u[0]+u[1]*u[1])**0.5
            v2=(v[0]*v[0]+v[1]*v[1])**0.5
            uv= u[0]*v[0]+u[1]*v[1] 
            #para evitar division por cero
            if u2*v2==0 or uv/(u2*v2)>1:
                det=0
                alphacom=0
            else:
                alphacom=math.acos(uv/(u2*v2))
                det=u[0]*v[1]-u[1]*v[0]
            
            if det<0:
                alphacom=alphacom
                dirmov=-1
            else:
                alphacom=2*math.pi-alphacom
                dirmov=1
                
            #distancia=math.sqrt((pos[m][0]-centroc1[0][0])**2+(pos[m][1]-centroc1[0][1])**2)
            distancia=math.sqrt((posbf[0][0]-centroc1[0][0])**2+(posbf[0][1]-centroc1[0][1])**2)
            if alphacom>math.radians(10) and dirmov==-1 and distancia >mul*r:
                B[z].rotar(0)
            elif alphacom>math.radians(10) and dirmov==1 and distancia >mul*r:
                B[z].rotar(1)
            elif distancia >mul*r:
                B[z].mover()
            elif distancia > mul*r-50 and distancia <=mul*r:
                pygame.draw.line(pantalla, (0,0,255), centroc1[0], posbf[0], 1)
                x0=posbf[0][0]-centroc1[0][0]
                y0=posbf[0][1]-centroc1[0][1]
                tan=y0, -x0
                x=tan[0]+centroc1[0][0]
                y=tan[1]+centroc1[0][1]
                pygame.draw.line(pantalla, (0,255,255), centroc1[0], (x,y), 1)
                
                centroc1=B[z].getdatpos()
                vl=B[z].getvel()
                ang=B[z].getang()
                p1=(vl*math.cos(ang)+centroc1[0][0], vl*math.sin(ang)+centroc1[0][1])
                p2=centroc1[0][0], centroc1[0][1]
                p3=(x,y)
                
                u=(p1[0]-p2[0], p1[1]-p2[1])
                v=(p3[0]-p2[0], p3[1]-p2[1])
                u2=(u[0]*u[0]+u[1]*u[1])**0.5
                v2=(v[0]*v[0]+v[1]*v[1])**0.5
                uv= u[0]*v[0]+u[1]*v[1] 
                #para evitar division por cero
                if u2*v2==0 or uv/(u2*v2)>1:
                    det=0
                    alphacom=0
                else:
                    alphacom=math.acos(uv/(u2*v2))
                    det=u[0]*v[1]-u[1]*v[0]
                
                if det<0:
                    alphacom=alphacom
                    dirmov=-1
                else:
                    alphacom=2*math.pi-alphacom
                    dirmov=1
                #print(math.degrees(alphacom), 'angulo')
                    
                if alphacom>math.radians(10) and dirmov==-1:
                    B[z].rotar(0)
                elif alphacom>math.radians(10) and dirmov==1:
                    B[z].rotar(1)
                else:
                    if dirmov==-1 and distancia >mul*r-5:
                        B[z].mover()
                    elif dirmov==1 and distancia >mul*r-5:
                        B[z].mover()
                    elif dirmov==-1 and distancia >mul*r-30:
                        B[z].rotar(0)
                        B[z].mover()
                    elif dirmov==1 and distancia >mul*r-30:
                        B[z].rotar(1)
                        B[z].mover()
                    else:
                        B[z].mover()
        


    pygame.display.flip()
    my_clock.tick(60) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()
