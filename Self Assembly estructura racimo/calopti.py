import fig
import pygame
#import math
import time
import optirx as rx
import os




#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100#-1825 este numero es para cuando se usa extender pantalla
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


def getdata(): #coloca el codigo para capturar datos del optitrack en una funcion, la cual puede ser llamada posteriormente
    dsock = rx.mkdatasock()
    version = (2, 7, 0, 0)  # NatNet version to use     
        
    data = dsock.recv(rx.MAX_PACKETSIZE)
    packet = rx.unpack(data, version=version)
    if type(packet) is rx.SenderData:
        version = packet.natnet_version
    return packet


pygame.init()
dimensiones = [1600, 1000]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('ventana de prueba para los dibujos')
NEGRO= (0,0,0)
#(s*c[0][0]+x,s*c[0][1]+y),(s*c[1][0]+x,s*c[1][1]+y),(s*c[2][0]+x,s*c[2][1]+y) asi se obtiene el dato del optitrack
#p1=(100,50)
#p2=(300,500)
#p3=(400,200)


#pa=((238,412),(138,362),(238,312))
pa=((150,300),(200,400),(250,300))
pb=((450,100),(500,200),(550,100))
#pb=((100,400),(200,200),(300,400))
p1a=pa[0]
p2a=pa[1]
p3a=pa[2]
p1b=pb[0]
p2b=pb[1]
p3b=pb[2]

#t1=fig.Chevibot(p1a, p2a, p3a, pantalla,'funcionando', 't1')
#t2=fig.Chevibot(p1b, p2b, p3b, pantalla, 'detenido', 't2')
#cbot=[t1,t2]


#inicializar valores  parametros
s=1459.5
x=742.5
y=742.0
t=1269.5
a=x
b=y
c=s
d=t
#inicializar valores boolean
xt=False
yt=False
st=False
tt=False


contador=0
while True:       
    tiempo0=time.clock()
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    mensaje0='los parametros iniciales son: x = {}, y = {} y s = {} st={}'.format(str(a), str(b), str(c), str(d))
    mensaje1='los parametros despues de la calibarcion son: xc = {}, yc = {} y sc = {}, sct={}, contador={}'.format(str(x), str(y), str(s), str(t), str(contador))
    
    pygame.draw.circle(pantalla, (255,255,255), (int(x),int(y)), 5, 0)
    a=getdata() #funcion que recoje los datos del optitrack
    print(a)
    b=a[1] #obtiene los datos de cuerpo rigido
    c=b[b'all'] 
    print(c)
    
    d=(-1*s*c[0][0]+x,-1*s*c[0][2]+y),(-1*s*c[1][0]+x,-1*s*c[1][2]+y),(-1*s*c[2][0]+x,-1*s*c[2][2]+y)
    e=(-1*s*c[3][0]+x,-1*s*c[3][2]+y),(-1*s*c[4][0]+x,-1*s*c[4][2]+y),(-1*s*c[5][0]+x,-1*s*c[5][2]+y)
    t1=fig.Chevibot(d[0], d[1], d[2], pantalla,'funcionando', 't1')
    t2=fig.Chevibot(e[0], e[1], e[2], pantalla, 'detenido', 't2')
    
    ev = pygame.event.poll() # Look for any event
    
    if ev.type == pygame.QUIT: # Window close button clicked?
        print(mensaje0)
        print(mensaje1)
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            print(mensaje0)
            print(mensaje1)
            break
        if ev.key == pygame.K_r:
            contador+=1
        if ev.key == pygame.K_e:
            contador-=1
        if ev.key == pygame.K_x:
            xt=True
            yt=False
            st=False
            tt=False
        if ev.key == pygame.K_y:
            xt=False
            yt=True
            st=False
        if ev.key == pygame.K_s:
            xt=False
            yt=False
            st=True
            tt=False
        if ev.key == pygame.K_t:
            xt=False
            yt=False
            st=False
            tt=True
        if st==False and xt==False and yt==False and tt==False:
            pass 
        if xt==True:
            if ev.key == pygame.K_KP_PLUS:
                x=x+100
            if ev.key == pygame.K_KP_MINUS:
                x=x-100
            if ev.key == pygame.K_UP:
                x=x+10
            if ev.key == pygame.K_DOWN:
                x=x-10
            if ev.key == pygame.K_RIGHT:
                x=x+0.5
            if ev.key == pygame.K_LEFT:
                x=x-0.5
                
        if yt==True:
            if ev.key == pygame.K_KP_PLUS:
                y=y+100
            if ev.key == pygame.K_KP_MINUS:
                y=y-100
            if ev.key == pygame.K_UP:
                y=y+10
            if ev.key == pygame.K_DOWN:
                y=y-10
            if ev.key == pygame.K_RIGHT:
                y=y+0.5
            if ev.key == pygame.K_LEFT:
                y=y-0.5
                
        if st==True:
            if ev.key == pygame.K_KP_PLUS:
                s=s+100
            if ev.key == pygame.K_KP_MINUS:
                s=s-100
            if ev.key == pygame.K_UP:
                s=s+10
            if ev.key == pygame.K_DOWN:
                s=s-10
            if ev.key == pygame.K_RIGHT:
                s=s+0.5
            if ev.key == pygame.K_LEFT:
                s=s-0.5
        
        if tt==True:
            if ev.key == pygame.K_KP_PLUS:
                t=t+100
            if ev.key == pygame.K_KP_MINUS:
                t=t-100
            if ev.key == pygame.K_UP:
                t=t+10
            if ev.key == pygame.K_DOWN:
                t=t-10
            if ev.key == pygame.K_RIGHT:
                t=t+0.5
            if ev.key == pygame.K_LEFT:
                t=t-0.5
    
    
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