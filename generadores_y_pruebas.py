
import math


def pruebaChiCuadrado(cantDatos, amplitud, datos):
    # m = math.ceil(math.sqrt(n))
    c = 10
    gl = c - 1
    
    #array con los valores de chi-cuadrado críticos
    tabla = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307, 19.675, 21.026, 22.362, 23.685, 24.996, 26.296, 27.587, 28.869, 30.144, 31.410]
    
    #utilizar amplitud por defecto
    # amplitud = 1/c
    
    fO = []
    fE = []
    calculado = []
    limiteInf = 0
    limiteSup = amplitud
    
    #darle limites o rango, en esta parte del codigo se llena dos arrays que son los limites dependiendo de la amplitud especificada
    limiteInf = []
    limiteInf.append(0)
    limiteSup = []
    for i in range(10):
        limiteSup.append(limiteInf[i] + amplitud)
        limiteInf.append(limiteSup[i])
    limiteInf = limiteInf[:-1]
    
    
    #prueba con los limites asignados
    contFO = 0
    for item in range(10):
        for i in range(len(datos)):
            if datos[i] >= limiteInf[item] and datos[i] < limiteSup[item]:
                contFO += 1
        fO.append(contFO)
        fE.append(int(cantDatos/c))
        contFO = 0
    
    #prueba con todos los limites es decir, con la amplitud por defecto
    # salida = 0
    # while(salida != m):
    #     salida += 1
    #     for i in range(len(datos)):
    #         if datos[i] >= limiteInf and datos[i] < limiteSup:
    #             contFO += 1
    #     fO.append(contFO)
    #     fE.append(int(n/m))
    #     limiteInf = limiteSup
    #     limiteSup = limiteInf + amplitud
    #     contFO = 0
        
    
    # se asignan los valores del chi cuadrado calculado 
    for i in range(len(fO)):
        calculado.append((fE[i] - fO[i])**2/fE[i])
    
    suma = sum(calculado) 
        
    print("PRUEBA DE CHI-CUADRADO-------------------------------------")   
    print("FO =",fO)
    print("FE =",fE)
    print("X^2 =",calculado)
    print("Suma chi-calculado = ", suma)
    print("chi-critico = ", tabla[gl-1])
    if suma <= tabla[gl-1] : print("El generador en bueno en cuanto a uniformidad") 
    else: print("El generador no es bueno porque el chi-cuadrado es mayor al chi-critico")
    



def generatorLineal(x0,a,c,m, cantDatos):
    # x0 = int(input("X0: "))
    # a = int(input("a: "))
    # c = int(input("c: "))
    # m = int(input("m: "))
    stop = x0
    periodo = 1
    datos_xn = []
    datos_rn = []
    
    datos_xn.append(x0)
    rn = x0/m
    datos_rn.append(rn)
    
    x0 = (a * x0 + c) % m
    
    while(x0 != stop):
        datos_xn.append(x0)
        rn = x0/m
        datos_rn.append(rn)
        x0 = (a * x0 + c) % m
        periodo += 1
    
    #retorna la cantidad de datos especificada
    # for i in range(24):
    #     datos_xn.append(x0)
    #     rn = x0/m
    #     datos_rn.append(rn)
    #     x0 = (a * x0 + c) % m
    #     periodo += 1
    
    print("Xn = ",datos_xn)
    print("Rn = ",datos_rn)
    print("Periodo = ",periodo)
    print("------------------------------------------")
    
    #llamado al metodo para hacer la prueba de chi-cuadrado
    datos_rn = datos_rn[:cantDatos]
    pruebaChiCuadrado(cantDatos, 0.1, datos_rn)
    

def generadorEstandarMinimo(x0, a, m):
    
    r = m % a
    q = math.floor(m / a)
    m = a * q + r
    stop = x0
    periodo = 1
    datos_xn = []
    
    print("r: ",r, "\nq: ",q, "\nm: ",m)
   
    while(True):
        periodo += 1

        if  (a * (x0 % q) - r * math.floor(x0/q)) >= 0:
          x0 = (a * (x0 % q) - r * math.floor(x0/q)) % m
        else:
          x0 = (a * (x0 % q) - r * math.floor(x0/q) + m) % m
        
        stop = x0
        if stop in datos_xn:
            break
        else:
            datos_xn.append(x0)
    
    print("Xn = ",datos_xn)
    print("Periodo = ", periodo)
     
print("Generador lineal")
# generatorLineal(7, 3, 4, 20)
generatorLineal(5, 106, 1283, 6075, 1000)

# print("\nGenerador estandar minimo")
# generadorEstandarMinimo(27, 17, 100)

