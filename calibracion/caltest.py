import pygame
import os

#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


pygame.init()
dimensiones = [1800, 1000]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('test calibracion')
NEGRO= (0,0,0)

#inicializar teclas de calibracion (boolean) y valores de inicio
xt=False
yt=False
st=False
x=800
y=500
X=x
Y=y
s=1
r=10

a=x
b=y
c=s
d=r

while True:       
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    mensaje0='los parametros iniciales son: x = {}, y = {} y s = {}'.format(str(a), str(b), str(c))
    mensaje1='los parametros despues de la calibarcion son: xc = {}, pc = {} y sc = {}'.format(str(x), str(y), str(s))
    
    
    
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
        if ev.key == pygame.K_x:
            xt=True
            yt=False
            st=False
        if ev.key == pygame.K_y:
            xt=False
            yt=True
            st=False
        if ev.key == pygame.K_s:
            xt=False
            yt=False
            st=True
        if st==False and xt==False and yt==False:
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
                s=s+10
            if ev.key == pygame.K_KP_MINUS:
                s=s-10
            if ev.key == pygame.K_UP:
                s=s+1
            if ev.key == pygame.K_DOWN:
                s=s-1
            if ev.key == pygame.K_RIGHT:
                s=s+0.05
            if ev.key == pygame.K_LEFT:
                s=s-0.05
                
        
        
    pygame.draw.circle(pantalla, (255,255,255), (int(x),int(y)), (int(r*s)), 0)
    pygame.draw.line(pantalla, (255,0,0), (int(X),int(Y)), (int(X)+200,int(Y)), 1)
    pygame.draw.line(pantalla, (0,255,0), (int(X),int(Y)), (int(X),int(Y)-200), 1)
        
        
        
    pygame.display.flip()
    my_clock.tick(24) #FPS de la ventana y tambien de la actualizacion de los datos

pygame.quit()