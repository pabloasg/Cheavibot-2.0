#coding: cp1252
import csv
import matplotlib.pyplot as plt
import math
import numpy as np


'''
la estructura del archivo .csv viene del programa SPPesc, y es de la siguiente forma, columna 1: posicion x, columna 2: posicion y, columna 3:velocidad x, columna 4:velocidad y,
columna 5: magnitud velocidad, columna 6:angulo, estas 6 columnas se repiten para cada bot, las filas representan cada paso de la simulacion
'''

paso=1
j=0
with open('movF.csv', newline='') as f: #la lista a es una lista con float que contiene la informacion del archivo csv
    reader = csv.reader(f)
    datos=[]
    for row in reader:
        a=[float(i) for i in row]
        datos.append(a)
    
        nc=6 #numero de columnas que se escriben por bots, corresponde a la cantidad de datos de coordenadas del archivo SPPes
        nbots=int(len(datos[0])/nc)
        x=[]
        y=[]
        vx=[]
        vy=[]
        vd=[]
        ad=[]
        xx=0
        yy=0
        vxx=0
        vyy=0
        for i in range (0, nbots):
            xd=datos[j][nc*i]
            yd=datos[j][nc*i+1]
            vxd=datos[j][nc*i+2]
            vyd=datos[j][nc*i+3]
            v=datos[j][nc*i+4]
            a=math.degrees(datos[j][nc*i+5])
            x.append(xd)
            y.append(yd)
            vx.append(vxd)
            vy.append(vyd)
            vd.append(v)
            ad.append(a)            
            xx=xx+xd
            yy=yy+yd
            vxx=vxx+vxd
            vyy=vyy+vyd
            
        xxc=xx/nbots
        yyc=yy/nbots
        vxc=vxx/nbots
        vyc=vyy/nbots
        
            
        print(x)
        print(y)
        print(vx)
        print(vy)
        print(vd)
        print(ad)
        print('largo de los vectores', len(x), len(y), len(vx), len(vy), len(vd), len(ad))
        print('datos del vector central', xxc, yyc, vxc, vyc)
        
        #graficar vectores de velocidad
        plt.figure()
        pasos=str(paso)
        plt.title('prueba para graficar velocidades'+ ' paso número '+pasos)
        plt.xlabel('posición eje x [cm]')
        plt.ylabel('posición eje y [cm]')
        plt.quiver(x, y, vx, vy)
        plt.quiver(xxc, yyc, vxc, vyc, color=(1.0,0,0))
        #plt.scatter(x,y, s=20.0, c='g')
        plt.scatter(x,y, s=20.0, facecolors='none', edgecolors='g')
        name='Vect paso N'+pasos+'.png'
        plt.savefig(name)
        #plt.show()
        plt.close()
        
        #graficar histograma
        plt.figure()
        plt.hist(ad, edgecolor='black', bins=12, range=(0,360))
        plt.title('prueba para graficar dirección de movimiento (ángulos)'+ ' paso número '+pasos)
        plt.xlabel('ángulo')
        plt.ylabel('cantidad de bots')
        name='Hist paso N'+pasos+'.png'
        plt.savefig(name)
        #plt.show()
        plt.close()
        paso=paso+1
        j=j+1
        #graficar histograma polar
        
        N = 12
        bottom = 0
        # create theta for 24 hours
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        # make the histogram that bined on 24 hour
        radii, tick = np.histogram(ad, bins = 12, range=(0,360))
        
        # width of each bin on the plot
        width = (2*np.pi) / N
        
        # make a polar plot
        plt.figure(figsize = (12, 8))
        ax = plt.subplot(111, polar=True)
        print(theta)
        
        print(radii)
        print(width, math.degrees(width), math.degrees(width)*N)
        bars = ax.bar(theta, radii, width=width, bottom=bottom, align='center', edgecolor='black')
        
        
        # set the lable go clockwise and start from the top
        ax.set_theta_zero_location("E")
        # clockwise
        ax.set_theta_direction(1)
        
        plt.title('prueba para histograma polar'+ ' paso número '+pasos)
        # set the label
        #ticks = ['0', '45', '90', '135', '180', '235', '270', '315']
        #ax.set_xticklabels(ticks)
        name='Hist  polar paso N'+pasos+'.png'
        plt.savefig(name)
        #plt.show()
        plt.close()
        
        #graficar diagrama polar con flechas
        
        N = 12
        bottom = 0
        # create theta for 24 hours
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        # make the histogram that bined on 24 hour
        radii, tick = np.histogram(ad, bins = 12, range=(0,360))
        
        # width of each bin on the plot
        width = (2*np.pi) / N
        
        # make a polar plot
        plt.figure(figsize = (12, 8))
        ax = plt.subplot(111, polar=True)
        print(theta)
        print(radii)
        #radii=radii+1
        print(radii)
        print(width, math.degrees(width), math.degrees(width)*N)
        #bars = ax.bar(theta, radii, width=width, bottom=bottom, align='edge', edgecolor='black')
        rmin=np.zeros(len(theta))
        #ax.plot(theta, radii, 'r*')
        rh=max(radii)/10
        radii=radii+rh
        ax.vlines(theta, rmin, radii)
        for i in range (0, len(theta)):
            if radii[i]>rh:
                if radii[i] < max(radii)/3:
                    plt.arrow(theta[i], 0, 0, radii[i], alpha = 1, width = 0.025, edgecolor = 'black', facecolor = 'black', lw = 1, length_includes_head=True, head_length=rh/2, head_width=0.025*5)
                else:
                    plt.arrow(theta[i], 0, 0, radii[i], alpha = 1, width = 0.025, edgecolor = 'black', facecolor = 'black', lw = 1, length_includes_head=True, head_length=rh)
            else:
                plt.plot(theta[i], radii[i], 'ko')

        ax.grid(False)
        ax.set_yticklabels([])
        
        # set the lable go clockwise and start from the top
        ax.set_theta_zero_location("E")
        # clockwise
        ax.set_theta_direction(1)
        
        plt.title('prueba para shift (diagrama con flechas)'+ ' paso número '+pasos)
        # set the label
        #ticks = ['0', '45', '90', '135', '180', '235', '270', '315']
        #ax.set_xticklabels(ticks)
        name='flechas paso N'+pasos+'.png'
        plt.savefig(name)
        #plt.show()
        plt.close()
    
    
            
        
        print(datos)
        print(len(datos),'largo de datos', len(datos[0]), 'elementos en fila')
        
print('done, ya termino de guardar los graficos')
    
'''
nbots=int(len(datos[0])/4)

for j in range(0, len(datos)):
    x=[]
    y=[]
    vx=[]
    vy=[]
    for i in range (0, nbots):
        xd=datos[j][4*i]
        yd=datos[j][4*i+1]
        vxd=datos[j][4*i+2]
        vyd=datos[j][4*i+3]
        x.append(xd)
        y.append(yd)
        vx.append(vxd)
        vy.append(vyd)
        
    print(x)
    print(y)
    print(vx)
    print(vy)
    print('largo de los vectores', len(x), len(y), len(vx), len(vy))
    
    plt.figure()
    paso=str(j)
    plt.title('prueba para graficar velocidades'+ ' paso numero '+paso)
    plt.xlabel('posicion eje x [cm]')
    plt.ylabel('posicion eje y [cm]')
    plt.quiver(x, y, vx, vy)
    plt.quiver(500, 500, 100, 100, color='r')
    plt.show()
    '''