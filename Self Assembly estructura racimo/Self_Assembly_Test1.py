import fig
import pygame
import math
import time
import random
import os
from pickle import NONE #se ocupa para poder usar la variable NONE

#ajusta la aparicion de la ventana en las coordenadas x,y
x = 600
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#en este caso se inicializa pygame para poder obtener los objetos, ademas se inicializa las condiciones de la pantalla y parametros para la generacion de objetos
#se escoge generar objetos segun una reticula hexagonal
Lx=800
Ly=800
os=200 #offset total
pygame.init()
dimensiones = [Lx+os, Ly+os]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('objetos generados')
NEGRO= (0,0,0)
BLANCO=(255,255,255)


font = pygame.font.SysFont("comicsansms", 20)

#parametros de la reticula
c=[]
L=100 #separacion entre bots
nx=int(Lx/L)
ny=int(Ly/(L*math.sqrt(3)/2)+1)
dx=int(L)
dy=int(L*math.sqrt(3)/2)
s=3000 #factor de escalamiento, dice que tan alejados estan los puntos desde su origen, mientras mas alto el numero, menor es la variacion
osi=int(os/2) #offset de un lado transformado a int
random.seed(1)

#coordenadas de la reticula
for i in range(0,ny):
    for j in range(0,nx):
        if i%2==0:
            coordenadas=(osi+int(dx/2)+dx*j+int(random.uniform(-dx/s, dx/s)),osi+int(dy/3)+dy*i+int(random.uniform(-dy/s, dy/s)),random.uniform(0,360))
            c.append(coordenadas)
        else:
            coordenadas=(osi+int(dx)+dx*j+int(random.uniform(-dx/s, dx/s)),osi+int(dy/3)+dy*i+int(random.uniform(-dy/s, dy/s)),random.uniform(0,360))
            c.append(coordenadas)
print(len(c),'elementos de c')       
n=int(len(c)/10)
nobj=50 #representa al numero total de puntos
ndel=len(c)-nobj
print(ndel,'numero de elementos a borrar')

for a in range(0,ndel):
    b=int(random.uniform(0,len(c)))
    del c[b]
    
print(len(c),'longitud deseada de c')


r=25 #radio de los chevibot
print(len(c),'elementos de c')


#crea una lista que contiene las coordenadas de los marcadores
puntos=[]
for p in c:
    cor= [(p[0]+r*math.cos(math.radians(p[2])),p[1]+r*math.sin(math.radians(p[2]))),(p[0]+r*math.cos(math.radians(p[2])-math.radians(130)),p[1]+r*math.sin(math.radians(p[2])-math.radians(130))),(p[0]+r*math.cos(math.radians(p[2])+math.radians(130)),p[1]+r*math.sin(math.radians(p[2])+math.radians(130)))]
    puntos.append(cor)
    #print(cor, 'coordenadas de los puntos')
    #print(len(cor), type(cor), cor[0][0], cor[1][1], cor[2][0])
#print(len(puntos), type(puntos), puntos)



#el siguiente codigo prueba la reconstruccion a partir de los puntos del circumcirculo, los cuales estan distribuidos en un triangulo isoceles



#el siguiente codigo crea los objetos chevibot a partir de las coordenadas de los triangulos
CB=[]
i=1
for z1 in puntos:
    p1=z1[0]
    p2=z1[1]
    p3=z1[2]
    obj=str(i)
    chevi=fig.Chevibot(p1, p2, p3, pantalla,'funcionando', obj)
    CB.append(chevi)
    i=i+1

#bloque para designar a los objetos que parten detenidos
''' 
#al invocar al siguiente bloque se detienen los bots definidos por el usuario   
CB[5].actualizarestado()
CB[15].actualizarestado()
CB[3].actualizarestado()
'''
'''    
#al invocar al siguiente bloque se detienen bots aleatorios, segun parametros definidos por el usuario
ns=1    #numero de bots detenidos al inicio de la simulacion
for j in range(0,ns):
    b=int(random.uniform(0, len(CB)))
    CB[b].actualizarestado()
'''
CB[5].actualizarestado('detenido') #se tiene un objeto detenido de prueba
#bloque condicional para determinar movimiento de los bots  
cte=int(2*L/r) #numero de radios que estan dentro del alcance de cada bot
dl=int(cte*r*1.2) #distancia de interaccion de los bots, este parametro es lo que se usa para resolver el problema de los vecinos cercanos
rd=2*r+r/3 #distancia a la cual no pueden acercarse los bots, se usa para evitar colisiones
print('valor de dl es', dl)

ra=2*r+r/3

while True:      
    t1=time.clock() 
    tiempo0=time.clock()
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            break
    
    A=[]
    B=[]
    ORI=[]
    G=[]
    vecinos=[]
    pygame.draw.line(pantalla, BLANCO, (osi, osi), (osi+Lx, osi), 1)
    pygame.draw.line(pantalla, BLANCO, (osi, osi), (osi, osi+Ly), 1)
    pygame.draw.line(pantalla, BLANCO, (osi+Lx, osi), (osi+Lx, osi+Ly), 1)
    pygame.draw.line(pantalla, BLANCO, (osi, osi+Ly), (osi+Lx, osi+Ly), 1)
    
    
    #este bloque dibuja a los bots
    for i in range(0,len(CB)):   
        CB[i].dibujar()
        ang=CB[i].angulos()
        ori=CB[i].orientacion65(ang)
        ORI.append(ori)
        ap=CB[i].circumcentro()
        a=(ap[0], ap[1])
        A.append(a)
        b=ap[2]
        B.append(b)
        CB[i].dibujarlrd1(a, b, ori)
        CB[i].dibvect1(a,b, ori)
        d=CB[i].getdibvect1(a,b, ori)
        CB[i].dibujarcir(ap)
        CB[i].dibestado(a, int(b/4))
        CB[i].dibcentro(a,b)
        g=CB[i].angorientacion(a, ori)
        G.append(g)
        

    #bloque que indica los vecinos, en otras palabras cuales bots interactuan entre si
    for i in range(0,len(CB)):
        x1=A[i][0]
        y1=A[i][1]
        j=0
        for j in range(0,len(CB)):
            x2=A[j][0]
            y2=A[j][1]
            distancia=math.sqrt((x1-x2)**2+(y1-y2)**2)
            #codigo para verificar distancias e indices
            #print('valor i', i, 'valor j',j)
            #print('coordenadas i', A[i][0], A[i][1], 'coordenadas j', A[j][0], A[j][1])
            #print('distancia i, j', distancia, 'distancia de interaccion', dl)
            if distancia < dl:
                if i==j:
                    pass
                #elif j>i-1:
                    #   pass
                else:
                    nn=[i,j, distancia]
                    vecinos.append(nn) 
                    #print('valor radio interaccion',dl, 'valor distancia', distancia)           
    #codigo para verificar los vecinos
    print(vecinos)
    print('numero pares de vecinos', len(vecinos))
    print('valor de las coordenadas',A)
    
    #este bloque reordena los vecinos en una lista que muestra el indice del bot seguido de que vecinos tiene
    #adicionalmente se crea una lista similar que en lugar de contener el indice contiene la distancia, la cual sirve para detectar las colisiones
    lvecinos=[]
    lvecinosD=[]
    for i in range(0,len(CB)):
        
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
    
    pygame.draw.circle(pantalla, (0,100+int(155/(i+1)),0), (A[3]), dl,1)
    #bloque condicional
    de=[]#indice del bot detenido
    #actualiza estados de los bots
    for i in range(0,len(lvecinos)):
        #esta linea genera una lista con los indices de todos los bots detenidos
        if CB[i].getestado()=='detenido':
            de.append(i)
        #esta linea actualiza los estados de los bots en funcionando y sin vecinos, segun el radio de interaccion del bot i
        else:
            #print('valor i',i)
            #pygame.draw.circle(pantalla, (0,100+int(155/(i+1)),0), (A[i]), dl,1)
            z2=0
            for h in range (0,len(lvecinos[i][1])):
                b=lvecinos[i][1][h]
                if CB[b].getestado()=='detenido':
                    z2=1
            #print(i, z2,' valores del bot i y de z2')
            if z2!=1:
                CB[i].actualizarestado('sin vecinos')
            else:
                CB[i].actualizarestado('funcionando')
    
    #codigo para verificar colisiones y actualizar estado a espera
   
           
                
    #codigo para detectar colisiones
    
        
    for n1 in range(0, len(lvecinos)):
        if CB[n1].getestado()=='detenido':
            pass
        else:
            for m1 in range(0, len(lvecinosD[n1][1])):
                #print(len(lvecinosD),len(lvecinosD[n1][1]) )
                #print(lvecinosD[n1][1][m1])
                if lvecinosD[n1][1][m1]<ra:# and CB[m1].getestado=='funcionando':
                    CB[n1].actualizarestado('con vecinos')
                #elif lvecinosD[n1][1][m1]<ra:# and CB[m1].getestado=='sin vecinos':
                #    CB[n1].actualizarestado('con vecinos')
                
    #instrucciones segun estado de los bots
    
    for i in range(0,len(CB)):
        text = font.render(str(i), True, (0, 128, 0))
        pantalla.blit(text,(A[i][0], A[i][1]))
        if CB[i].getestado()=='detenido':
            pass
        elif CB[i].getestado()=='sin vecinos':
            CB[i].dibrotacion(A[i], B[i], ORI[i],1, 1)
            CB[i].rotar(A[i], 1) 
            CB[i].mover(G[i])
            
            ''' bloque de prueba que controla el movimiento de lso bots en el estado sin vecinos
            rmov=int(random.uniform(0,3))
            print(rmov,'valor random de movimiento')
            if rmov==0:
                CB[i].dibrotacion(A[i], B[i], ORI[i],0, 1)
                CB[i].rotar(A[i], 0) 
                CB[i].mover(G[i])
            elif rmov==1:
                CB[i].dibrotacion(A[i], B[i], ORI[i],1, 1)
                CB[i].rotar(A[i], 1) 
                CB[i].mover(G[i])
            elif rmov==2:
                CB[i].dibavance(A[i], B[i], ORI[i], 1)
                CB[i].mover(G[i]) 
            '''  
        #elif CB[i].getestado()=='con vecinos':
        #    pass
            
        elif CB[i].getestado()=='funcionando':
            pygame.draw.circle(pantalla, (0,100+int(155/(i+1)),0), (A[i]), dl,1)
            aux=(500000,5000000) #se escoge un numero bastante alto para inicializar la comparacion
            for j1 in range (0,len(de)):
                if CB[i].getestado()=='funcionando':
                    aa=de[j1]
                    #print(i, j1, aa, CB[i].getestado())
                    a1=CB[i].compdisan(A[i],ORI[i], CB[aa])
                    if aux[0] < a1[0]:
                            aux=aux
                            aux2=aux
                    else:
                        aux=CB[i].compdisan(A[i],ORI[i], CB[aa])
                        aux2=CB[aa].compdisan(A[aa],ORI[aa], CB[i])
                    
                    #print(math.degrees(g))
                    #print(aux[0], math.degrees(aux[1]))
                    #print(G[i], 'valor de gi para el bot',i)
            
            if aux[1]<=math.pi and aux[1]>math.radians(5) and aux[0]>rd :
                CB[i].dibrotacion(A[i], B[i], ORI[i],aux[2], aux2[2])
                CB[i].rotar(A[i],aux[2])
                CB[i].mover(G[i])
                   
            elif aux[0]>rd:
                CB[i].dibavance(A[i], B[i], ORI[i], 1)
                CB[i].mover(G[i])        
            if aux[0]<rd+1: #se coloca un numero mayor, de forma que los bots se detengan antes de chocar con el bot detenido
                CB[i].actualizarestado('detenido')
            
            else:
                pass   
            
            
        elif CB[i].getestado()=='con vecinos':
            print('valor de i', i)
            v2=NONE
            #pygame.draw.circle(pantalla, (0,100+int(155/(i+1)),0), (A[i]), dl,1)
            aux=(500000,5000000) #se escoge un numero bastante alto para inicializar la comparacion
            disc=500000#se usa un valor grande para comparar las distancias
            for e in range(0, len(lvecinos[i][1])):
                v1=lvecinos[i][1][e]
                if CB[v1].getestado()=='con vecinos':
                    if disc < lvecinosD[i][1][e]:
                        disc=disc
                    else:
                        disc=lvecinosD[i][1][e]
                        v2=lvecinos[i][1][e]
            if v2==NONE:
                pass
            else:        
                print(CB[v2].getestado(),v2, 'valor del vecino detenido', i, 'valor del i bot detenido',len(lvecinos[i][1]),'numero de vecinos de i' )
            #codigo para evitar que suceda el error de indices repetidos
            if i ==v2 or v2==NONE:
                pass
            else:
                ac=CB[i].angcol(A[i],A[v2])
                av=CB[i].vectper(A[i],A[v2],ac)
                av=CB[i].dirav(A[i],ORI[i],av,B[i])
                apo=CB[i].compapo(A[i],ORI[i],av,B[i])
                ac1=CB[v2].angcol(A[v2],A[i])
                av1=CB[v2].vectper(A[v2],A[i],ac1)
                av1=CB[v2].dirav(A[v2],ORI[v2],av1,B[v2])
                if apo<math.radians(90):
                    rot=0
                else:
                    rot=1
                for j2 in range (0,len(de)):
                    #print(len(de), 'largo de', de, 'valor de', math.degrees(apo), 'angulo entre la perpendicular y la orientacion')
                    #print(math.degrees(av), math.degrees(av1),math.degrees(av-av1),math.degrees(ac), math.degrees(ac1), math.degrees(ac-ac1))
                    if CB[i].getestado()=='con vecinos':
                        aa=de[j2]
                        #print(i, j2, aa, CB[i].getestado())
                        a1=CB[i].compdisan(A[i],ORI[i], CB[aa])
                        if aux[0] < a1[0]:
                                aux=aux
                                aux2=aux
                        else:
                            aux=CB[i].compdisan(A[i],ORI[i], CB[aa])
                            aux2=CB[aa].compdisan(A[aa],ORI[aa], CB[i])
                            print('valor aux', aux)
                print('el angulo es',math.degrees(ac))       
                        #print(math.degrees(g))
                        #print(aux[0], math.degrees(aux[1]))
                        #print(G[i], 'valor de gi para el bot',i)
                
                if aux[1]<=math.pi and aux[1]>math.radians(5) and aux[0]>rd :
                    CB[i].dibrotacion(A[i], B[i], ORI[i],rot, 1)
                    CB[i].mover(av)
                    CB[i].rotar(A[i],rot)
                    CB[i].dibvectper(A[i],A[v2],av,ac,B[i])
                    CB[v2].dibvectper(A[v2],A[i],av1,ac1,B[v2])

                       
                elif aux[0]>rd:
                    CB[i].dibavance(A[i], B[i], ORI[i], rot)
                    CB[i].mover(av)        
                if aux[0]<rd:
                    CB[i].actualizarestado('detenido')
                
                else:
                    pass 
    t2=time.clock()
    #muestra los tiempos de calculo
    print('el tiempo es',t2-t1, 'segundos')
    print('esto equivale a', 1/(t2-t1),'fps')
        
        
       
        
    
    #pygame.image.save(pantalla, "screenshot.jpeg")
    pygame.display.flip()
    my_clock.tick(24) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()