import math
import pygame

'''
este archivo se crea para realizar las pruebas con bots mas sencillos que los tipo chevibots, de esta forma se puede visualizar mejor los resultados
'''
BLANCO=(255,255,255)#(0,0,0)#
#font = pygame.font.SysFont("arial", 20)


class coin():
    def __init__(self, surface, centro, radio, velocidad, angulo, seed, gradiente, estado, contador):
        self.surface=surface
        self.centro=centro
        self.radio=radio
        self.velocidad=velocidad
        self.angulo=angulo
        self.seed=seed
        self.gradiente=gradiente
        self.estado=estado
        self.contador=contador
    '''
    sobre las variables:
    seed indica si el bot es seed o no, tiene valor verdadero o falso
    estado tiene valores:
        fijo: indica que el bot no se movera mas, puede ser porque empezo como seed o porque el bot llego a un lugar de la figura donde ya no tiene que moverse mas
        detenido: indica que el bot esta quieto, es como un estado de pausa, donde el bot espera la instruccion para moverse
        funcionando: una vez se le da la orden de moverse al bot, este se aleja del pack de los bots
        moviendose: una vez el bot se ha alejado del pack, se mueve por el borde, hasta entrar en la figura
        figura:indica que el bot entro a la figura y debe activar el algoritmo para detener el bot
    contador: cuenta cuantas veces el bot ha entrado en la figura    
    '''
    
    
    #codigo para comprobar estados e inicializar los estados
    def compseed(self): #funcion que da a todos los estados seed un valor booleano (V o F), lo cual es un valor valido para trabajar mas adelante
        b=self.seed
        if b==True:
            pass
        elif b==False:
            pass
        else:
            self.seed=False
            
    def compgrad(self, largo): #funcion que da a todos los estados grad un valor int, lo cual es un valor valido para trabajar mas adelante, len se refiere al numero de elementos
        a=self.gradiente
        if type(a)==int:
            pass
        else:
            self.gradiente=largo+10
            
    def compestado(self):
        a=self.estado
        b=self.seed
        if b==True:
            self.estado='fijo'
        elif b==False:
            if a=='detenido' or a=='funcionando' or a=='moviendose':
                pass
            else:
                self.estado='detenido'
            
    def compcontador(self):#función que inicializa el contador en cero, en caso de ser cero, queda tal cual
        a=self.contador
        if a==0:
            pass
        else:
            self.contador=0
    
    #codigo para dibujar
    def dibujar(self):
        pos=int(self.centro[0]), int(self.centro[1])
        r=int(self.radio)
        pygame.draw.circle(self.surface, BLANCO, pos , r, 1)
        
    def dibvel(self, s):
        c=self.centro
        x=s*self.velocidad*math.cos(self.angulo)+c[0]
        y=s*self.velocidad*math.sin(self.angulo)+c[1]
        pygame.draw.line(self.surface, (255,0,0), self.centro, (x,y), 1)
        
    def dibseed(self):
        a=self.seed
        b=int(self.radio/5)
        if b<1:
            b=5
        if a==True:
            pygame.draw.circle(self.surface, (0,255,0), (int(self.centro[0]), int(self.centro[1])), b , 0)
        elif a==False:
            pygame.draw.circle(self.surface, (255,0,0), (int(self.centro[0]), int(self.centro[1])), b , 0)
        else:
            pygame.draw.circle(self.surface, (0,0,255), (int(self.centro[0]), int(self.centro[1])), b , 0)
            
    def dibgrad(self):
        font = pygame.font.SysFont("arial", 20)
        escribir=str(self.gradiente)
        grad=font.render(escribir, True, (255,0,255))
        a=coin.getdatpos(self)
        self.surface.blit(grad, (a[0][0]+10, a[0][1]+5))
    
    def dibestado(self):
        a=self.estado
        b=int(self.radio-self.radio/7)
        c=2
        if b<1:
            b=5
        if a=='fijo':
            pygame.draw.circle(self.surface, (0,255,0), (int(self.centro[0]), int(self.centro[1])), b , c)
        elif a=='detenido':
            pygame.draw.circle(self.surface, (255,0,0), (int(self.centro[0]), int(self.centro[1])), b , c)
        elif a=='funcionando':
            pygame.draw.circle(self.surface, (255,255,0), (int(self.centro[0]), int(self.centro[1])), b , c)
        elif a=='moviendose':
            pygame.draw.circle(self.surface, (0,255,255), (int(self.centro[0]), int(self.centro[1])), b , c)
        elif a=='figura':
            pygame.draw.circle(self.surface, (0,0,255), (int(self.centro[0]), int(self.centro[1])), b , c)
        else:
            pygame.draw.circle(self.surface, (255,255,255), (int(self.centro[0]), int(self.centro[1])), b , c)
            
    def dibcontador(self):
        font = pygame.font.SysFont("arial", 20)
        escribir=str(self.contador)
        grad=font.render(escribir, True, (255,0,255))
        a=coin.getdatpos(self)
        self.surface.blit(grad, (a[0][0]+10, a[0][1]-25))
    #funciones para recuperar variables de coin
    def getdatpos(self):
        return self.centro, self.radio
    
    def getvel(self):
        return self.velocidad

    def getang(self):
        return self.angulo
    
    def getseed(self):
        return self.seed
    
    def printseed(self):
        sd=self.seed
        if sd==True:
            print('si es seed')
        elif sd==False:
            print('no es seed')
        else:
            print('valor incorrecto de seed')
            
    def getgrad(self):
        return self.gradiente
    
    def getestado(self):
        return self.estado
    
    def getcontador(self):
        return self.contador
    
    #funciones para sobreescibir variables de estado de la clase coin
    def modcentro(self, x, y):
        centro=self.centro
        xc=centro[0]+x
        yc=centro[1]+y
        ncentro=xc, yc
        return ncentro
    
    def modvel(self, vel):
        v=self.velocidad+vel
        return v
    
    def modang(self, ang):
        alpha=self.angulo+ang
        return alpha
    
    def modseed(self, seed):
        s=self.seed
        if seed==True or False:
            self.seed= seed
        else:
            self.seed=s
            
    def modgrad(self, grad):
        if type(grad)==int:
            self.gradiente=grad
        else:
            print('el tipo de entrada no es valido para gradiente')
            
    def modestado(self, nestado):
        self.estado=nestado
        
    def modcontador(self, ncontador):
        self.contador=ncontador
            
    def mover(self):
        alpha=self.angulo
        v=self.velocidad
        vx=v*math.cos(alpha)
        vy=v*math.sin(alpha)
        pos=self.centro
        x=pos[0]+vx
        y=pos[1]+vy
        ncentro=x,y
        self.centro=ncentro
        
    def rotar(self, dirmov):#0 es direccion anti horaria, 1 es direccion horaria
        paso=math.radians(5)#angulo a mover en grados
        if dirmov==0:
            self.angulo=self.angulo-paso
        elif dirmov==1:
            self.angulo=self.angulo+paso
        else:
            self.angulo=self.angulo+paso
            print('se entrego un valor no valido y por defecto se cambio a 1')
        
    