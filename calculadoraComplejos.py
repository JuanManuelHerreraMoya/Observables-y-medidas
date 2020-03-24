<<<<<<< HEAD
import math 
##import wolframalpha

num1 = [3,2]

num2 = [-1,2]


vector1 =[[2,1], [1,-3]]
vector2 =[[5,0],[2,0]]
vectorFinal = []
vectorMultiComplejoVector = []
vectorFinalTensor = []


ident = [[[1, 0],[0,0]] , [[0,0],[0,0]]]
##matriz1 = [[[0, 0],[1,0]] , [[1,0],[0,0]]]
##matriz2 = [[[(1/(2**0.5)),0],[(1/(2**0.5)),0]] , [[(-1/(2**0.5)),0],[(1/(2**0.5)),0]]]
matrizTensorFinal = []
matrizFinal = []

c = [0,0]
def sumar(num1,num2):
    aux = []
    resuE = (num1[0])+(num2[0])
    resuI = (num1[1])+(num2[1])
    c[0],c[1] = resuE,resuI
    aux.append(resuE)
    aux.append(resuI)
    return (aux)

def restar(num1,num2):
    aux=[]
    resuE = (num1[0])-(num2[0])
    resuI = (num1[1])-(num2[1])
    
    c[0],c[1] = resuE,resuI
    aux.append(resuE)
    aux.append(resuI)
    return (aux)

def multiplicar(num1,num2):
    aux = []
    res1 = num1[0]*num2[0] 
    res2 = num1[0]*num2[1]
    res3 = num1[1]*num2[0]
    res4 = (num1[1]*num2[1])*-1
    res1 = res1+res4
    res2 = res2+res3
    aux.append(res1)
    aux.append(res2)
    c[0],c[1] = res1,res2
    return (aux)

def divicion(num1,num2):
    aux = num2[:]
    aux[-1]=aux[-1]*-1
    conjugado1=multiplicar(num1,aux)
    conjugado2=multiplicar(num2,aux)
    res1 = conjugado1[0]/conjugado2[0]
    res2 = conjugado1[1]/conjugado2[0]
    c[0],c[1]=res1,res2
    print(c)
    return (res1,res2)


def modulo(num1):
    resu = ((num1[0]**2)+(num1[1]**2))**0.5
    c[0],c[1]=resu,"null"
    print(c)
    return resu
def inversa(num1):
    c[0],c[1]= num1[0]*-1,num1[1]*-1
    return  c[0],c[1]
def conjugado(num1):
    c[0],c[1]=num1[0],(num1[1]*-1)
    print(c)
    return (c[0],c[1])

def cartesianasPolares(num1):
    hipo = ((num1[0]**2)+num1[1]**2)**(0.5)
    angulo = math.degrees(math.atan(num1[1]/num1[0]))

    if num1[0]<0 and num1[1]<0:
        angulo = angulo + 180
    elif 0>num1[1]:
        angulo = 360 -angulo
    elif 0>num1[0]:
        angulo = 180- angulo
    c[0],c[1]= hipo ,angulo
    print(c)
    return (hipo,angulo)


def sumaVectores(vec1,vec2):
    resu = []
    sumar = [0,0]
    if len(vec1)== len(vec2):
        for i in range(len(vec1)):
            print(sumar(vec1[i],vec2[i]))
            resu.append(sumar(vec1[i],vec2[i]))
            print(aux)
        for j in range(len(aux)):
            suma = sumar(suma,aux[j])
    return vectorFinal



def inversaVectores(vec1):
    for i in range(len(vec1)):
        vectorFinal.append(inversa(vec1[i]))
    print(vectorFinal)
    return vectorFinal

matriz1 = [[[1,-1],[2,7]] , [[4,0],[5,1]]]
matriz2 = [[[2, 0],[5,0]] , [[3,0],[7,0]]]

def adicionMat(mat1,mat2):
    for i in range(len(mat1)):
        aux = []
        for j in range(len(mat1[0])):
            aux.append(sumar(mat1[i][j],mat2[i][j]))
    print(aux)
    return(aux)

def matrizTranspuesta(mat1):
    for i in range(len(mat1[0])):
        temporal = []
        for j in range(len(mat1)):
            temporal.append(mat1[j][i])
        matrizFinal.append(temporal)
    return matrizFinal

def productoInternoVectores(vec1,vec2):
    aux = []
    resu = [0,0]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
           aux.append(multiplicar(vec1[i],vec2[i]))
           resu = sumar(resu,aux[i])
    return(resu)
    
def matrizConjugada(vec1):
    resu = ""
    for i in range(len(vec1)):
        temporal = []

        for j in range(len(vec1[0])):
            temporalNumeros = []
            resu= (conjugado(vec1[i][j]))
            temporalNumeros.append(resu[0])
            temporalNumeros.append(resu[1])
            temporal.append(temporalNumeros)
        matrizFinal.append(temporal)
    return (matrizFinal)

def escalarPorVector(a,vec1):
    for i in range(len(vec1)):
        nuevaMatriz = []
        nuevaMatriz.append(vec1[i][0]*a)
        nuevaMatriz.append(vec1[i][1]*a)
        vectorMultiComplejoVector.append(nuevaMatriz)

    return (vectorMultiComplejoVector)


def escalarPorMatriz(a,mat1):
    for i in range(len(mat1)):
        aux = []
        aux.append(escalarPorVector(a,mat1[i]))
    return (aux)


def productoTensorVectores(vec1,vec2):
    vectorAux=[]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            vectorAux.append(multiplicar(vec1[i],vec2[j]))
    vectorFinal=vectorAux

    return vectorAux



def productoTensorMatriz(mat1,mat2):
    aux = []
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            aux.append(productoTensorVectores(mat1[i],mat2[j]))
    matrizTensorFinal = aux
    return aux    

def potenciaCuadrada (num):
    return (multiplicar(num,num))

def productoInternoVectores(vec1,vec2):
    resu = []
    if len(vec1)==len(vec2):
        cont = 0
        for i in range(len(vec1)):
            resu = multiplicar(vec1[i],vec2[i])
    return (resu)

def distanciaVectores(vec1,vec2):
    resu = []
    solucion = [0,0]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
            resu.append(restar(vec1[i],vec2[i]))
        for j in range(len(resu)):
            solucion = sumar(solucion,potenciaCuadrada(resu[j]))
    solucion[0]=solucion[0]**0.5
    vectorFinal = solucion
    return (solucion)

def normaDeVector(vec1):
    solucion = [0,0]
    for i in range(len(vec1)):
        solucion = sumar(solucion,potenciaCuadrada(vec1[i]))
    solucion[0]=solucion[0]**0.5
    return(solucion)


def multiMatriz(mat1,mat2):
    finMat = []
    for i in range(len(mat1)):
        aux = []
        for j in range(len(mat2[0])):
            cont = (0,0)
            for k in range(len(mat2)):
                sumas = multiplicar(mat1[i][k],mat2[k][j])
                cont = sumar(sumas,cont) 
            aux.append(cont)
        finMat.append(aux)
    return (finMat)
    

def prettyPrinting(c):
    if c[1]!="null":
        if c[1]>=0:
            print (str(c[0])+"+"+str(c[1])+"i")
        else:
            print (str(c[0])+""+str(c[1])+"i")
    else:
        print(str(c[0]))



def prettyprintingVectores(vf):
    vectorPintar = []
    if vectorFinal == [""]:
        print("No se pudo Sumar vector , Longitudes diferentes")
    else:
        for i in vf:
            if (i[1]>0):
                print(str(i[0])+"+"+str(i[1])+"i")
            else:
                print(str(i[0])+str(i[1])+"i")

                
    
def prettyprintingMatriz(matrizFinal):
    for i in matrizFinal:
        print(*i)


        

##def main():
##    productoInternoVectores(vector1,vector2)
##    normaDeVector(vector1)
##    distanciaVectores(vector1,vector2)
##     print(escalarPorMatriz(2,[[[1,0],[2,0]] , [[4,0],[5,0]]]))
##    adicionMat(matriz1,matriz2)
##    m1 = productoTensorMatriz(matriz1,matriz1)
##    m2 = productoTensorMatriz(matriz1,matriz2)
##    multiplicacionMatriz1 = multiMatriz(m2,m1)
##    multiplicacionMatriz2 = multiMatriz(multiplicacionMatriz1,ident)
##    print(multiplicacionMatriz2)
##    print(multiplicacionMatriz2)
##    multiMatriz(matriz1,matriz2)
##    productoTensorMatriz(matriz1,matriz2)
##    productoTensorVectores(vector1,vector2)
##    print(escalarPorVector(3,[[2,1], [1,-3]]))
##    matrizConjugada([[[1,-1],[2,7],[3,4]] , [[4,0],[5,10],[7,-4]]])
##    print(matrizTranspuesta([[[7, -9], [3, -4]], [[-1, 9], [5, -2]]]))
##    inversaVectores(vector1)
##    sumaVectores(vector1,vector2)
##    cartesianasPolares(num1)
##    multiplicar(num1,num2)
##    sumar(num1,num2)
##    restar(num1,num2)
##    divicion(num1,num2)
##    modulo([3,2])
##    conjugado([3,2])
##    prettyPrinting(c)
##    prettyprintingVectores(vectorFinal)
##    prettyprintingMatriz(matrizFinal)
##main()
=======
import math 
##import wolframalpha

num1 = [3,2]

num2 = [-1,2]


vector1 =[[1,1], [1,1]]
vector2 =[[0,0],[0,0]]
vectorFinal = []
vectorMultiComplejoVector = []
vectorFinalTensor = []


ident = [[[1, 0],[0,0]] , [[0,0],[0,0]]]
##matriz1 = [[[0, 0],[1,0]] , [[1,0],[0,0]]]
##matriz2 = [[[(1/(2**0.5)),0],[(1/(2**0.5)),0]] , [[(-1/(2**0.5)),0],[(1/(2**0.5)),0]]]
matrizTensorFinal = []
matrizFinal = []

c = [0,0]
def sumar(num1,num2):
    aux = []
    resuE = (num1[0])+(num2[0])
    resuI = (num1[1])+(num2[1])
    c[0],c[1] = resuE,resuI
    aux.append(resuE)
    aux.append(resuI)
    return (aux)

def restar(num1,num2):
    aux=[]
    resuE = (num1[0])-(num2[0])
    resuI = (num1[1])-(num2[1])
    
    c[0],c[1] = resuE,resuI
    aux.append(resuE)
    aux.append(resuI)
    return (aux)

def multiplicar(num1,num2):
    aux = []
    res1 = num1[0]*num2[0] 
    res2 = num1[0]*num2[1]
    res3 = num1[1]*num2[0]
    res4 = (num1[1]*num2[1])*-1
    res1 = res1+res4
    res2 = res2+res3
    aux.append(res1)
    aux.append(res2)
    c[0],c[1] = res1,res2
    return (aux)

def divicion(num1,num2):
    aux = num2[:]
    aux[-1]=aux[-1]*-1
    conjugado1=multiplicar(num1,aux)
    conjugado2=multiplicar(num2,aux)
    res1 = conjugado1[0]/conjugado2[0]
    res2 = conjugado1[1]/conjugado2[0]
    c[0],c[1]=res1,res2
    print(c)
    return (res1,res2)


def modulo(num1):
    resu = ((num1[0]**2)+(num1[1]**2))**0.5
    c[0],c[1]=resu,"null"
##    print(c)
    return resu
def inversa(num1):
    c[0],c[1]= num1[0]*-1,num1[1]*-1
    return  c[0],c[1]
def conjugado(num1):
    c[0],c[1]=num1[0],(num1[1]*-1)
##    print(c)
    return (c[0],c[1])

def cartesianasPolares(num1):
    hipo = ((num1[0]**2)+num1[1]**2)**(0.5)
    angulo = math.degrees(math.atan(num1[1]/num1[0]))

    if num1[0]<0 and num1[1]<0:
        angulo = angulo + 180
    elif 0>num1[1]:
        angulo = 360 -angulo
    elif 0>num1[0]:
        angulo = 180- angulo
    c[0],c[1]= hipo ,angulo
##    print(c)
    return (hipo,angulo)


def sumaVectores(vec1,vec2):
    print ("---------------")
    resu = []
    sumarRes = [0,0]
    if len(vec1)== len(vec2):
##        print(vec1[0])
##        for i in range(len(vec1)):
##            print(i)
##            print(type(vec1[i]),vec1[i])
##            print(type(vec2[i]),vec2[i])
##            sumNumeros=sumar(vec1[i],vec2[i])
####            resu.append(sumar(vec1[i],vec2[i]))
##            print(sumNumeros)
##            resu.append(sumNumeros)
##        print("Segunda entrada")
##        for j in range(len(resu)):
##            sumarRes = sumar(sumarRes,resu[j])
##    print(sumarRes)
##    return sumarRes
##        print("Entre")
        for i in range(2):
            resu.append(sumar(vec1[i],vec2[i]))
        for j in range(len(resu)):
            sumarRes = sumar(sumarRes,resu[j])
    print(sumarRes)
    return sumarRes



def inversaVectores(vec1):
    for i in range(len(vec1)):
        vectorFinal.append(inversa(vec1[i]))
##    print(vectorFinal)
    return vectorFinal

matriz1 = [[[1,-1],[2,7]] , [[4,0],[5,1]]]
matriz2 = [[[2, 0],[5,0]] , [[3,0],[7,0]]]

def adicionMat(mat1,mat2):
    for i in range(len(mat1)):
        aux = []
        for j in range(len(mat1[0])):
            aux.append(sumar(mat1[i][j],mat2[i][j]))
##    print(aux)
    return(aux)

def matrizTranspuesta(mat1):
    for i in range(len(mat1[0])):
        temporal = []
        for j in range(len(mat1)):
            temporal.append(mat1[j][i])
        matrizFinal.append(temporal)
    return matrizFinal

def productoInternoVectores(vec1,vec2):
    aux = []
    resu = [0,0]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
           aux.append(multiplicar(vec1[i],vec2[i]))
           resu = sumar(resu,aux[i])
    return(resu)
    
def matrizConjugada(vec1):
    resu = ""
    for i in range(len(vec1)):
        temporal = []

        for j in range(len(vec1[0])):
            temporalNumeros = []
            resu= (conjugado(vec1[i][j]))
            temporalNumeros.append(resu[0])
            temporalNumeros.append(resu[1])
            temporal.append(temporalNumeros)
        matrizFinal.append(temporal)
    return (matrizFinal)

def escalarPorVector(a,vec1):
    for i in range(len(vec1)):
        nuevaMatriz = []
        nuevaMatriz.append(vec1[i][0]*a)
        nuevaMatriz.append(vec1[i][1]*a)
        vectorMultiComplejoVector.append(nuevaMatriz)

    return (vectorMultiComplejoVector)


def escalarPorMatriz(a,mat1):
    for i in range(len(mat1)):
        aux = []
        aux.append(escalarPorVector(a,mat1[i]))
    return (aux)


def productoTensorVectores(vec1,vec2):
    vectorAux=[]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            vectorAux.append(multiplicar(vec1[i],vec2[j]))
    vectorFinal=vectorAux

    return vectorAux



def productoTensorMatriz(mat1,mat2):
    aux = []
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            aux.append(productoTensorVectores(mat1[i],mat2[j]))
    matrizTensorFinal = aux
    return aux    

def potenciaCuadrada (num):
    return (multiplicar(num,num))

def productoInternoVectores(vec1,vec2):
    resu = []
    if len(vec1)==len(vec2):
        cont = 0
        for i in range(len(vec1)):
            resu = multiplicar(vec1[i],vec2[i])
    return (resu)

def distanciaVectores(vec1,vec2):
    resu = []
    solucion = [0,0]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
            resu.append(restar(vec1[i],vec2[i]))
        for j in range(len(resu)):
            solucion = sumar(solucion,potenciaCuadrada(resu[j]))
    solucion[0]=solucion[0]**0.5
    vectorFinal = solucion
    return (solucion)

def normaDeVector(vec1):
    solucion = [0,0]
    for i in range(len(vec1)):
        solucion = sumar(solucion,potenciaCuadrada(vec1[i]))
    solucion[0]=solucion[0]**0.5
    return(solucion)


def multiMatriz(mat1,mat2):
    finMat = []
    for i in range(len(mat1)):
        aux = []
        for j in range(len(mat2[0])):
            cont = (0,0)
            for k in range(len(mat2)):
                sumas = multiplicar(mat1[i][k],mat2[k][j])
                cont = sumar(sumas,cont) 
            aux.append(cont)
        finMat.append(aux)
    return (finMat)
    

def prettyPrinting(c):
    if c[1]!="null":
        if c[1]>=0:
            print (str(c[0])+"+"+str(c[1])+"i")
        else:
            print (str(c[0])+""+str(c[1])+"i")
    else:
        print(str(c[0]))



def prettyprintingVectores(vf):
    vectorPintar = []
    if vectorFinal == [""]:
        print("No se pudo Sumar vector , Longitudes diferentes")
    else:
        for i in vf:
            if (i[1]>0):
                print(str(i[0])+"+"+str(i[1])+"i")
            else:
                print(str(i[0])+str(i[1])+"i")

                
    
def prettyprintingMatriz(matrizFinal):
    for i in matrizFinal:
        print(*i)


        

##def main():
##    print(productoInternoVectores([[2,1], [1,-3]],[[5,0],[2,0]]))
##    normaDeVector(vector1)
##    distanciaVectores(vector1,vector2)
##     print(escalarPorMatriz(2,[[[1,0],[2,0]] , [[4,0],[5,0]]]))
##    adicionMat(matriz1,matriz2)
##    m1 = productoTensorMatriz(matriz1,matriz1)
##    m2 = productoTensorMatriz(matriz1,matriz2)
##    print(multiMatriz([[[1,-1],[2,7]] , [[4,0],[5,1]]],[[[2, 0],[5,0]] , [[3,0],[7,0]]]))
##    multiplicacionMatriz2 = multiMatriz(multiplicacionMatriz1,ident)
##    print(multiplicacionMatriz2)
##    print(multiplicacionMatriz2)
##    multiMatriz(matriz1,matriz2)
##    productoTensorMatriz([[[1,-1],[2,7]] , [[4,0],[5,1]]],[[[2, 0],[5,0]] , [[3,0],[7,0]]])
##    productoTensorVectores(vector1,vector2)
##    print(escalarPorVector(3,[[2,1], [1,-3]]))
##    matrizConjugada([[[1,-1],[2,7],[3,4]] , [[4,0],[5,10],[7,-4]]])
##    print(matrizTranspuesta([[[7, -9], [3, -4]], [[-1, 9], [5, -2]]]))
##    inversaVectores(vector1)
##print(sumaVectores([[5,0],[2,0]],[[2,0],[8,0]]))
##    cartesianasPolares(num1)
##    multiplicar(num1,num2)
##    sumar(num1,num2)
##    restar(num1,num2)
##    divicion(num1,num2)
##    modulo([3,2])
##    conjugado([3,2])
##    prettyPrinting(c)
##    prettyprintingVectores(vectorFinal)
##    prettyprintingMatriz(matrizFinal)
##main()
>>>>>>> 20d5a4b0662d59f78a2c04e3af86cd86b5edd6b7
