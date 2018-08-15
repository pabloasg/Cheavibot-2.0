import fig
import pygame
#import math
import time
import optirx as rx
import os
import csv

'''
en este programa se calibrab las distancias que corresponden a los cuadrantes en los cuales se divide el area de trabajo
'''


#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

'''
def getdata(): #coloca el codigo para capturar datos del optitrack en una funcion, la cual puede ser llamada posteriormente
    dsock = rx.mkdatasock()
    version = (2, 7, 0, 0)  # NatNet version to use     
        
    data = dsock.recv(rx.MAX_PACKETSIZE)
    packet = rx.unpack(data, version=version)
    if type(packet) is rx.SenderData:
        version = packet.natnet_version
    return packet
'''

pygame.init()
dimensiones = [1600, 1000]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('ventana de prueba para los dibujos')
NEGRO= (0,0,0)
BLANCO=(255,255,255)


#inicializar valores  parametros
s=1459.5
x=742.5
y=742.0
contador=10

ac=0
bc=0
cc=0
dc=0

ac0=0
bc0=0
cc0=0
dc0=0

at=False
bt=False
ct=False
dt=False

xm=0.7194
xb=0.8407
ym=0.7180
yb=-0.1867

xm1=-30
xm2=30
ym1=30
ym2=-30

xp1=(1/xm)*(xm1+xb)+x
xp2=(1/xm)*(xm2+xb)+x
yp1=(1/ym)*(ym1+yb)+y
yp2=(1/ym)*(ym2+yb)+y

print(xp2)
while True:       
    tiempo0=time.clock()
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    mensaje0='los parametros iniciales son: x1 = {}, x2 = {} y1 = {} y2={}'.format(str(ac0), str(bc0), str(cc0), str(dc0))
    mensaje1='los parametros despues de la calibarcion son: x1 = {}, x2 = {} , y1 = {} , y2={},  contador={}'.format(str(ac), str(bc), str(cc), str(dc), str(contador))
    
    pygame.draw.circle(pantalla, (255,255,255), (int(x),int(y)), 5, 0)
    
    pygame.draw.line(pantalla, BLANCO, (xp1+ac,0), (xp1+ac, dimensiones[1]), 1)
    pygame.draw.line(pantalla, BLANCO, (xp2+bc,0), (xp2+bc, dimensiones[1]), 1)
    pygame.draw.line(pantalla, BLANCO, (0,yp1+cc), (dimensiones[0], yp1+cc), 1)
    pygame.draw.line(pantalla, BLANCO, (0,yp2+dc), (dimensiones[0], yp2+dc), 1)
    '''
    a=getdata() #funcion que recoje los datos del optitrack
    print(a)
    b=a[1] #obtiene los datos de cuerpo rigido
    c=b[b'all'] 
    print(c)
    
    d=(-1*s*c[0][0]+x,-1*s*c[0][2]+y),(-1*s*c[1][0]+x,-1*s*c[1][2]+y),(-1*s*c[2][0]+x,-1*s*c[2][2]+y)
    e=(-1*s*c[3][0]+x,-1*s*c[3][2]+y),(-1*s*c[4][0]+x,-1*s*c[4][2]+y),(-1*s*c[5][0]+x,-1*s*c[5][2]+y)
    t1=fig.Chevibot(d[0], d[1], d[2], pantalla,'funcionando', 't1')
    t2=fig.Chevibot(e[0], e[1], e[2], pantalla, 'detenido', 't2')
    '''
    
    ev = pygame.event.poll() # Look for any event
    
    if ev.type == pygame.QUIT: # Window close button clicked?
        print(mensaje0)
        print(mensaje1)
        mensaje_final='los parametros finales son: x1 = {}, x2 = {} y1 s = {} y2={}'.format(str(xp1+ac), str(xp2+bc), str(yp1+cc), str(yp2+dc))
        print(mensaje_final)
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            print(mensaje0)
            print(mensaje1)
            mensaje_final='los parametros finales son: x1 = {}, x2 = {} y1 s = {} y2={}'.format(str(xp1+ac), str(xp2+bc), str(yp1+cc), str(yp2+dc))
            print(mensaje_final)
            break
        if ev.key == pygame.K_a:
            at=True
            bt=False
            ct=False
            dt=False
        if ev.key == pygame.K_b:
            at=False
            bt=True
            ct=False
            dt=False
        if ev.key == pygame.K_c:
            at=False
            bt=False
            ct=True
            dt=False
        if ev.key == pygame.K_d:
            at=False
            bt=False
            ct=False
            dt=True
        if at==False and bt==False and ct==False and dt==False:
            pass
        if at==True:
            if ev.key == pygame.K_KP_PLUS:
                ac=ac+1
            if ev.key == pygame.K_KP_MINUS:
                ac=ac-1
        if bt==True:
            if ev.key == pygame.K_KP_PLUS:
                bc=bc+1
            if ev.key == pygame.K_KP_MINUS:
                bc=bc-1
        if ct==True:
            if ev.key == pygame.K_KP_PLUS:
                cc=cc+1
            if ev.key == pygame.K_KP_MINUS:
                cc=cc-1
        if dt==True:
            if ev.key == pygame.K_KP_PLUS:
                dc=dc+1
            if ev.key == pygame.K_KP_MINUS:
                dc=dc-1
        
        
        
        
    '''   
        
    t1.dibujar()
    t2.dibujar()
    ang1=t1.angulos()
    ang2= t2.angulos()
    ori1=t1.orientacion65(ang1)
    ori2=t2.orientacion65(ang2)
    ap1=t1.circumcentro()
    ap2=t2.circumcentro()
    #b=t2.radio1()
    #a=t2.centrotri()
    a1=(ap1[0], ap1[1])
    b1=ap1[2]
    a2=(ap2[0], ap2[1])
    b2=ap2[2]
    #t2.dibujarcir1(a,b)
    z=0+contador
    t1.dibujarlrd1(a1, (b1+z), ori1)
    t2.dibujarlrd1(a2,(b2+z), ori2)
    t1.dibvect1(a1,(b1+z), ori1)
    t2.dibvect1(a2,(b2+z), ori2)
    d1=t1.getdibvect1(a1,b1, ori1)
    d2=t2.getdibvect1(a2,b2, ori2)
    ap11=[a1[0],a1[1], (b1+z)]
    ap22=[a2[0],a2[1], (b2+z)]
    t1.dibujarcir(ap11)
    t2.dibujarcir(ap22)
    t1.dibestado(a1, int(b1/4))
    t2.dibestado(a2, int(b2/4))
    t1.dibcentro(a1,b1)
    t2.dibcentro(a2,b2)
    g=t1.angorientacion(a1, ori1)
    h=t2.angorientacion(a2, ori2)
    
    
    
    #bloque condicional para controlar el movimiento
    #este bloque mueve el chevibot activo en los ejes x e y
    if t1.getestado()=='detenido':
        pass
    elif t1.getestado()=='funcionando':
        aux=t1.compdisan(a1,ori1, t2)
        aux1=t2.compdisan(a2,ori2, t1)
        #print(math.degrees(g))
        #print(aux[0], math.degrees(aux[1]))
        t1.dibrotacion(a1, b1, ori1,1,aux1[2])
        t1.rotar(a1,aux[2])
        t1.mover(g)   
    '''    
         
    '''
        if aux[1]<=math.pi and aux[1]>math.radians(5) and aux[0]>130 :
            t1.dibrotacion(a1, b1, ori1,aux[2],aux1[2])
            t1.rotar(a1,aux[2])
            t1.mover(g)        
        elif aux[0]>130:
            t1.dibavance(a1, b1, ori1, 1)
            t1.mover(g)        
        if aux[0]<130:
            t1.actualizarestado('detenido')
    
    else:
        pass
    '''
    
    tiempo1=time.clock()
    
    print('el tiempo de proceso es', tiempo1-tiempo0,'segundos, esto equivale a',1/(tiempo1-tiempo0),'fps')
    
        
   
   
 
    #bloque para escribir los datos de movimiento en un archivo csv
    
    #las siguientes lineas son para probar escribir un archivo con las coordenadas de los cuerpos rigidos

    
    pygame.display.flip()
    my_clock.tick(24) #FPS de la ventana y tambien de la actualizacion de los datos

pygame.quit()
datos=[ac, bc, cc, dc, contador]
with open('consquad.csv', 'w', newline='') as f: 
    writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(datos)
print('los valores de las lineas son:', xp1, xp2, yp1, yp2)