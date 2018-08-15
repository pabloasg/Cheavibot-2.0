import pygame
import os
import imagenes
#import math


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

x,y=(800,500)
cir=imagenes.circulo(pantalla, 3, 500, (x,y))
cir.ajustar()
board=imagenes.checkboard(pantalla, 8, 800, (800,500))
board.ajustar()

print(board.getdat())

while True:       
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO) 
    
    my_clock = pygame.time.Clock()
    pantalla.fill(NEGRO)
    
    ev = pygame.event.poll() # Look for any event
    if ev.type == pygame.QUIT: # Window close button clicked?
        pygame.quit()
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            pygame.quit()
        if ev.key == pygame.K_UP:
            y=y-10
        if ev.key == pygame.K_DOWN:
            y=y+10
        if ev.key == pygame.K_RIGHT:
            x=x+10
        if ev.key == pygame.K_LEFT:
            x=x-10
            
    cir.dibujar()       
    cir.mover(x,y)
    
    #board.dibujar()
    #board.mover(x,y)
    
    
    
    
            
    pygame.display.flip()
    my_clock.tick(60) #FPS de la ventana y tambien de la actualizacion de los datos

pygame.quit()