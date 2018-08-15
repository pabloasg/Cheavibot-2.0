import math
import pygame

BLANCO=(255,255,255)

class Triangulo:  #define un triangulo dados 3 puntos
    def __init__(self, p1, p2, p3, surface):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.surface =surface
        

    def dibujar(self):
        pygame.draw.polygon(self.surface, (BLANCO), (self.p1, self.p2, self.p3), 1)
    
    
    def centrotri(self):  #calcula las coordenadas del centro de un triangulo
        xc=(self.p1[0] + self.p2[0] +self.p3[0])//3
        yc=(self.p1[1] + self.p2[1] +self.p3[1])//3
        return (xc, yc)
    
    def radio1(self):  #calcula el radio de un circulo, esta funcion no es exacta
        xc=(self.p1[0] + self.p2[0] +self.p3[0])//3
        yc=(self.p1[1] + self.p2[1] +self.p3[1])//3
        r1=int(((xc-self.p1[0])**2 + (yc-self.p1[1])**2)**0.5)
        r2=int(((xc-self.p2[0])**2 + (yc-self.p2[1])**2)**0.5)
        r3=int(((xc-self.p3[0])**2 + (yc-self.p3[1])**2)**0.5)
        return (r1+r2+r3)//3
    
    def circumcentro(self):
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        d=2*(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))
        ux=(1/d)*((a[0]*a[0]+a[1]*a[1])*(b[1]-c[1])+(b[0]*b[0]+b[1]*b[1])*(c[1]-a[1])+(c[0]*c[0]+c[1]*c[1])*(a[1]-b[1]))
        uy=(1/d)*((a[0]*a[0]+a[1]*a[1])*(c[0]-b[0])+(b[0]*b[0]+b[1]*b[1])*(a[0]-c[0])+(c[0]*c[0]+c[1]*c[1])*(b[0]-a[0]))
        #ap=(a[0]-a[0], a[1]-a[1])
        bp=(b[0]-a[0], b[1]-a[1])
        cp=(c[0]-a[0], c[1]-a[1])
        dp=2*(bp[0]*cp[1]-bp[1]*cp[0])
        uxp=(1/dp)*(cp[1]*(bp[0]*bp[0]+bp[1]*bp[1])-bp[1]*(cp[0]*cp[0]+cp[1]*cp[1]))
        uyp=(1/dp)*(bp[0]*(cp[0]*cp[0]+cp[1]*cp[1])-cp[0]*(bp[0]*bp[0]+bp[1]*bp[1]))
        r=math.sqrt(uxp*uxp+uyp*uyp)
        return (int(ux), int(uy), int(r*1.2), int(uxp+a[0]), int(uyp+a[1]))
    
    def angulos(self): #calcula los 3 angulos internos del triangulo y los entrega
        a= (self.p1[0], self.p1[1])
        b= (self.p2[0], self.p2[1])
        c= (self.p3[0], self.p3[1])
        #calculo de alpha1, indice 1 corresponde al angulo del punto 1, el indice 12, representa elevado al cuadrado
        u1= (c[0]-a[0], c[1]-a[1])
        v1= (b[0]-a[0], b[1]-a[1])
        u12= (u1[0]*u1[0]+u1[1]*u1[1])**0.5
        v12= (v1[0]*v1[0]+v1[1]*v1[1])**0.5
        uv1= u1[0]*v1[0]+u1[1]*v1[1]
        alpha1=math.acos(uv1/(u12*v12))
        #calculo de alpha2
        u2= (a[0]-b[0], a[1]-b[1])
        v2= (c[0]-b[0], c[1]-b[1])
        u22= (u2[0]*u2[0]+u2[1]*u2[1])**0.5
        v22= (v2[0]*v2[0]+v2[1]*v2[1])**0.5
        uv2= u2[0]*v2[0]+u2[1]*v2[1]
        alpha2=math.acos(uv2/(u22*v22))
        #calculo de alpha3
        u3= (a[0]-c[0], a[1]-c[1])
        v3= (b[0]-c[0], b[1]-c[1])
        u32= (u3[0]*u3[0]+u3[1]*u3[1])**0.5
        v32= (v3[0]*v3[0]+v3[1]*v3[1])**0.5
        uv3= u3[0]*v3[0]+u3[1]*v3[1]
        alpha3=math.acos(uv3/(u32*v32))
        return[alpha1, alpha2, alpha3]
        
    '''las siguientes funciones comparan los angulos interiores de los triangulos y entregan el mayor o menor angulo, dependiendo del caso
    existen 2 configuraciones posibles para los marcadores, que el angulo doble del triangulo isoceles (el que se repite) sea 55grados o 65 grados, 
    en el caso de 65 grados la orientacion tiene que ir al angulo menor, en el caso de 55 grados la orientacion tiene que ir al angulo mayor
    el resultado entregado es el contador del punto, osea punto 1, punto2 o punto 3, posteriormente hay que restar 1 para que coincida la indexacion
    ''' 
    def orientacion65(self, angulos):  
        menor=math.pi
        i=1
        count=0
        for a in angulos:
            if menor > a:
                menor=a
                count=i
            else:
                menor=menor
            i=i+1
        return count
        
    def orientacion55(self, angulos):  
        mayor=0
        i=1
        count=0
        for a in angulos:
            if mayor < a:
                mayor=a
                count=i
            else:
                mayor=mayor
            i=i+1
        return count
    
    def angorientacion(self, centro, orientacion):
        xc=centro[0]
        yc=centro[1]
        xcp=centro[0]+1
        ycp=centro[1]
        po=orientacion-1
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        px=puntos[po][0]
        py=puntos[po][1]
        
        u=(px-xc, py-yc)
        v=(xcp-xc, ycp-yc)
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1] 
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        return alpha
    
    def dibujarcir1(self , a, r): #dibuja un circulo con el radio calculado en la funcion 1
        pygame.draw.circle(self.surface, (BLANCO), a, r, 1)
        
    def dibujarcir(self, datos):
        a=(int(datos[0]), int(datos[1]))
        r=datos[2]
        pygame.draw.circle(self.surface, (BLANCO), a, r, 1)
    
    def dibujarlrd1(self, pos, R, orientacion): #dibuja los circulos de las LDR, R corresponde al radio del triangulo, pos a las coordenadas del centro del triangulo
        r=R//7
        l=5
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        #p2=puntos[pc]
        p1=puntos[pc-1]
        p3=puntos[pc-2]
        p1p=(p1[0]+1, p1[1])
        
        u=(p3[0]-p1[0], p3[1]-p1[1])
        v=(p1p[0]-p1[0], p1p[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        #c1=math.degrees(alpha)
        c=alpha+math.radians(90)
        #print('angulos',c, c1) 
        #print((math.sin(c)))
        #print((math.cos(c)))     
        b1a=pos[0] + int(0.8*l*r*math.cos(c))
        b2a=pos[1] + int(0.8*l*r*math.sin(c))
        b1b=pos[0] - int(l*r*math.cos(c))
        b2b=pos[1] - int(l*r*math.sin(c))
        pygame.draw.line(self.surface, (BLANCO), pos, (b1a, b2a), 1)
        pygame.draw.line(self.surface, (BLANCO), pos, (b1b, b2b), 1)
        pygame.draw.circle(self.surface, (BLANCO), (b1a, b2a), r, 1)
        pygame.draw.circle(self.surface, (BLANCO), (b1b, b2b), r, 1)
        #print(r)
        #print(b1a, b2a, b1b, b2b)
       
        
        
          
    def dibvect1(self, centro, R, orientacion): #metodo de prueba dibuja un vector desde el centro a algun vertice
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        pygame.draw.line(self.surface, (BLANCO), centro, puntos[pc], 1)
        
    def getdibvect1(self, centro, R, orientacion): #metodo de prueba obtiene el punto desde cual se dirije hacia adelante
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        return puntos[pc]
        
    def dibcentro(self, centro, R):
        r=int(R/15)
        pygame.draw.circle(self.surface, (BLANCO), (centro), r, 0)
        

        

class Chevibot(Triangulo):
    def __init__(self, p1, p2, p3, surface, estado, obj):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.surface =surface
        self.estado=estado
        self.obj=obj
        
    def getestado(self):
        return self.estado
        
        
    def dibestado(self, pos,r):
        '''posibles estados:
        'detenido': se representa en color rojo, un bot esta detenido cuando no ejecuta mas movimientos 
        'funcionando': se representa en color azul, un bot se dice que esta funcionando cuando detecta un vecino detenido, el bot funcionando puede moverse
        'con vecinos': se representa en color verde, al entrar en este estado el bot se detiene temporalmente, es un estado para impedir colisiones, tambien se le puede denominar 'espera' a este estado
        'sin vecinos': se representa en color amarillo, un bot sin vecinos es aquel que no tiene un vecino detenido, pero si otros activos, el bot se puede mover
        '''
        if self.estado=='detenido':
            pygame.draw.circle(self.surface, (255,0,0), pos, r, 0)
        elif self.estado=='funcionando':
            pygame.draw.circle(self.surface, (0,0,255), pos, r, 0)
        elif self.estado=='sin vecinos':
            pygame.draw.circle(self.surface, (255,255,0), pos, r, 0)
        elif self.estado=='con vecinos':
            pygame.draw.circle(self.surface, (0,255,0), pos, r, 0)
        elif self.estado !='detenido ' and self.estado !='funcionando' and self.estado !='sin vecinos' and self.estado !='con vecinos':
            print(self.obj, 'este objeto no tiene asignado un estado')
            
    def composx(self, datos, obj): #metodo que compara la posicion en x del objeto 1 con un objeto 2
        x1=datos[0]
        #y1=datos[1]
        datos2=obj.circumcentro()
        x2=datos2[0]
        #y2=datos2[1]
        if math.fabs(x2-x1)<10:
            return True
        else:
            return False
        
    def composy(self, datos, obj): #metodo que compara la posicion en y del objeto 1 con un objeto 2
        #x1=datos[0]
        y1=datos[1]
        datos2=obj.circumcentro()
        #x2=datos2[0]
        y2=datos2[1]
        y3=datos2[2]*2+datos2[2]//10
        if math.fabs(y2-y1)<y3:
            return True
        else:
            return False
        
    def compang(self, angulo1, angulo2): #metodo que compara los angulos de la orientacion de un objeto 1 con un objeto 2
        n=1000000 #numero lo bastante grande para que el resultado sea 0 o 1
        difang=math.fabs(angulo2-angulo1)
        dirmov=math.ceil((angulo2-angulo1)/n)
        if math.ceil((((angulo2+math.pi)-angulo1)/n))==0:
            dirmov=1
        return(difang, dirmov)
        
    def dirmov(self, datos, obj):
        x1=datos[0]
        y1=datos[1]
        datos2=obj.circumcentro()
        x2=datos2[0]
        y2=datos2[1]
        n=1000000 #se escoge un numero suficientemente grande de modo que si el numero es positivo se redeondee a 1 y si es negativo a 0
        mx=math.ceil((x2-x1)/n)
        my=math.ceil((y2-y1)/n)
        return (mx, my)
            
            
    #los siguientes corresponden a metodos para realizar el control de los chevibots        
    def actualizarestado(self, estado):
        self.estado = estado
          
            
        
    def actualizarposx(self, mov): #actualiza la posicion de las luces guias, en primera instancia se usa sobre los marcadores en el eje x a modo de prueba 
        p=5 #tamano del paso por actualizacion
        if mov ==1:
            smov=1
        elif mov==0:
            smov=-1
        else:
            print('error')
        self.p1=self.p1[0]+p*smov, self.p1[1]
        self.p2=self.p2[0]+p*smov, self.p2[1]
        self.p3=self.p3[0]+p*smov, self.p3[1]
        
        
    def actualizarposy(self, mov): #actualiza la posicion de las luces guias, en primera instancia se usa sobre los marcadores en el eje y a modo de prueba
        p=5 #tamano del paso por actualizacion
        if mov ==1:
            smov=1
        elif mov==0:
            smov=-1
        else:
            print('error')
        self.p1=self.p1[0], self.p1[1]+p*smov
        self.p2=self.p2[0], self.p2[1]+p*smov
        self.p3=self.p3[0], self.p3[1]+p*smov
        
    def mover(self, ang):
        p=10.0/10.0
        c=math.cos(ang)
        s=math.sin(ang)
        self.p1=self.p1[0]+p*c, self.p1[1]+p*s
        self.p2=self.p2[0]+p*c, self.p2[1]+p*s
        self.p3=self.p3[0]+p*c, self.p3[1]+p*s
        
    def mover2(self, ang,a):
        p=10*a
        c=math.cos(ang)
        s=math.sin(ang)
        self.p1=self.p1[0]+p*c, self.p1[1]+p*s
        self.p2=self.p2[0]+p*c, self.p2[1]+p*s
        self.p3=self.p3[0]+p*c, self.p3[1]+p*s
        
        
    def rotar(self, centro, direcmov):
        ang=math.radians(5/2.5)#se escribe el incremento en grados, luego se transforma a radianes
        xc=centro[0]
        yc=centro[1]
        cos=math.cos(ang)
        sin=math.sin(ang)
        p1=self.p1[0], self.p1[1]
        p2=self.p2[0], self.p2[1]
        p3=self.p3[0], self.p3[1]
        if direcmov==0:
            self.p1=cos*(p1[0]-xc)+sin*(p1[1]-yc)+xc, -sin*(p1[0]-xc)+cos*(p1[1]-yc)+yc
            self.p2=cos*(p2[0]-xc)+sin*(p2[1]-yc)+xc, -sin*(p2[0]-xc)+cos*(p2[1]-yc)+yc
            self.p3=cos*(p3[0]-xc)+sin*(p3[1]-yc)+xc, -sin*(p3[0]-xc)+cos*(p3[1]-yc)+yc
        elif direcmov==1:
            self.p1=cos*(p1[0]-xc)-sin*(p1[1]-yc)+xc, +sin*(p1[0]-xc)+cos*(p1[1]-yc)+yc
            self.p2=cos*(p2[0]-xc)-sin*(p2[1]-yc)+xc, +sin*(p2[0]-xc)+cos*(p2[1]-yc)+yc
            self.p3=cos*(p3[0]-xc)-sin*(p3[1]-yc)+xc, +sin*(p3[0]-xc)+cos*(p3[1]-yc)+yc
            

    #los siguientes bloques realizan comparaciones de acuerdo a reglas del enjambre
    #la primera regla hace referencia a un objeto quieto 'detenido' y el resto funcionando al etar a cierta distancia se acoplan al objeto detenido y se detienen
    def compdisan(self, centro1, orientacion1, objeto):
        datos=objeto.circumcentro()
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion1 -1
        pori=puntos[pc]
        distancia=math.sqrt((datos[0]-centro1[0])**2+(datos[1]-centro1[1])**2)
        u=(pori[0]-centro1[0], pori[1]-centro1[1])
        v=(datos[0]-centro1[0], datos[1]-centro1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            dm=0
        else:
            dm=1
        return (distancia, alpha,dm)
        #print(distancia)
        #print(alpha, math.degrees(alpha))
        
    #bloque que dibuja las luces de control
    def dibavance(self, pos, R, orientacion, ncir):  #dibuja 1 circulo en cada LDR o un circulo grande
        # si ncir es uno dibuja un circulo grande, en caso de que se entregue cualquier otro valor dibuja un circulo por ldr
        if ncir==1:
            #circulo grande
            r=int(R-R/8)
            pygame.draw.circle(self.surface, (0,255,0), (pos), r, 0)
        else:
            #un circulo en cada ldr
            r=R//7
            l=5
            a=(self.p1[0], self.p1[1])
            b=(self.p2[0], self.p2[1])
            c=(self.p3[0], self.p3[1])
            puntos=(a,b,c)
            pc=orientacion -1
            #p2=puntos[pc]
            p1=puntos[pc-1]
            p3=puntos[pc-2]
            p1p=(p1[0]+1, p1[1])
        
            u=(p3[0]-p1[0], p3[1]-p1[1])
            v=(p1p[0]-p1[0], p1p[1]-p1[1])
            u2=(u[0]*u[0]+u[1]*u[1])**0.5
            v2=(v[0]*v[0]+v[1]*v[1])**0.5
            uv= u[0]*v[0]+u[1]*v[1]
            alpha=math.acos(uv/(u2*v2))
            det=u[0]*v[1]-u[1]*v[0]
            if det<0:
                alpha=alpha
            else:
                alpha=2*math.pi-alpha
                #c1=math.degrees(alpha)
            c=alpha+math.radians(90)
            #print('angulos',c, c1) 
            #print((math.sin(c)))
            #print((math.cos(c)))     
            b1a=pos[0] + int(0.8*l*r*math.cos(c))
            b2a=pos[1] + int(0.8*l*r*math.sin(c))
            b1b=pos[0] - int(l*r*math.cos(c))
            b2b=pos[1] - int(l*r*math.sin(c))
            pygame.draw.circle(self.surface, (255,255,255), (b1a, b2a), 2*r, 0)
            pygame.draw.circle(self.surface, (255,255,255), (b1b, b2b), 2*r, 0)
            
    def dibrotacion(self, pos, R, orientacion, dm1, dm2):
        r=R//7
        l=5
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        #p2=puntos[pc]
        #p1=puntos[pc-1]
        #p3=puntos[pc-2]
        #p1p=(p1[0]+1, p1[1])
        p1p=(pos[0]+1,pos[1])
        p1=(pos[0],pos[1])
        p3=(puntos[pc])
        
        u=(p3[0]-p1[0], p3[1]-p1[1])
        v=(p1p[0]-p1[0], p1p[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha+math.radians(90)
        else:
            alpha=-alpha+math.radians(90)
        #c1=math.degrees(alpha)
        c=alpha+math.radians(90)
        #print('angulos',c, c1) 
        #print((math.sin(c)))
        #print((math.cos(c)))     
        b1a=pos[0] + int(0.8*l*r*math.cos(c))
        b2a=pos[1] + int(0.8*l*r*math.sin(c))
        b1b=pos[0] - int(l*r*math.cos(c))
        b2b=pos[1] - int(l*r*math.sin(c))
        if dm1==1:
            pygame.draw.circle(self.surface, (255,255,255), (b1b, b2b), 3*r, 0) 
        elif dm1==0:
            pygame.draw.circle(self.surface, (255,255,255), (b1a, b2a), 3*r, 0) 
        #pygame.draw.circle(self.surface, (0,255,0), (b1b, b2b), 2*r, 5)
        
    def angcol(self, centro1,centro2):
        p1=centro1
        p2=centro2
        p3=(centro1[0]+1,centro1[1])
        u=(p2[0]-p1[0], p2[1]-p1[1])
        v=(p3[0]-p1[0], p3[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        return alpha
    
    def vectper(self, centro1,centro2,angcol):
        p1=centro1
        p2=centro2
        p3=(p1[0]+1,p1[1])
        p2p=(p2[1]-p1[1])+p1[0],-(p2[0]-p1[0])+p1[1]
        u=(p2p[0]-p1[0], p2p[1]-p1[1])
        v=(p3[0]-p1[0], p3[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        return alpha
    def dibvectper(self, centro1,centro2,angper,angcol,r): 
        p1=centro1
        p2=centro2
        p3=(p1[0]+30,p1[1])
        p2p=(p2[1]-p1[1])+p1[0],-(p2[0]-p1[0])+p1[1]
        p1p=math.cos(angper)*r+p1[0],math.sin(angper)*r+p1[1]
        p1per=math.cos(angcol)*r+p1[0],math.sin(angcol)*r+p1[1]
        u=(p3[0]-p1[0], p3[1]-p1[1])
        v=(p2p[0]-p1[0], p2p[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        pygame.draw.line(self.surface, (255,0,0), (p1),(p1per))
        pygame.draw.line(self.surface, (0,0,255), (p1),(p1p))
        #pygame.draw.line(self.surface, (255,0,255), (p1),(p2))#linea morada que une los centros
        pygame.draw.line(self.surface, (0,255,255), (p1),(p3))#linea celeste que sirve como referencia para el calculo de los angulos
    
    def dirav(self, centro, orientacion, angper, r):
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        p3=(puntos[pc])
        p1=centro
        p2=math.cos(angper)*r+p1[0],math.sin(angper)*r+p1[1]
        u=(p3[0]-p1[0], p3[1]-p1[1])
        v=(p2[0]-p1[0], p2[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        if alpha<=math.radians(90):
            angper=angper
        elif alpha>math.radians(90):
            angper=angper+math.radians(180)  
        return angper
    
    def compapo(self, centro, orientacion, angper, r):#comparacion entre el angulo perpendicular y la orientacion, para obtener el angulo
        a=(self.p1[0], self.p1[1])
        b=(self.p2[0], self.p2[1])
        c=(self.p3[0], self.p3[1])
        puntos=(a,b,c)
        pc=orientacion -1
        p3=(puntos[pc])
        p1=centro
        p2=math.cos(angper)*r+p1[0],math.sin(angper)*r+p1[1]
        u=(p3[0]-p1[0], p3[1]-p1[1])
        v=(p2[0]-p1[0], p2[1]-p1[1])
        u2=(u[0]*u[0]+u[1]*u[1])**0.5
        v2=(v[0]*v[0]+v[1]*v[1])**0.5
        uv= u[0]*v[0]+u[1]*v[1]
        alpha=math.acos(uv/(u2*v2))
        det=u[0]*v[1]-u[1]*v[0]
        if det<0:
            alpha=alpha
        else:
            alpha=2*math.pi-alpha
        return alpha
        
'''
#se silencia esta parte del codigo, la cual se uso para probar el dibujo de las clases
pygame.init()
dimensiones = [700, 500]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('ventana de prueba para los dibujos')
NEGRO= (0,0,0)
#(s*c[0][0]+x,s*c[0][1]+y),(s*c[1][0]+x,s*c[1][1]+y),(s*c[2][0]+x,s*c[2][1]+y) asi se obtiene el dato del optitrack
#p1=(100,50)
#p2=(300,500)
#p3=(400,200)

p=((100,400),(200,150),(300,400))
#p=((100,400),(200,200),(300,400))
p1=p[0]
p2=p[1]
p3=p[2]

#pruebas de los dibujos de las clases
t1=Triangulo(p1, p2, p3, pantalla)
t2=Chevibot(p1, p2, p3, pantalla, 'funcionando',1)
t2.dibujar()
ang= t2.angulos()
ori=t2.orientacion65(ang)
ap=t2.circumcentro()
#b=t2.radio1()
t1.dibujar()
#a=t2.centrotri()
a=(ap[0], ap[1])
b=ap[2]
#t2.dibujarcir1(a,b)
t2.dibujarlrd1(a,b, ori)
t2.dibvect1(a,b, ori)
dat=t2.circumcentro()
t2.dibujarcir(dat)
t2.dibestado(a, int(b/4))

pygame.draw.circle(pantalla, (255,255,255), a, 5, 0)

while True:       
    my_clock = pygame.time.Clock()
    #pantalla.fill(NEGRO) 
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            break
      
    pygame.display.flip()
    my_clock.tick(10) #FPS de la ventana y tambien de la actualizacion de los datos

pygame.quit()
'''