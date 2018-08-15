import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#import math
import csv

x=np.arange(-210,270,60)
y=np.arange(-210,210,60)

print('datos de la grilla')
print(x, '\n', y)
X=np.zeros(len(x)*len(y))
Y=np.zeros(len(x)*len(y))
contador=0
for i in range(0, len(x)):
    for j in range(0, len(y)):
        Y[contador]=y[j]
        X[contador]=x[i]
        #print(i,j, contador, X[contador], Y[contador])
        contador+=1
for i in range(0, len(x)):
    X=np.append(X, x[i])
    Y=np.append(Y, 0)
for i in range(0, len(y)):
    X=np.append(X, 0)
    Y=np.append(Y, y[i])
#print(X, Y,len(x), len(y), len(X))
X=np.append(X, 0)
Y=np.append(Y, 0)
#print(len(X), len(Y))
print('puntos de la grilla')
print(X,Y)
'''
plt.figure()
plt.title('puntos de medicion')
plt.xlabel('distancia eje x [mm]')
plt.ylabel('distancia eje y [mm]')
plt.plot(X,Y, '.')
plt.show()
'''

with open('daterr.csv', newline='') as f: #la lista a es una lista con float que contiene la informacion del archivo csv
    reader = csv.reader(f)
    datosr=[]
    for row in reader:
        a=[float(i) for i in row]
        datosr.append(a)
print('datos de los errores')
print(datosr, type(datosr), len(datosr))
xerr=np.array([])
yerr=np.array([])
for i in range(0, len(datosr)):
    xerr=np.append(xerr, datosr[i][0])
    yerr=np.append(yerr, datosr[i][1])
print('vectores con errores x e y')
print(xerr)
print(yerr)

plt.figure()
plt.title('desplazamiento del centro entre la imagen proyectada y la posicion real')
plt.xlabel('distancia eje x [mm]')
plt.ylabel('distancia eje y [mm]')
plt.quiver(X,Y,xerr, yerr, width=0.003, scale=100)
#plt.show()


#correccion del desplazamiento
xperr=np.zeros(len(X))
yperr=np.zeros(len(Y))

#limites de los cuadrados
a=-210
b=-30
c=30
d=210
e=150

for i in range(0, len(X)):
    ax=X[i]
    ay=Y[i]
    x=xerr[i]
    y=yerr[i]
    if a<=ax<b and a<=ay<b:
        xperr[i]=x-(1)
        yperr[i]=y-(-3)
    elif b<=ax<=c and a<=ay<b:
        xperr[i]=x-(6)
        yperr[i]=y-(0)
    elif c<ax<=d and a<=ay<b:
        xperr[i]=x-(8)
        yperr[i]=y-(1)
    
    elif a<=ax<b and b<=ay<=c:
        xperr[i]=x-(x*0.5)
        yperr[i]=y-(y*0.5)
    elif b<=ax<=c and b<=ay<=c:
        xperr[i]=x-(5)
        yperr[i]=y-(y*0.5)
    elif c<ax<=d and b<=ay<=c:
        xperr[i]=x-(11.5)
        yperr[i]=y-(3)
    
    elif a<=ax<b and c<ay<=e:
        xperr[i]=x-(x*0.5)
        yperr[i]=y-(4.5)
    elif b<=ax<=c and c<ay<=e:
        xperr[i]=x-(6)
        yperr[i]=y-(5)
    elif c<ax<=d and c<ay<=e:
        xperr[i]=x-(11)
        yperr[i]=y-(7)
print('errores corregidos')        
print(xperr)
print(yperr)
        
plt.figure()
plt.title('correccion del desplazamiento del centro')
plt.xlabel('distancia eje x [mm]')
plt.ylabel('distancia eje y [mm]')
plt.quiver(X,Y,xperr, yperr, width=0.003, scale=100)
plt.show()
    
    
