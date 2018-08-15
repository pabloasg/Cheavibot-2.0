import pygame
import os
import objetos

'''
crea figuras de un determinado numero de pixeles, la posicion indicada corresponde a la esquina superior derecha
el objetivo es medir las figuras proyectadas (rectangulos) para determinar cuantos mm miden
y luego ver la relacion entre pixel y mm segun las coordenadas x e y 
'''

#ajusta la aparicion de la ventana en las coordenadas x,y
x = 100
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


pygame.init()
dimensiones = [1600, 1000]
pantalla =pygame.display.set_mode(dimensiones)
pygame.display.set_caption('ventana de prueba para los dibujos')
NEGRO= (0,0,0)
BLANCO=(255,255,255)
font = pygame.font.SysFont("arial", 25)

rect1=objetos.rectangulo(pantalla, 500,500,100,300)

while True:       
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    ev = pygame.event.poll() # Look for any event
    
    if ev.type == pygame.QUIT: # Window close button clicked?
        break
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            break
        if ev.key == pygame.K_RIGHT:
            xmod=10
            rect1.modificarx(xmod)
        if ev.key == pygame.K_LEFT:
            xmod=-10
            rect1.modificarx(xmod)
        if ev.key == pygame.K_UP:
            ymod=-10
            rect1.modificary(ymod)
        if ev.key == pygame.K_DOWN:
            ymod=10
            rect1.modificary(ymod)
    
    
        if ev.key == pygame.K_w:
            wmod=10
            rect1.modificarw(wmod)
        if ev.key == pygame.K_s:
            wmod=-10
            rect1.modificarw(wmod)
        if ev.key == pygame.K_e:
            hmod=10
            rect1.modificarh(hmod)
        if ev.key == pygame.K_d:
            hmod=-10
            rect1.modificarh(hmod)
            
            
    rect1.dibujar()
    datos=rect1.getdat()
    print(datos)
    
    datx='posicion de x=  '+str(datos[0])+ ' [pixeles]'
    datxf=font.render(datx, True, (255,255,255))
    pantalla.blit(datxf, (1300,50))

    daty='posicion de y=  '+str(datos[1])+ ' [pixeles]'
    datyf=font.render(daty, True, (255,255,255))
    pantalla.blit(datyf, (1300,80))
    
    datw='ancho w=  '+str(datos[2])+ ' [pixeles]'
    datwf=font.render(datw, True, (255,255,255))
    pantalla.blit(datwf, (1300,110))
    
    dath='alto h=  '+str(datos[3])+ ' [pixeles]'
    dathf=font.render(dath, True, (255,255,255))
    pantalla.blit(dathf, (1300,140))
    
    
    
    
    
    
    pygame.display.flip()
    my_clock.tick(24) #FPS de la ventana y tambien de la actualizacion de los datos

pygame.quit()