import fig
import pygame
#import math
import time
import optirx as rx
import os
import math
import csv

'''
en este programa se calibrab las distancias que corresponden a los cuadrantes en los cuales se divide el area de trabajo
'''


#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100#-1825#100
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
CYAN=(0,255,255)
font = pygame.font.SysFont("arial", 25)

def getdata(): #coloca el codigo para capturar datos del optitrack en una funcion, la cual puede ser llamada posteriormente
    dsock = rx.mkdatasock()
    version = (2, 7, 0, 0)  # NatNet version to use     
        
    data = dsock.recv(rx.MAX_PACKETSIZE)
    packet = rx.unpack(data, version=version)
    if type(packet) is rx.SenderData:
        version = packet.natnet_version
    return packet


#inicializar valores  parametros
s=1459.5
x=742.5
y=742.0
contador=10

x1=704.5
x2=788.0
y1=782.0
y2=698.5

#cuadrantes
c1=False
c2=False
c3=False
c4=False
c5=False
c6=False
c7=False
c8=False
c9=False
#metodo de relosucion
uni=False#corresponde a una solucion uniforme
pen=False#corresponde a solo encontrar una pendiente
lin=False#corresponde a encontrar la pendiente y una constante
#coordenada a modificar
xmod=False
ymod=False
#inicializar variables para modificar posicion
#valores que corresponden a la constante
c1xb=0
c1yb=0
c2xb=0
c2yb=0
c3xb=0
c3yb=0
c4xb=0
c4yb=0
c5xb=0
c5yb=0
c6xb=0
c6yb=0
c7xb=0
c7yb=0
c8xb=0
c8yb=0
c9xb=0
c9yb=0
#valores que corresponden a la pendiente
c1xm=0
c1ym=0
c2xm=0
c2ym=0
c3xm=0
c3ym=0
c4xm=0
c4ym=0
c5xm=0
c5ym=0
c6xm=0
c6ym=0
c7xm=0
c7ym=0
c8xm=0
c8ym=0
c9xm=0
c9ym=0

xc1=int(650)
yc1=int(800)
xc2=int(740)
yc2=int(800)
xc3=int(820)
yc3=int(800)
xc4=int(650)
yc4=int(740)
xc5=int(740)
yc5=int(740)
xc6=int(820)
yc6=int(740)
xc7=int(650)
yc7=int(640)
xc8=int(740)
yc8=int(640)
xc9=int(820)
yc9=int(640)



while True:       
    tiempo0=time.clock()
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    #mensaje0='los parametros iniciales son: x1 = {}, x2 = {} y1 s = {} y2={}'.format(str(ac0), str(bc0), str(cc0), str(dc0))
    #mensaje1='los parametros despues de la calibarcion son: x1 = {}, x2 = {} , y1 = {} , y2={},  contador={}'.format(str(ac), str(bc), str(cc), str(dc), str(contador))
    
    pygame.draw.circle(pantalla, (255,255,255), (int(x),int(y)), 5, 0)
    
    pygame.draw.line(pantalla, BLANCO, (x1,0), (x1, dimensiones[1]), 1)
    pygame.draw.line(pantalla, BLANCO, (x2,0), (x2, dimensiones[1]), 1)
    pygame.draw.line(pantalla, BLANCO, (0,y1), (dimensiones[0], y1), 1)
    pygame.draw.line(pantalla, BLANCO, (0,y2), (dimensiones[0], y2), 1)
    
    
    #escribe el numero del cuadrante en el cuadrante correspondiente
    cuad1=str(1)
    cuad1f=font.render(cuad1, True, (255,255,255))
    pantalla.blit(cuad1f, ((x1-20), (y1+20)))
    cuad2=str(2)
    cuad2f=font.render(cuad2, True, (255,255,255))
    pantalla.blit(cuad2f, ((x2-45), (y1+20)))
    cuad3=str(3)
    cuad3f=font.render(cuad3, True, (255,255,255))
    pantalla.blit(cuad3f, ((x2+20), (y1+20)))
    cuad4=str(4)
    cuad4f=font.render(cuad4, True, (255,255,255))
    pantalla.blit(cuad4f, ((x1-20), (y2+20)))
    cuad5=str(5)
    cuad5f=font.render(cuad5, True, (255,255,255))
    pantalla.blit(cuad5f, ((x2-45), (y2+20)))
    cuad6=str(6)
    cuad6f=font.render(cuad6, True, (255,255,255))
    pantalla.blit(cuad6f, ((x2+20), (y2+20)))
    cuad7=str(7)
    cuad7f=font.render(cuad7, True, (255,255,255))
    pantalla.blit(cuad7f, ((x1-20), (y2-40)))
    cuad8=str(8)
    cuad8f=font.render(cuad8, True, (255,255,255))
    pantalla.blit(cuad8f, ((x2-45), (y2-40)))
    cuad9=str(9)
    cuad9f=font.render(cuad9, True, (255,255,255))
    pantalla.blit(cuad9f, ((x2+20), (y2-40)))
    
    a=getdata() #funcion que recoje los datos del optitrack
    print(a)
    b=a[1] #obtiene los datos de cuerpo rigido
    c=b[b'all'] 
    print(c)
    
    d=(-1*s*c[0][0]+x,-1*s*c[0][2]+y),(-1*s*c[1][0]+x,-1*s*c[1][2]+y),(-1*s*c[2][0]+x,-1*s*c[2][2]+y)
    e=(-1*s*c[3][0]+x,-1*s*c[3][2]+y),(-1*s*c[4][0]+x,-1*s*c[4][2]+y),(-1*s*c[5][0]+x,-1*s*c[5][2]+y)
    t1=fig.Chevibot(d[0], d[1], d[2], pantalla,'funcionando', 't1')
    t2=fig.Chevibot(e[0], e[1], e[2], pantalla, 'detenido', 't2')
    
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
    
    xc=ap1[0]
    yc=ap1[1]
    r=ap1[2]+10
    xcp=ap2[0]
    ycp=ap2[1]
    rp=ap2[2]
    
   
    xm, ym =pygame.mouse.get_pos()
    pygame.draw.circle(pantalla, BLANCO, (xm, ym), 50, 1)
    
    #bloque para escribir en pantalla informacion
    met=''
    coor=''
    if c1 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c1xm), str(c1xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c1ym), str(c1yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc11=xc+int(xc*c1xm+c1xb)
        yc11=yc+int(yc*c1ym+c1yb)
        pygame.draw.circle(pantalla, CYAN, (xc11, yc11), r, 2)
        xc11p=xcp+int(xcp*c1xm+c1xb)
        yc11p=ycp+int(ycp*c1ym+c1yb)
        pygame.draw.circle(pantalla, CYAN, (xc11p, yc11p), rp, 2)
        dat='cuadrante =  '+str(1)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c2 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c2xm), str(c2xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c2ym), str(c2yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc21=xc+int(xc*c2xm+c2xb)
        yc21=yc+int(yc*c2ym+c2yb)
        pygame.draw.circle(pantalla, CYAN, (xc21, yc21), r, 2)
        xc21p=xcp+int(xcp*c2xm+c2xb)
        yc21p=ycp+int(ycp*c2ym+c2yb)
        pygame.draw.circle(pantalla, CYAN, (xc21p, yc21p), rp, 2)
        dat='cuadrante =  '+str(2)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c3 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c3xm), str(c3xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c3ym), str(c3yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc31=xc+int(xc*c3xm+c3xb)
        yc31=yc+int(yc*c3ym+c3yb)
        pygame.draw.circle(pantalla, CYAN, (xc31, yc31), r, 2)
        xc31p=xcp+int(xcp*c3xm+c3xb)
        yc31p=ycp+int(ycp*c3ym+c3yb)
        pygame.draw.circle(pantalla, CYAN, (xc31p, yc31p), rp, 2)
        dat='cuadrante =  '+str(3)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c4 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c4xm), str(c4xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c4ym), str(c4yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc41=xc+int(xc*c4xm+c4xb)
        yc41=yc+int(yc*c4ym+c4yb)
        pygame.draw.circle(pantalla, CYAN, (xc41, yc41), r, 2)
        xc41p=xcp+int(xcp*c4xm+c4xb)
        yc41p=ycp+int(ycp*c4ym+c4yb)
        pygame.draw.circle(pantalla, CYAN, (xc41p, yc41p), rp, 2)
        dat='cuadrante =  '+str(4)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c5 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c5xm), str(c5xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c5ym), str(c5yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc51=xc+int(xc*c5xm+c5xb)
        yc51=yc+int(yc*c5ym+c5yb)
        pygame.draw.circle(pantalla, CYAN, (xc51, yc51), r, 2)
        xc51p=xcp+int(xcp*c5xm+c5xb)
        yc51p=ycp+int(ycp*c5ym+c5yb)
        pygame.draw.circle(pantalla, CYAN, (xc51p, yc51p), rp, 2)
        dat='cuadrante =  '+str(5)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c6 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c6xm), str(c6xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c6ym), str(c6yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc61=xc+int(xc*c6xm+c6xb)
        yc61=yc+int(yc*c6ym+c6yb)
        pygame.draw.circle(pantalla, CYAN, (xc61, yc61), r, 2)
        xc61p=xcp+int(xcp*c6xm+c6xb)
        yc61p=ycp+int(ycp*c6ym+c6yb)
        pygame.draw.circle(pantalla, CYAN, (xc61p, yc61p), rp, 2)
        dat='cuadrante =  '+str(6)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c7 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c7xm), str(c7xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c7ym), str(c7yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc71=xc+int(xc*c7xm+c7xb)
        yc71=yc+int(yc*c7ym+c7yb)
        pygame.draw.circle(pantalla, CYAN, (xc71, yc71), r, 2)
        xc71p=xcp+int(xcp*c7xm+c7xb)
        yc71p=ycp+int(ycp*c7ym+c7yb)
        pygame.draw.circle(pantalla, CYAN, (xc71p, yc71p), rp, 2)
        dat='cuadrante =  '+str(7)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c8 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c8xm), str(c8xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c8ym), str(c8yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc81=xc+int(xc*c8xm+c8xb)
        yc81=yc+int(yc*c8ym+c8yb)
        pygame.draw.circle(pantalla, CYAN, (xc81, yc81), r, 2)
        xc81p=xcp+int(xcp*c8xm+c8xb)
        yc81p=ycp+int(ycp*c8ym+c8yb)
        pygame.draw.circle(pantalla, CYAN, (xc81p, yc81p), rp, 2)
        dat='cuadrante =  '+str(8)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    if c9 == True:
        if uni== True:
            met='uniforme'
        elif pen == True:
            met='pendiente'
        elif lin == True:
            met='lineal'
        if xmod == True:
            coor='x'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c9xm), str(c9xb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        elif ymod == True:
            coor= 'y'
            dat3='valor modificacion mx= {}, bx ={}  '.format(str(c9ym), str(c9yb))
            datf3=font.render(dat3, True, (255,255,255))
            pantalla.blit(datf3, (1000,340))
        xc91=xc+int(xc*c9xm+c9xb)
        yc91=yc+int(yc*c9ym+c9yb)
        pygame.draw.circle(pantalla, CYAN, (xc91, yc91), r, 2)
        xc91p=xcp+int(xcp*c9xm+c9xb)
        yc91p=ycp+int(ycp*c9ym+c9yb)
        pygame.draw.circle(pantalla, CYAN, (xc91p, yc91p), rp, 2)
        dat='cuadrante =  '+str(9)
        datf=font.render(dat, True, (255,255,255))
        pantalla.blit(datf, (1000,250))
        dat1='metodo resolucion =  '+met
        datf1=font.render(dat1, True, (255,255,255))
        pantalla.blit(datf1, (1000,280))
        dat2='coordenada =  '+coor
        datf2=font.render(dat2, True, (255,255,255))
        pantalla.blit(datf2, (1000,310))
        
    
    ev = pygame.event.poll() # Look for any event
    
    if ev.type == pygame.QUIT: # Window close button clicked?
        #print(mensaje0)
        #print(mensaje1)
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            #print(mensaje0)
            #print(mensaje1)
            break
        #asigna valores bool a las teclas
        if ev.key == pygame.K_1:
            c1=True 
            c2=False
            c3=False
            c4=False
            c5=False
            c6=False
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_2:
            c1=False 
            c2=True
            c3=False
            c4=False
            c5=False
            c6=False
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_3:
            c1=False 
            c2=False
            c3=True
            c4=False
            c5=False
            c6=False
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_4:
            c1=False
            c2=False
            c3=False
            c4=True
            c5=False
            c6=False
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_5:
            c1=False 
            c2=False
            c3=False
            c4=False
            c5=True
            c6=False
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_6:
            c1=False
            c2=False
            c3=False
            c4=False
            c5=False
            c6=True
            c7=False
            c8=False
            c9=False
        if ev.key == pygame.K_7:
            c1=False
            c2=False
            c3=False
            c4=False
            c5=False
            c6=False
            c7=True
            c8=False
            c9=False
        if ev.key == pygame.K_8:
            c1=False 
            c2=False
            c3=False
            c4=False
            c5=False
            c6=False
            c7=False
            c8=True
            c9=False
        if ev.key == pygame.K_9:
            c1=False 
            c2=False
            c3=False
            c4=False
            c5=False
            c6=False
            c7=False
            c8=False
            c9=True
        if ev.key == pygame.K_u:
            uni=True
            pen=False
            lin=False
        if ev.key == pygame.K_p:
            uni=False
            pen=True
            lin=False
        if ev.key == pygame.K_l:
            uni=False
            pen=False
            lin=True
        if ev.key == pygame.K_x:
            xmod=True
            ymod=False
        if ev.key == pygame.K_y:
            xmod=False
            ymod=True
            
        #bloque para reiniciar valores de desplazamiento
        if ev.key == pygame.K_KP1:
            c1xb=0
            c1xm=0
            c1yb=0
            c1ym=0
        if ev.key == pygame.K_KP2:
            c2xb=0
            c2xm=0
            c2yb=0
            c2ym=0
        if ev.key == pygame.K_KP3:
            c3xb=0
            c3xm=0
            c3yb=0
            c3ym=0
        if ev.key == pygame.K_KP4:
            c4xb=0
            c4xm=0
            c4yb=0
            c4ym=0
        if ev.key == pygame.K_KP5:
            c5xb=0
            c5xm=0
            c5yb=0
            c5ym=0
        if ev.key == pygame.K_KP6:
            c6xb=0
            c6xm=0
            c6yb=0
            c6ym=0
        if ev.key == pygame.K_KP7:
            c7xb=0
            c7xm=0
            c7yb=0
            c7ym=0
        if ev.key == pygame.K_KP8:
            c8xb=0
            c8xm=0
            c8yb=0
            c8ym=0
        if ev.key == pygame.K_KP9:
            c9xb=0
            c9xm=0
            c9yb=0
            c9ym=0
        #bloque para modificar desplazamientos
        if c1 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1xb=c1xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c1xb=c1xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1yb=c1yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c1yb=c1yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1xm=round(c1xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c1xm=round(c1xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1ym=round(c1ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c1ym=round(c1ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1xm=round(c1xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c1xb=c1xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c1xm=round(c1xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c1xb=c1xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c1ym=round(c1ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c1yb=c1yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c1ym=round(c1ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c1yb=c1yb-1
            
                    
                    
        if c2 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2xb=c2xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c2xb=c2xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2yb=c2yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c2yb=c2yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2xm=round(c2xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c2xm=round(c2xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2ym=round(c2ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c2ym=round(c2ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2xm=round(c2xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c2xb=c2xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c2xm=round(c2xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c2xb=c2xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c2ym=round(c2ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c2yb=c2yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c2ym=round(c2ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c2yb=c2yb-1
                    
                    
        if c3 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3xb=c3xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c3xb=c3xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3yb=c3yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c3yb=c3yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3xm=round(c3xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c3xm=round(c3xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3ym=round(c3ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c3ym=round(c3ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3xm=round(c3xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c3xb=c3xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c3xm=round(c3xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c3xb=c3xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c3ym=round(c3ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c3yb=c3yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c3ym=round(c3ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c3yb=c3yb-1
                    
                    
        if c4 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4xb=c4xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c4xb=c4xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4yb=c4yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c4yb=c4yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4xm=round(c4xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c4xm=round(c4xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4ym=round(c4ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c4ym=round(c4ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4xm=round(c4xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c4xb=c4xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c4xm=round(c4xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c4xb=c4xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c4ym=round(c4ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c4yb=c4yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c4ym=round(c4ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c4yb=c4yb-1
                    
                    
        if c5 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5xb=c5xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c5xb=c5xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5yb=c5yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c5yb=c5yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5xm=round(c5xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c5xm=round(c5xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5ym=round(c5ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c5ym=round(c5ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5xm=round(c5xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c5xb=c5xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c5xm=round(c5xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c5xb=c5xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c5ym=round(c5ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c5yb=c5yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c5ym=round(c5ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c5yb=c5yb-1
                    
                    
        if c6 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6xb=c6xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c6xb=c6xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6yb=c6yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c6yb=c6yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6xm=round(c6xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c6xm=round(c6xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6ym=round(c6ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c6ym=round(c6ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6xm=round(c6xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c6xb=c6xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c6xm=round(c6xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c6xb=c6xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c6ym=round(c6ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c6yb=c6yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c6ym=round(c6ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c6yb=c6yb-1
                    
                    
        if c7 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7xb=c7xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c7xb=c7xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7yb=c7yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c7yb=c7yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7xm=round(c7xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c7xm=round(c7xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7ym=round(c7ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c7ym=round(c7ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7xm=round(c7xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c7xb=c7xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c7xm=round(c7xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c7xb=c7xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c7ym=round(c7ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c7yb=c7yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c7ym=round(c7ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c7yb=c7yb-1
                    
                    
        if c8 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8xb=c8xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c8xb=c8xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8yb=c8yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c8yb=c8yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8xm=round(c8xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c8xm=round(c8xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8ym=round(c8ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c8ym=round(c8ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8xm=round(c8xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c8xb=c8xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c8xm=round(c8xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c8xb=c8xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c8ym=round(c8ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c8yb=c8yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c8ym=round(c8ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c8yb=c8yb-1
                    
                    
        if c9 == True:
            if uni == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9xb=c9xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c9xb=c9xb-1
            if uni == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9yb=c9yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c9yb=c9yb-1
            if pen == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9xm=round(c9xm+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c9xm=round(c9xm-0.001, 3)
            if pen == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9ym=round(c9ym+0.001, 3)
                if ev.key == pygame.K_KP_MINUS:
                    c9ym=round(c9ym-0.001, 3)
            if lin == True and xmod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9xm=round(c9xm+0.001, 3)
                if ev.key == pygame.K_UP:
                    c9xb=c9xb+1
                if ev.key == pygame.K_KP_MINUS:
                    c9xm=round(c9xm-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c9xb=c9xb-1
            if lin == True and ymod == True:
                if ev.key == pygame.K_KP_PLUS:
                    c9ym=round(c9ym+0.001, 3)
                if ev.key == pygame.K_UP:
                    c9yb=c9yb+1
                if ev.key == pygame.K_KP_MINUS:
                    c9ym=round(c9ym-0.001, 3)
                if ev.key == pygame.K_DOWN:
                    c9yb=c9yb-1
            
        
        
        
            
            
            
        
    print(c1, c2, c3, c4, c5, c6, c7, c8, c9, 'metodos', uni, pen, lin)
     
    
    
    
    
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
datos=[[1,c1xm, c1xb, c1ym, c1yb], [2,c2xm, c2xb, c2ym, c2yb], [3,c3xm, c3xb, c3ym, c3yb], [4,c4xm, c4xb, c4ym, c4yb], [5,c5xm, c5xb, c5ym, c5yb], [6,c6xm, c6xb, c6ym, c6yb], [7,c7xm, c7xb, c7ym, c7yb], [8,c8xm, c8xb, c8ym, c8yb], [9,c9xm, c9xb, c9ym, c9yb]]
print(datos)

with open('constantes1.csv', 'w', newline='') as f: 
    writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(datos)
