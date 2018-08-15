import numpy as np
import csv
import matplotlib.pyplot as plt


'''
graficos para encontrar la correlacion entre pixeles proyectados y mm medidos
'''

#lee y guarda los datos de las mediciones
with open('pixel a mm.csv', newline='') as f: #la lista a es una lista con float que contiene la informacion del archivo csv
    reader = csv.reader(f)
    datosr=[]
    for row in reader:
        a=[float(i) for i in row]
        datosr.append(a)
        #print(a)
        #print(datosr)
        #print('espacio')
        
xcor=np.array([])
ycor=np.array([])
        
for i in range(0, int(len(datosr)/6)):
    xp=np.array([])
    yp=np.array([])
    xm=np.array([])
    ym=np.array([])
    for j in range (0, 6):
        a=i*6+j
        #print(a, j)
        #print(datosr[a])
        xp=np.append(xp, datosr[a][2])
        yp=np.append(yp, datosr[a][3])
        xm=np.append(xm, datosr[a][4])
        ym=np.append(ym, datosr[a][5])
    
    #codigo para comprobar los valores de los vectores
    print(xp)
    print(yp)
    print(xm)
    print(ym)
    pp=np.array([20,50,70,100,150,300])
    y=(pp*2+1)
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    plt.title('distancias en el eje x medicion '+str(i))
    plt.xlabel('distancia proyectada [pixeles]')
    plt.ylabel('distancia medida [mm]')
    zx=np.polyfit(xp, xm,1)
    #print(z[0], 'espacio', z[1])
    plt.plot(xp, xm, 'bo', xp, xm, 'k')
    plt.plot(pp,(pp*zx[0]+zx[1]), 'g--')
    ax.text(50, 200, 'xm = {:.3}xp+{:.3}'.format(zx[0], zx[1]), fontsize=15)
    #print(zx)
    xcor=np.append(xcor, zx)
    #plt.show()
    
    fig=plt.figure()
    ay=fig.add_subplot(111)
    plt.title('distancias en el eje y medicion '+str(i))
    plt.xlabel('distancia proyectada [pixeles]')
    plt.ylabel('distancia medida [mm]')
    zy=np.polyfit(yp, ym,1)
    plt.plot(yp, ym, 'ro', yp, ym, 'k')
    plt.plot(pp,(pp*zy[0]+zy[1]), 'g--')
    ay.text(50, 200, 'ym = {:.3}yp+{:.3}'.format(zy[0], zy[1]), fontsize=15)
    #print(zy)
    ycor=np.append(ycor, zy)
    #plt.show()

print(xcor, 'correlacion en x')
print(ycor, 'correlacion en y')

xcorm=np.array([])
xcorb=np.array([])
ycorm=np.array([])
ycorb=np.array([])
for i in range (0, len(xcor)):
    if i%2==0:
        xcorm=np.append(xcorm, xcor[i])
        ycorm=np.append(ycorm, ycor[i])
    else:
        xcorb=np.append(xcorb, xcor[i])
        ycorb=np.append(ycorb, ycor[i])
        
        
print(xcorm)
print(ycorm)    
        
xm=np.mean(xcorm)
ym=np.mean(ycorm)
xb=np.mean(xcorb)
yb=np.mean(ycorb)
xms=np.std(xcorm)
yms=np.std(ycorm)
xbs=np.std(xcorb)
ybs=np.std(ycorb)
print(xm, xb)
print(ym, yb)
print('desviaciones estandar')
print(xms, xbs)
print(yms, ybs)

    
    
        
        