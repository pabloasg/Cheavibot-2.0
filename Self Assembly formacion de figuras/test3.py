import math
import pygame
import figuras
import os
import bot
import random
'''
test 3, el objetivo es probar como los bots salen del pack y siguen por la esquina, para posteriormente entrar a la figura
'''

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

L=600
ofx=200
ofy=400

f2=figuras.estrella5(pantalla, (ofx,ofy), L,L, 1)



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
        b1=bot.coin(pantalla, (x,y), r, vel, alpha, False, '1')
        B.append(b1)
   
'''

#arreglo ordenado de bots en reticula hexagonal
dx=2*r
dy=int(2*r*math.sqrt(3)/2)
for i in range(0,ny):
    for j in range(0,nx):
        if i%2==0:
            coordenadas=(ofx+int(dx/2)+dx*j-r+L/2 , ofy+int(dy/2)-dy*i)
            vel=5#random.uniform(0,10)
            alpha=random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, False, '*', 'detenido',0)
            B.append(b1)
        else:
            #coordenadas=(200+int(dx)+dx*j , 200+int(dy/2)+dy*i)#coloca los bots de la segunda liena a la derecha
            coordenadas=(ofx+dx*j-r+L/2 , ofy+int(dy/2)-dy*i)#coloca los bots de la segunda linea a la izquierda
            vel=5#random.uniform(0,10)
            alpha=random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, '123', '*', 'detenido',0)
            B.append(b1)
            



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


'''
para el algoritmo de gradiente se ocupa un radio de interaccion menor
este radio tiene un valor de 3*r
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
    
#asignacion de gradiente a los bots
while True:    
    comp=[]
    for i in range(0, len(B)):
        H=[]
        
        for j in range(0, len(lvecinos[i][1])):
            a=B[lvecinos[i][1][j]].getgrad()
            H.append(a)
        b=min(H)
        if (B[i].getseed())==True:
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
            
#inicializa el contador y los estados
for i in range(0, len(B)):
    B[i].compestado()
    B[i].compcontador()

  
#guarda la posicion inicial de los bots
posi=[]
for i in range(0, len(B)):
    aux=B[i].getdatpos()
    x=aux[0][0]
    y=aux[0][1]
    posi.append((x,y))
        
        
paso=1000
contador=-1
mov=[]
fun=[]
direcciones={}
for k in range(0, paso):
    contador=contador+1
    if contador==10:
        print('contador reiniciado')
        contador=0
    for h in range(0, len(B)):
       
        my_clock = pygame.time.Clock()
        pantalla.fill(NEGRO)
        
        ev = pygame.event.poll() # Look for any event
        if ev.type == pygame.QUIT: # Window close button clicked?
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
      
                
        
        f2.dibstar5()
        f2.dibujarS()
        
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
            
        
                
        for i in range(0, len(B)):
            pygame.draw.circle(pantalla, (0,255,0), (int(A[h][0]), int(A[h][1])), 4*r, 1)
         
        #dibujar bots   
        for i in range(0, len(B)):
            B[i].dibujar()
            B[i].dibvel(10)
            B[i].dibseed()
            B[i].dibgrad()
            B[i].dibestado()
            #imprime la ID del bot
            bot=str(i)
            grad=font.render(bot, True, (255,255,255))
            a=B[i].getdatpos()
            pantalla.blit(grad, (a[0][0]-15, a[0][1]-25))
            
        #mover bots
        z=(0,-1)
        if h==len(B)-1:
            if contador==0:
                grad=[]
                print(fun, 'bots con estado funcionando')
                for i in range(0, len(B)):
                    if B[i].getestado()=='funcionando' or B[i].getestado()=='moviendose' or B[i].getestado()=='fijo':
                        pass
                    else:
                        z=(B[i].getgrad(),i)
                    grad.append(z)
                c=max(grad)
                print(c, 'elemento que sera el proximo en moverse')
                if c in fun:
                    pass
                else:
                    B[c[1]].modestado('funcionando')
                    if len(lvecinos[c[1]][1])==0:
                        cen=B[c[1]].getdatpos()
                        xcp=cen[0][0]
                        ycp=cen[0][1]
                        print('esta linea se ejecuto y es un error plop')
                    else:
                        #x=0
                        #y=0
                        posx=[]
                        posy=[]
                        for j in range(0, len(lvecinos[c[1]][1])):
                            k=lvecinos[c[1]][1][j]
                            print(lvecinos[c[1]][1],'vecinos')
                            if B[k].getestado()=='funcionando' or B[k].getestado()=='moviendose':
                                print(k, 'paso')
                            else:
                                if lvecinosD[c[1]][1][j]<2.2*r:
                                    cen=B[k].getdatpos()
                                    x=cen[0][0]
                                    y=cen[0][1]
                                    posx.append((x,k))
                                    posy.append((y,k))
                        if len(posx)!=0 and len(posy)!=0: 
                            print(posx, posy, 'posiciones y vecinos')
                            x2=max(posx)
                            x1=min(posx)
                            y2=max(posy)
                            y1=min(posy)
                            cen=B[c[1]].getdatpos()
                            x=cen[0][0]
                            y=cen[0][1]
                            #mov en x
                            if x<x2[0]-r and x>x1[0]+r:
                                xmov=0
                            elif x<x2[0]-r and x<=x1[0]+r:
                                xmov=-1
                            elif x>x2[0]-r and x>x1[0]+r:
                                xmov=1
                            else:
                                xmov=0
                            #mov en y
                            
                            if y<y2[0] and y>y1[0]:
                                ymov=0
                            elif y<y2[0]-1.7*r and y<=y1[0]+1.7*r:
                                ymov=-1
                            elif y>y2[0]-1.7*r and y>y1[0]+1.7*r:
                                print(y2[0]-1.7*r, y1[0]+1.7*r, y)
                                ymov=1
                            else:
                                ymov=0
                            direcciones[c[1]]=xmov, ymov
                            print(direcciones, 'direcciones')
                        
                        
                    
                    
                    
        fun=[]
        if h==len(B)-1:
            for i in range(0, len(B)):
                estado=B[i].getestado()
                if estado=='funcionando':
                    fun.append(i)
                    
            #print(fun, 'elementos funcionando')
            #print(direcciones, 'direcciones')
            
        if h==len(B)-1:
            #codigo para separar al bot del pack
            for elem in fun:
                a=elem#este es el indice del bot
                
                #pygame.image.save(pantalla, 'self assembly.jpeg')
                if (a in direcciones)==True: 
                    cenele=B[a].getdatpos()
                    dire=direcciones[a]
                    xcp=3*r*dire[0]+cenele[0][0]
                    ycp=3*r*dire[1]+cenele[0][1]
                    #print(xcp, ycp, a, 'valores', fun, direcciones)
                    vl=B[a].getvel()
                    ang=B[a].getang()
                    p1=(vl*math.cos(ang), vl*math.sin(ang))
                    p2=(0,0)
                    p3=(xcp-cenele[0][0],ycp-cenele[0][1])
                    
                    #pygame.draw.circle(pantalla, (0,255,0), (int(xc), int(yc)), 5, 0)
                    pygame.draw.circle(pantalla, (0,255,255), (int(xcp), int(ycp)), 5, 0)
                    
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
                    posa=B[a].getdatpos()
                    distancia2=math.sqrt((posa[0][0]-posi[a][0])**2+(posa[0][1]-posi[a][1])**2)
                    #print(posa[0], posi[a], distancia2, 'datos posicion')
                    
                    if alphacom>math.radians(10) and dirmov==-1 and distancia2<(2*r):
                        B[a].rotar(0)   
                    elif alphacom>math.radians(10) and dirmov==1 and distancia2<(2*r):
                        B[a].rotar(1)   
                    elif alphacom<math.radians(10) and distancia2<(r):
                        B[a].mover()
                    elif distancia2>=r:
                        B[a].modestado('moviendose')
                else:
                    pass
            
                    
                #B[elem[1]].mover()    
        
        
        pygame.image.save(pantalla, 'self assembly salida del pack.jpeg')
        pygame.display.flip()
        my_clock.tick(1000) #FPS de la ventana y tambien de la actualizacion de los datos
pygame.quit()