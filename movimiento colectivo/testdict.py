


class prueba():
    def __init__(self, datos, posicion, velocidad):
        self.datos=datos
        self.posicion=posicion
        self.velocidad=velocidad
        
    def getdat(self):
        return(self.datos)
    
    def getvel(self):
        return self.velocidad
    
    def velmedia(self, vseq):
        v=0
        v1=self.velocidad
        if len(vseq)==0:
            v=v1
        else:
            for i in range(0, len(vseq)):
                v=v+vseq[i]
            v=v+v1
            v=v/(len(vseq)+1)
        return v
    
    def modvel(self, vel):
        self.velocidad=vel
            
        
    
a1=prueba('algo', (100, 100), 50)
a2=prueba('segundo obj', (100,50), 70)
a3=prueba('tercer obj', (50,50), 100)

v=a2.getvel(), a3.getvel()
vm=a1.velmedia(v)
print(v,'valores de velocidad', vm, 'vel media')

print(a1.getdat())
print(type(a1))

dic={}
dic[1]='valor 1'
dic[2]='valor 2'
dic[3]=a1
dic[4]=a2
dic[5]=a3
print(dic)
for i in range(1,4):
    print(dic[i], 'este es el valor ', i, ' del diccionario')
    
b=dic[3].getdat()
print(b)
dic[2]='nuevo valor 2'
dic[1]='valor 1 modificado'
print(dic)
for i in range(1,4):
    print(type(dic[i]), 'tipo valor ', i, ' del diccionario')

del dic[1]
print(dic)
dic[1]=1
dic[1]+=10
print(dic)
print(len(dic), 'elementos del diccionario')
print(dic.keys())
print(dic.values())
print(dic.items())
print('prueba' not in dic)
print(1 in dic)
dic['cat']='hay un gato en el diccionario'
b='cat' in dic
if b==True:
    print(dic['cat'])
elif b==False:
    print('no existe esa clave en el diccionario')
    
vp=dic[4].getvel(), dic[5].getvel()
vpm=dic[3].velmedia(vp)
print(vp,'valores de velocidad', vpm, 'vel media')

dic2={0:'val0', 1:'val1',2:'val2', 3:'val3',4:'val4',5:'val5'}
print(len(dic2))

for i in range(0, len(dic2)):
    print(dic2[i])
    
