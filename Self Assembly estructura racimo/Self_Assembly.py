import fig
import pygame
import math
import time
import random
import os

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




#parametros de la reticula
c=[]
L=200
nx=int(Lx/L)
ny=int(Ly/(L*math.sqrt(3)/2)+1)
dx=int(L)
dy=int(L*math.sqrt(3)/2)
s=3000 #factor de escalamiento, dice que tan alejados estan los puntos desde su origen, mientras mas alto el numero, menor es la variacion
osi=int(os/2) #offset de un lado transformado a int

#coordenadas de la reticula
for i in range(0,ny):
    for j in range(0,nx):
        if i%2==0:
            coordenadas=(osi+int(dx/2)+dx*j+int(random.uniform(-dx/s, dx/s)),osi+int(dy/2)+dy*i+int(random.uniform(-dy/s, dy/s)),random.uniform(0,360))
            c.append(coordenadas)
        else:
            coordenadas=(osi+int(dx)+dx*j+int(random.uniform(-dx/s, dx/s)),osi+int(dy/2)+dy*i+int(random.uniform(-dy/s, dy/s)),random.uniform(0,360))
            c.append(coordenadas)
print(len(c),'elementos de c')       
n=int(len(c)/10)
nobj=30 #representa al numero total de puntos
ndel=len(c)-nobj
print(ndel,'numero de elementos a borrar')
for a in range(0,ndel):
    b=int(random.uniform(0,len(c)))
    del c[b]
    
print(len(c),'longitud deseada de c')


r=30 #radio de los chevibot
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
CB[10].actualizarestado('detenido') #se tiene un objeto detenido de prueba
#bloque condicional para determinar movimiento de los bots  
cte=int(2*L/r) #numero de radios que estan dentro del alcance de cada bot
dl=int(cte*r*1.0) #distancia de interaccion de los bots, este parametro es lo que se usa para resolver el problema de los vecinos cercanos
rd=2*r+r/2 #distancia a la cual no pueden acercarse los bots, se usa para evitar colisiones
print('valor de dl es', dl)

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
                    nn=(i,j, distancia)
                    vecinos.append(nn) 
                    #print('valor radio interaccion',dl, 'valor distancia', distancia)           
    #codigo para verificar los vecinos
    print(vecinos)
    print('numero pares de vecinos', len(vecinos))
    print(A)
    
    
    #bloque condicional
    de=[]#indice del bot detenido
    
    for i in range(0,len(CB)):
        if CB[i].getestado()=='detenido':
            de.append(i)
    for i in range(0,len(CB)):
        if CB[i].getestado()=='detenido':
            pass
        else:
            #print('valor i',i)
            pygame.draw.circle(pantalla, (0,100+int(155/(i+1)),0), (A[i]), dl,1)
            aux=(500000,5000000) #se escoge un numero bastante alto para inicializar la comparacion
            for j in range (0,len(de)):
                if CB[i].getestado()=='funcionando':
                    a=de[j]
                    a1=CB[i].compdisan(A[i],ORI[i], CB[a])
                    if aux[0] < a1[0]:
                        aux=aux
                        aux2=aux
                    else:
                        aux=CB[i].compdisan(A[i],ORI[i], CB[a])
                        aux2=CB[a].compdisan(A[a],ORI[a], CB[i])
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
            if aux[0]<rd:
                CB[i].actualizarestado('detenido')
            
            else:
                pass
            
            t2=time.clock()
    print('el tiempo es',t2-t1, 'segundos')
    print('esto equivale a', 1/(t2-t1),'fps')
        
        
       
        
       
    pygame.display.flip()
    my_clock.tick(60) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()