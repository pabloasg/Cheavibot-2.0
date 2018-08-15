import pygame
import math
import os
import bot
import figuras
import random
import time

'''
pruebas que junta todas las etapas del programa
'''


#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

Lx=1600
Ly=1000
pygame.init()
dimensiones = [Lx, Ly]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Self Assembly, prueba con todas las partes unidas')
NEGRO= (0,0,0)
BLANCO=(255,255,255)

font = pygame.font.SysFont("arial", 20)


B=[]
l=20
r=25
n2=50
nx=int(math.sqrt(n2))
ny=int(n2/nx)


L=600
ofx=200
ofy=400
f1=figuras.circulo(pantalla, (500,680), (ofx+L/2, ofy), r)
f2=figuras.estrella5(pantalla, (ofx,ofy), L,L, 1)
t1=figuras.Ctest(pantalla,(500,500), 50)

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
            alpha=math.pi*7/4#random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, False, '*', 'detenido',0)
            B.append(b1)
        else:
            #coordenadas=(200+int(dx)+dx*j , 200+int(dy/2)+dy*i)#coloca los bots de la segunda liena a la derecha
            coordenadas=(ofx+dx*j-r+L/2 , ofy+int(dy/2)-dy*i)#coloca los bots de la segunda linea a la izquierda
            vel=5#random.uniform(0,10)
            alpha=math.pi*7/4#random.uniform(0,2*math.pi)
            b1=bot.coin(pantalla, (coordenadas[0],coordenadas[1]), r, vel, alpha, '123', '*', 'detenido',0)
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
'''
para el algoritmo de gradiente se ocupa un radio de interaccion menor
este radio tiene un valor de 3*r
'''
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
    #if B[i].getgrad()<=2:
    #    pass
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
contadorpack=-1
contadorfigura=1
mov=[]
fun=[]
direcciones={}
mul=2.9
contador=[]
cfigura=[]
for i in range(0, len(B)):
    contador.append(0)
    cfigura.append('1')

tac=0
while True:
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO)
    t0=time.clock()
    
    contadorpack=contadorpack+1
    if contadorpack==700:
        print('contador pack reiniciado')
        contadorpack=0
        
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        pygame.quit()
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            pygame.quit()
            
    f1.dibujarcir()
    #f2.dibstar5()
    #t1.dibujar()
    pos=pygame.mouse.get_pos()
    t1.actualizarpos(pos[0], pos[1])
    a=t1.getpos()
    
    #comparacion=f2.comp(a[0][0], a[0][1], a[1])
    comparacion=f1.compC(a[0][0], a[0][1], a[1])
    
    if comparacion==True:
        #print('el objeto esta dentro')
        pygame.draw.circle(pantalla, (255,0,0), (850,850), 25, 0)
    else:
        #print('el objeto esta fuera')
        pygame.draw.circle(pantalla, (0,0,255), (850,850), 25, 0)
        
    #dibujar bots 
    for i in range(0, len(B)):
        B[i].dibujar()
        #B[i].dibvel(5)
        B[i].dibseed()
        #B[i].dibgrad()
        B[i].dibestado()
        #imprime la ID del bot
        #bot=str(i)
        #grad=font.render(bot, True, (255,255,255))
        #a=B[i].getdatpos()
        #pantalla.blit(grad, (a[0][0]-15, a[0][1]-25))
        
    #mover bots
    z=(0,-1)
    
    if contadorpack==0:
        grad=[]
        print(fun, 'bots con estado funcionando')
        for i in range(0, len(B)):
            if B[i].getestado()=='funcionando' or B[i].getestado()=='moviendose' or B[i].getestado()=='fijo' or B[i].getestado()=='figura':
                pass
            else:
                z=(B[i].getgrad(),i)
            grad.append(z)
        c=max(grad)
        '''
        luego hay que cambiar esta parte para que se guarde el valor del gradiente maximo, junto con los bots que tienen ese gradiente,
        la idea es una vez se determina el gradiente mayor, tener una coleccion de k bots que tienen ese valor
        y luego usar algun metodo para escoger al bot que se mueve
        '''
        print(c, 'elemento que sera el proximo en moverse')
        if c in fun:
            pass
        else:
            B[c[1]].modestado('funcionando')
            if len(lvecinos[c[1]][1])==0:
                cen=B[c[1]].getdatpos()
                xcp=cen[0][0]
                ycp=cen[0][1]
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
                    if x<x2[0]-1.2*r and x>x1[0]+1.2*r:
                        xmov=0
                    elif x<x2[0]-1.2*r and x<=x1[0]+1.2*r:
                        xmov=-1
                    elif x>x2[0]-1.2*r and x>x1[0]+1.2*r:
                        xmov=1
                    else:
                        xmov=0
                    #mov en y
                    
                    if y<y2[0] and y>y1[0]:
                        ymov=0
                    elif y<y2[0]-1.6*r and y<=y1[0]+1.6*r:
                        ymov=-1
                    elif y>y2[0]-1.6*r and y>y1[0]+1.6*r:
                        print(y2[0]-1.6*r, y1[0]+1.6*r, y)
                        ymov=1
                    else:
                        ymov=0
                    direcciones[c[1]]=xmov, ymov
                    print(direcciones, 'direcciones')
                        
                        
                    
                    
                    
    fun=[]
    
    for i in range(0, len(B)):
        estado=B[i].getestado()
        if estado=='funcionando':
            fun.append(i)
                
        #print(fun, 'elementos funcionando')
        #print(direcciones, 'direcciones')
        
   
    #codigo para separar al bot del pack
    for elem in fun:
        a=elem#este es el indice del bot
        
        #pygame.image.save(pantalla, 'self assembly.jpeg')
        if (a in direcciones)==True: 
            cenele=B[a].getdatpos()
            dire=direcciones[a]
            xcp=5*r*dire[0]+cenele[0][0]
            ycp=5*r*dire[1]+cenele[0][1]
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
            #print(distancia2, 'esta es la distancia 2', 'valor de a = ', a)
            #print(posa[0], posi[a], distancia2, 'datos posicion')
            
            if alphacom>math.radians(10) and dirmov==-1 and distancia2<(3*r):
                B[a].rotar(0)   
            elif alphacom>math.radians(10) and dirmov==1 and distancia2<(3*r):
                B[a].rotar(1)   
            elif alphacom<math.radians(10) and distancia2<(3*r):
                B[a].mover()
            elif distancia2>=3*r:
                B[a].modestado('moviendose')
        else:
            pass
            
    '''
    codigo para mover hacia la figura
    '''
    
    bf=[]#bot que estan fijos
    bm=[]#bot que se estan moviendo
    for i in range (0, len(B)):
        if B[i].getestado()=='fijo' or B[i].getestado()=='detenido':
            indicef=i
            bf.append(indicef)
        elif B[i].getestado()=='moviendose' or B[i].getestado()=='figura': 
            indice=i
            bm.append(indice)
        else:
            pass
    
    for i in bf:
        posb=B[i].getdatpos()
        #pygame.draw.circle(pantalla, BLANCO, (int(posb[0][0]), int(posb[0][1])), r, 1)
        #pygame.draw.circle(pantalla, (0,255,0), (int(posb[0][0]), int(posb[0][1])), int(mul*r), 1)
        #bot=str(i)
        #grad=font.render(bot, True, (255,255,255))
        #a=posb[0]
        #pantalla.blit(grad, (a[0]-15, a[1]-25))

    #pygame.draw.circle(pantalla, BLANCO, (centro), r, 1)
    #pygame.draw.circle(pantalla, (0,255,0), (centro), 3*r, 1)
    
    #c2=(100,800)
    #R=50
    #pygame.draw.circle(pantalla, BLANCO, (c2), R, 1)
    #pygame.draw.circle(pantalla, (255,0,0), (c2), 4*R, 1)
    
    #codigo para comprobar si c1 ha entrado a la figura
    for z in bm:
        #B[z].dibvel(5)
        c1pos=B[z].getdatpos()
        #distancia=math.sqrt((c1pos[0][0]-c2[0])**2+(c1pos[0][1]-c2[1])**2)
        comparacion=f1.compC(c1pos[0][0], c1pos[0][1], r)
        
        if comparacion==True and cfigura[z]=='out':
            contador[z]=contador[z]+1
        elif comparacion==True and cfigura[z]=='in':
            contador[z]=contador[z]
        if comparacion==True and B[z].getestado()!='fijo':
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
        
        
        #print(cfigura[z], ',contador = ', contador[z], B[z].getestado(), 'antes, bot ', z)
        
        #codigo para identificar gradiente de los vecinos del bot
        gr=0
        z1=0
        for i in bm:
            est=B[i].getestado()
            vecinosG=[]
            auxv=[]
            Ci=B[i].getdatpos()
            if est=='moviendose' or est=='figura':
                pygame.draw.circle(pantalla, (255,0,255), (int(Ci[0][0]), int(Ci[0][1])), int(Ci[1]*(mul+1)), 1)
                for j in range(0, len(B)):
                    #print('valor j ',j,', valor i ', i)
                    if i==j:
                        pass
                    else:
                        Cj=B[j].getdatpos()
                        distancia2=(Ci[0][0]-Cj[0][0])**2+(Ci[0][1]-Cj[0][1])**2
                        radio2=(Ci[1]*(mul+1))**2
                        if distancia2<=radio2:
                            auxv.append(j)
                        else:
                            pass
                a=[i,auxv]
                vecinosG.append(a)
                #print('vecinos de j ',j, ' son: ', vecinosG)
                compv=[]
                compvdic={}
                
                if len(vecinosG[0][1])>0:
                    for h in range(0, len(vecinosG[0][1])):
                        aux1=vecinosG[0][1][h]
                        a=B[aux1].getgrad()
                        compv.append(a)
                        compvdic.update({a:aux1})
                    gr=max(compv)
                    z1=int(compvdic[gr])
                    
        
       
        pos1=B[z].getdatpos()
        pos2=B[z1].getdatpos()
        
        distanciavec=math.sqrt((pos1[0][0]-pos2[0][0])**2+(pos1[0][1]-pos2[0][1])**2)
        print(B[z].getcontador(),contadorfigura,'contadores')       
        print(distanciavec,mul*r,'distancias', z, z1, 'zetas', len(bm))
        if aux=='moviendose' and B[z].getcontador()==contadorfigura:
            B[z].modestado('fijo')
            print('1')
        
        elif aux=='figura' and B[z].getcontador()==contadorfigura and distanciavec <(mul-1)*r:
            B[z].modestado('fijo')
            print('2')
            
        elif aux=='figura' and B[z].getcontador()==contadorfigura and B[z].getgrad()==gr and distanciavec<=mul*r:
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
            
            
    for i in range(0, len(B)):
        est=B[i].getestado()
        vecinosG=[]
        auxv=[]
        Ci=B[i].getdatpos()
        if est=='moviendose' or est=='figura':
            pygame.draw.circle(pantalla, (255,0,255), (int(Ci[0][0]), int(Ci[0][1])), int(Ci[1]*(mul+1)), 1)
            for j in range(0, len(B)):
                #print('valor j ',j,', valor i ', i)
                if i==j:
                    pass
                else:
                    Cj=B[j].getdatpos()
                    distancia2=(Ci[0][0]-Cj[0][0])**2+(Ci[0][1]-Cj[0][1])**2
                    radio2=(Ci[1]*(mul+1))**2
                    if distancia2<radio2:
                        auxv.append(j)
                    else:
                        pass
            a=[i,auxv]
            vecinosG.append(a)
            #print('vecinos de j ',j, ' son: ', vecinosG)
            compv=[]
            
            if len(vecinosG[0][1])>0:
                for h in range(0, len(vecinosG[0][1])):
                    a=B[vecinosG[0][1][h]].getgrad()
                    compv.append(a)
                gr=min(compv)
                B[i].modgrad(gr+1)
    
    #my_clock.tick(10000) #FPS de la ventana y tambien de la actualizacion de los datos
    tf=time.clock()
    tp=tf-t0
    print('tiempo =', round(tp*1000), ' milisegundos')
    print('fps =', round(1/tp,1))
    texto='el tiempo en ms es: '+str(round(tp*1000))+' lo que equivale a '+str(round(1/tp,1))+' FPS'
    tfps=font.render(texto, True, (255,0,255))
    pantalla.blit(tfps, (851,150))
    tac=tac+tp
    print('tiempo =', round(tac*1000), ' milisegundos')
    texto='el tiempo  acumulado en segundos es: '+str(round(tac,1))+' seg'
    tfps=font.render(texto, True, (255,0,255))
    pantalla.blit(tfps, (851,250))
    
    
    pygame.display.flip()
    
    #print('contador = ',contadorpack)
    
    
    '''
    #codigo para verificar el tiempo de ejecucion del programa
    tf=time.clock()
    tiempo=(tf-t0)
    print('tiempo en segundos = ', tiempo)
    print('tiempo en milisegundos = ', tiempo*1000)
    print('cantidad de fps = ', 1/tiempo)
    '''
    #name=('condicion inicial '+str(n2)+' elementos'+'.jpeg')
    #pygame.image.save(pantalla, name)
    #break
    #datcir=f1.circulo()
    #print('datos circulo', datcir)
    #print('el radio del circulo es ', datcir[1]/r, ' veces el radio del bot')
pygame.quit() 

