'''
Created on 26/10/2014

@author: K
'''
from random import randint
from math import sqrt
from test.sortperf import randfloats
import random
import sys
'''
import csv
'''
    
if __name__ == '__main__':
    strax = sys.argv[1]
    stray = sys.argv[2]
    architeraciones = open('iteraciones.csv','w')
    #archivoX = open('C:\\Users\\K\\Desktop\\ejemplo\\xs.csv','r')
    #archivoY = open('C:\\Users\\K\\Desktop\\ejemplo\\ys.csv','r')
    archivoX = open(strax)
    archivoY = open(stray)
    i = 0
    j = 0
    k = 0
    l = 0
    alpha = float(sys.argv[3])
    iteraciones = int(sys.argv[4])
    error = float(sys.argv[5])
    ly = []
    lx = []
    lxx = []
    for lineY in archivoY:
        lineY = lineY.replace("\n", "")
        ly.append(lineY)
        #print(ly[k])
        k = k+1
        
    for lineX in archivoX:
        lineX = lineX.replace("\n", "")
        lineaX = lineX.split(',')
        lx.append(lineaX)
        l = len(lineaX)
        #print(lx[i])
        i = i + 1
    # l = cantidad n de variables , k = cantidad m de muestras
    archivoX.close()
    archivoY.close()
    # Theta alzar
    lt = []
    while(j<l):
        lt.append(random.randint(-3,3))
        #print(lt[j])
        j = j +1
    q=0
    le = []
    #lt[0] = 0.00 # valores prueba ejemplo
    #lt[1] = 1.00 # valores prueba ejemplo
    #lt[2] = 2.00 # valores prueba ejemplo
    w=False
    while(q<iteraciones and w==False):
        # Calculo Thetas
        # While para todas las funciones
        # Contador para calcular funcion por cada theta
        contadorThetas = 0
        # Calculo funcion h0o(xo..) - y
        calcfunh = 0
        gh = [] # Esta mierda contiene todas las h(X0,X1, ... , Xn)- y de todas las muestras
        # While para calcular cada h(X0,X1 ... , Xn) - Y una por cada muestra
        while(calcfunh<k):
            funh = 0.00
            contfh = 0
            # While sumatoria de theta i + xi
            while(contfh<l):
                #lt = arreglo de thetas y lx arreglo de x [ variar en m ] [ variar en n]
                funh = funh + ((float(lt[contfh])*float(lx[calcfunh][contfh])))
                str = lt[contfh].__str__() + ' * ' + lx[calcfunh][contfh]
                print(str)
                contfh = contfh + 1
            str = funh.__str__() + ' - ' + ly[calcfunh]
            funh = funh-float(ly[calcfunh])
            str = str + ' = ' + funh.__str__()
            print(str)
            gh.append(funh)
            calcfunh = calcfunh + 1
        print(gh)
        gh1 = [] # va a guardar gh solo que esta servira para el calculo de thetas por lo cual se le va a multiplicar su xn
        contadorgh1 = 0
        # Calculo sumatoria con thetas multiplicado por 1/m
        while (contadorgh1<l):
            total = 0.00
            tempc1 = 0
            m = k
            while (tempc1 < m):
                strk = '= ' + lx[tempc1][contadorgh1] +' X' + tempc1.__str__() + ',' + contadorgh1.__str__() + ' * ' + gh[tempc1].__str__()
                print(strk)
                total = total + (gh[tempc1] * float(lx[tempc1][contadorgh1]))
                tempc1 = tempc1 + 1
            print(total)
            total = total / m
            print(total)
            gh1.append(total)
            contadorgh1 = contadorgh1 + 1
        print('GH1=')
        print(gh1)
        contadorgh1 = 0
        # Calculo sumatoria con thetas multiplicado por 1/m
        while (contadorgh1<l):
            total = 0.00
            tempc1 = 0.00
            total = gh1[contadorgh1] * alpha
            print('Por Alpha:')
            print(total)
            tempc1 = lt[contadorgh1] - total
            print('Theta:')
            print(tempc1)
            lt[contadorgh1] = tempc1
            contadorgh1 = contadorgh1 + 1
        print(lt)
        # Funcion de Costos
        gh2 = []
        total2 = 0.00
        tempc2 = 0
        m = k
        while(tempc2<m):
            tempt = 0.00
            tempt = (gh[tempc2]**2)
            total2 = total2 + tempt
            tempc2 = tempc2 + 1
        total2 = total2 / (2*m)
        #print(total2)
        le.append(total2)
        err = 0.0
        #if (q>=1):
        #    err = float(le[q-1]-le[q])
        #else:
        #    err = total2
        err = total2
        str2 = 'Iteracion: ' + q.__str__()
        strE = err.__str__() + '\n'
        print(str2)
        print(err)
        architeraciones.write(strE)
        if (err>error):
            w = False
        else:
            w = True
        q = q + 1
    pass