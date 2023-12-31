
import math


def pruebaChiCuadrado(cantDatos, amplitud, datos):
    # m = math.ceil(math.sqrt(n))
    c = 10
    gl = c - 1
    
    #array con los valores de chi-cuadrado críticos
    tabla = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307, 19.675, 21.026, 22.362, 23.685, 24.996, 26.296, 27.587, 28.869, 30.144, 31.410, 32.671, 33.924, 35.172, 36.415, 37.652, 38.885, 40.113, 41.337, 42.557, 43.773]
    
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
    for item in range(c):
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
        
    
    # se guardan los valores del chi cuadrado calculado 
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
    
def pruebaKolmogorovSmirnov(cantDatos, amplitud, datos):
    c = 5
    gl = cantDatos
    dM_critico = 1.36 / math.sqrt(gl)
    
    fO = []
    fOA = []
    pOA = []
    pEA = []
    calculado = []
    limiteInf = 0
    limiteSup = amplitud
    
    #darle limites o rango, en esta parte del codigo se llena dos arrays que son los limites dependiendo de la amplitud especificada
    limiteInf = []
    limiteInf.append(0)
    limiteSup = []
    for i in range(c):
        limiteSup.append(round(limiteInf[i] + amplitud, 1))
        limiteInf.append(limiteSup[i])
    limiteInf = limiteInf[:-1]
    
    contFO = 0
    for item in range(c):
        for i in range(len(datos)):
            if datos[i] >= limiteInf[item] and datos[i] < limiteSup[item]:
                contFO += 1
        fO.append(contFO)
        contFO = 0
    
    #asignar los valores de la sumatoria para FOA
    
    sumatoria = 0
    for i in fO:
        sumatoria += i
        fOA.append(sumatoria)
        
    #asignar los valores de la probabilidad observada acumulada POA
    for i in fOA:
        pOA.append(i/cantDatos)
        
    #asignar los valores de la probabilidad esperada acumulada PEA
    for i in limiteSup:
        pEA.append(round(i, 1))
    
    #asignar el calculo de la prueba    
    for i in range(len(fO)):
        calculado.append(round(abs(pEA[i] - pOA[i]), 3))
    
    #buscar el numero mayor para el D calculado
    dM_calculado = max(calculado)
        
        
    
    print("FO = ", fO)
    print("FOA = ",fOA)
    print("POA = ", pOA)
    print("PEA = ", pEA)
    print("|PEA - POA| = ", calculado)
    print("DM calculado = ", dM_calculado)
    print("DM critico = ", dM_critico)
    print("-------------------------------------------------------------")
    if dM_calculado <= dM_critico: print("El generador es bueno en cuanto a unifomidad")
    else: print("El generador no es bueno en cuanto a uniformidad porque el DM-calculado es mayor al DM-critico")
    
def pruebaIndependencia_corridas(datos):
    # datos = [0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
    #         0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
    #         0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
    #         0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29]
    
#     datos = [0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
# 0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,
# 0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
# 0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91]
    signos = []
    z = [-1.96, 1.96]
    
    for i in range(len(datos)-1):
        if datos[i] < datos[i+1]: signos.append("+")
        else: signos.append("-")
            
    n1 = 0
    n2 = 0
    for signo in signos:
        if signo == "+": n1 += 1
        else: n2 += 1
            
    cont = 0
    for i in range(len(signos)):
        print(signos[i], end = " ")
        cont += 1
        if cont == 10: 
            print("\n")
            cont = 0
            
    cantCorridas = 1
    for i in range(len(signos) - 1):
        if signos[i] != signos[i + 1]:
            cantCorridas += 1
    
    n = len(datos)
    media = (2*n - 1)/3
    varianza = math.sqrt((16*n - 29)/90)
    zObs = (cantCorridas - media)/varianza
        
        
        
    print("\nn1 = ",n1,"\n","n2 = ",n2)
    print("corridas = ",cantCorridas)
    print("Zobs = ",zObs)
    if zObs > z[0] and zObs < z[1]:
        print("No hay evidencia para rechazar la hipotesis de independencia")

def pruebaSerie(datos):
    datos = [0.22461, 0.16079, 0.04036, 0.00115, 0.90845, 0.4653, 0.57244, 0.56637, 0.33142, 0.31993, 0.45972, 0.03052, 0.3749, 0.00066, 0.7603, 0.85726, 0.5032, 0.69631, 0.27826, 0.31928, 0.79147, 0.55291, 0.4087, 0.25956, 0.54569, 0.68597, 0.9219, 0.34651, 0.23954, 0.14225, 0.29237, 0.77293, 0.63084, 0.07777, 0.57014, 0.78343, 0.68368, 0.33864, 0.6064, 0.78244, 0.81772, 0.0443, 0.78031, 0.69844, 0.7114, 0.52108, 0.99163, 0.48105, 0.63905, 0.03888]
    
    tabla = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307, 19.675, 21.026, 22.362, 23.685, 24.996, 26.296, 27.587, 28.869, 30.144, 31.410, 32.671, 33.924, 35.172, 36.415, 37.652, 38.885, 40.113, 41.337, 42.557, 43.773]
    
    k = 2
    numGrupos = int(len(datos)/k)
    clases = math.ceil(math.sqrt(numGrupos))
    intervalos = math.ceil(pow(math.sqrt(numGrupos), 1/k))
    fE = numGrupos / clases
    gl = clases - 1
    
    #generar los limites
    amplitud = 1/5
    limiteInf = 0
    limites = []
    for i in range(5):
        par = (limiteInf, limiteInf + amplitud)
        limites.append(par)
        limiteInf += amplitud
    
    #organizar los numeros en pares 
    pares = []
    for i in range(0, len(datos), 2):
        par = (datos[i], datos[i + 1])
        pares.append(par)
    
    #llenar la matriz de ceros
    matriz = []
    for i in range(5):
        fila = [0] * 5
        matriz.append(fila)
        
    #hallando la frecuencia obtenida para cada intervalo
    for i in range(numGrupos):
        for x in range(5):
            for y in range(5):
                if (pares[i][0] >= limites[x][0] and pares[i][0] < limites[x][1]) and (pares[i][1] >= limites[y][0] and pares[i][1] < limites[y][1]):
                    matriz[x][y] += 1
                    
    
    #llenar la matriz de ceros
    matrizChi_cuadrado = []
    for i in range(5):
        fila = [0] * 5
        matrizChi_cuadrado.append(fila)
        
    #prueba chi-cuadrado
    for i in range(5):
        for j in range(5):
            fO = matriz[i][j]
            matrizChi_cuadrado[i][j] = (fE - fO)**2/fE
            
    suma = 0
    for i in range(5):
        for j in range(5):
            suma += matrizChi_cuadrado[i][j]        
        
            
    # for i in range(numGrupos):
    #     if (pares[i][0] >= 0 and pares[i][0] < 0.2) and (pares[i][1] >= 0 and pares[i][1] < 0.2): matriz[0][0] += 1 
    #     if (pares[i][0] >= 0 and pares[i][0] < 0.2) and (pares[i][1] >= 0.2 and pares[i][1] < 0.4): matriz[0][1] += 1 
    #     if (pares[i][0] >= 0 and pares[i][0] < 0.2) and (pares[i][1] >= 0.4 and pares[i][1] < 0.6): matriz[0][2] += 1 
    #     if (pares[i][0] >= 0 and pares[i][0] < 0.2) and (pares[i][1] >= 0.6 and pares[i][1] < 0.8): matriz[0][3] += 1 
    #     if (pares[i][0] >= 0 and pares[i][0] < 0.2) and (pares[i][1] >= 0.8 and pares[i][1] < 1): matriz[0][4] += 1 
       
    #     if (pares[i][0] >= 0.2 and pares[i][0] < 0.4) and (pares[i][1] >= 0 and pares[i][1] < 0.2): matriz[1][0] += 1 
    #     if (pares[i][0] >= 0.2 and pares[i][0] < 0.4) and (pares[i][1] >= 0.2 and pares[i][1] < 0.4): matriz[1][1] += 1 
    #     if (pares[i][0] >= 0.2 and pares[i][0] < 0.4) and (pares[i][1] >= 0.4 and pares[i][1] < 0.6): matriz[1][2] += 1 
    #     if (pares[i][0] >= 0.2 and pares[i][0] < 0.4) and (pares[i][1] >= 0.6 and pares[i][1] < 0.8): matriz[1][3] += 1 
    #     if (pares[i][0] >= 0.2 and pares[i][0] < 0.4) and (pares[i][1] >= 0.8 and pares[i][1] < 1): matriz[1][4] += 1 
        
    #     if (pares[i][0] >= 0.4 and pares[i][0] < 0.6) and (pares[i][1] >= 0 and pares[i][1] < 0.2): matriz[2][0] += 1 
    #     if (pares[i][0] >= 0.4 and pares[i][0] < 0.6) and (pares[i][1] >= 0.2 and pares[i][1] < 0.4): matriz[2][1] += 1 
    #     if (pares[i][0] >= 0.4 and pares[i][0] < 0.6) and (pares[i][1] >= 0.4 and pares[i][1] < 0.6): matriz[2][2] += 1 
    #     if (pares[i][0] >= 0.4 and pares[i][0] < 0.6) and (pares[i][1] >= 0.6 and pares[i][1] < 0.8): matriz[2][3] += 1 
    #     if (pares[i][0] >= 0.4 and pares[i][0] < 0.6) and (pares[i][1] >= 0.8 and pares[i][1] < 1): matriz[2][4] += 1 
        
    #     if (pares[i][0] >= 0.6 and pares[i][0] < 0.8) and (pares[i][1] >= 0 and pares[i][1] < 0.2): matriz[3][0] += 1 
    #     if (pares[i][0] >= 0.6 and pares[i][0] < 0.8) and (pares[i][1] >= 0.2 and pares[i][1] < 0.4): matriz[3][1] += 1 
    #     if (pares[i][0] >= 0.6 and pares[i][0] < 0.8) and (pares[i][1] >= 0.4 and pares[i][1] < 0.6): matriz[3][2] += 1 
    #     if (pares[i][0] >= 0.6 and pares[i][0] < 0.8) and (pares[i][1] >= 0.6 and pares[i][1] < 0.8): matriz[3][3] += 1 
    #     if (pares[i][0] >= 0.6 and pares[i][0] < 0.8) and (pares[i][1] >= 0.8 and pares[i][1] < 1): matriz[3][4] += 1 
        
    #     if (pares[i][0] >= 0.8 and pares[i][0] < 1) and (pares[i][1] >= 0 and pares[i][1] < 0.2): matriz[4][0] += 1 
    #     if (pares[i][0] >= 0.8 and pares[i][0] < 1) and (pares[i][1] >= 0.2 and pares[i][1] < 0.4): matriz[4][1] += 1 
    #     if (pares[i][0] >= 0.8 and pares[i][0] < 1) and (pares[i][1] >= 0.4 and pares[i][1] < 0.6): matriz[4][2] += 1 
    #     if (pares[i][0] >= 0.8 and pares[i][0] < 1) and (pares[i][1] >= 0.6 and pares[i][1] < 0.8): matriz[4][3] += 1 
    #     if (pares[i][0] >= 0.8 and pares[i][0] < 1) and (pares[i][1] >= 0.8 and pares[i][1] < 1): matriz[4][4] += 1 
    
    print("limites: ", limites)
    print("Matriz: ",matriz)
    print("Matriz con los chi-calculados: ",matrizChi_cuadrado)
    print("numero de clases: ", clases)
    print("intervalos para cada dimension: ", intervalos)
    print("probabilidad teorica en cada celda: ", 1/clases)
    print("Frecuencia esperada: ", fE)
    print("Valor de la suma chi calculado: ",suma)
    print("Grados de libertad: ",gl)
    print("chi-critico = ", tabla[gl-1])
    if suma <= tabla[gl-1] : print("El generador en bueno en cuanto a independencia") 
    else: print("El generador no es bueno porque el chi-calculado es mayor al chi-critico")
  
def pruebaPoker3(datos):
    datos = [0.959, 0.972, 0.178, 0.427, 0.299, 0.425, 0.372, 0.015, 0.153, 0.316, 0.087, 0.615, 0.188, 0.239, 0.808, 0.444, 0.084, 0.166, 0.199, 0.182, 0.532, 0.904, 0.216,0.466,0.317, 0.713, 0.051, 0.229, 0.577, 0.299, 0.185, 0.222, 0.296, 0.854, 0.283, 0.324, 0.913, 0.158, 0.954, 0.582]   
    
    tabla = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592]
    
    k = 3
    n = len(datos)
    fO = []
    fE = []
    probabilidad = []
    probabilidad.append(0.01)
    probabilidad.append(0.27)
    probabilidad.append(0.72)
    gl = len(probabilidad) - 1
    
    for num in probabilidad:
        valor = num * n
        fE.append(valor)
    
    tercia = 0
    par = 0
    pachuca = 0
    for num in datos:
        primer_digito = int(num * 10) % 10
        segundo_digito = int(num * 100) % 10
        tercer_digito = int(num * 1000) % 10
        
        if primer_digito == segundo_digito == tercer_digito:
            tercia += 1
        
        par1 = (primer_digito == segundo_digito)
        par2 = (primer_digito == tercer_digito)
        par3 = (segundo_digito == tercer_digito)
        if  (par1 and (primer_digito != tercer_digito)) or (par2 and (primer_digito != segundo_digito)) or (par3 and (segundo_digito != primer_digito)):
            par += 1
            
        if (primer_digito != segundo_digito) and (primer_digito != tercer_digito) and (segundo_digito != tercer_digito):
            pachuca += 1
    fO.append(tercia)        
    fO.append(par)        
    fO.append(pachuca)
        
    #calculado el chi-calculado
    chi_calculado = []
    for i in range(len(fO)):
        valor = (fE[i] - fO[i])**2/fE[i]
        chi_calculado.append(valor)
    
    
    #suma del chi-calculado
    suma = sum(chi_calculado)
        
    print("Frecuencia obtenida: ",fO) 
    print("Frecuencia esperada",fE)            
    print("chi-calculado: ",chi_calculado)
    print("Grados de libertad: ",gl)
    print("Valor de la suma chi calculado: ",suma)
    print("chi-critico = ", tabla[gl-1])
    if suma <= tabla[gl-1] : print("El generador en bueno en cuanto a independencia") 
    else: print("El generador no es bueno porque el chi-calculado es mayor al chi-critico")
            

def pruebaPoker5(datos):
    # datos = [.72484, .48999, .50502, .39528, .36782, .90234, .71890, .61234, .86322, .94134, .99872, .27657, .34565, .02345, .67347, .10987, .25678, .25593, .82345, .12387, .05389, .82474, .59289, .36782, .03991, .10461, .93716, .16894, .98953, .73231]
    
    tabla = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592]
    
    k = 5
    n = len(datos)
    fO = []
    fE = []
    probabilidad = []
    probabilidad.append(0.3024)
    probabilidad.append(0.5040)
    probabilidad.append(0.1080)
    probabilidad.append(0.0720)
    probabilidad.append(0.0090)
    probabilidad.append(0.0045)
    probabilidad.append(0.0001)
    gl = len(probabilidad) - 1
    
    for num in probabilidad:
        valor = num * n
        fE.append(valor)
    
    quintilla = 0
    poker = 0
    tercia = 0
    par = 0
    dosPares = 0
    pachuca = 0
    full = 0
    for num in datos:
        primer_digito = int(num * 10) % 10
        segundo_digito = int(num * 100) % 10
        tercer_digito = int(num * 1000) % 10
        cuarto_digito = int(num * 10000) % 10
        quinto_digito = int(num * 100000) % 10
        
        #QUINTILLA, todos iguales
        if primer_digito == segundo_digito == tercer_digito == cuarto_digito == quinto_digito:
            quintilla += 1
        
        #PACHUCA, todos diferentes
        if (primer_digito != segundo_digito) and (primer_digito != tercer_digito) and (primer_digito != cuarto_digito) and (primer_digito != quinto_digito):
            if (segundo_digito != tercer_digito) and (segundo_digito != cuarto_digito) and (segundo_digito != quinto_digito):
                if (tercer_digito != cuarto_digito) and (tercer_digito != quinto_digito) and (cuarto_digito != quinto_digito):
                    pachuca += 1
        
        #UN PAR, 2 iguales 3 diferentes
        par1 = (primer_digito == segundo_digito)
        par2 = (primer_digito == tercer_digito)
        par3 = (primer_digito == cuarto_digito)
        par4 = (primer_digito == quinto_digito)
        if (par1 and (primer_digito != tercer_digito) and (primer_digito != cuarto_digito) and (primer_digito != quinto_digito)):
            if (tercer_digito != cuarto_digito) and (tercer_digito != quinto_digito) and (cuarto_digito != quinto_digito):
                par += 1
        if (par2 and (primer_digito != segundo_digito) and (primer_digito != cuarto_digito) and (primer_digito != quinto_digito)):
            if (segundo_digito != cuarto_digito) and (segundo_digito != quinto_digito) and (cuarto_digito != quinto_digito):
                par += 1
        if (par3 and (primer_digito != segundo_digito) and (primer_digito != tercer_digito) and (primer_digito != quinto_digito)):
            if (segundo_digito != tercer_digito) and (segundo_digito != quinto_digito) and (tercer_digito != quinto_digito):
                par += 1
        if (par4 and (primer_digito != segundo_digito) and (primer_digito != tercer_digito) and (primer_digito != cuarto_digito)):
            if (segundo_digito != tercer_digito) and (segundo_digito != cuarto_digito) and (tercer_digito != cuarto_digito):
                par += 1
        
        par5 = (segundo_digito == tercer_digito)
        par6 = (segundo_digito == cuarto_digito)
        par7 = (segundo_digito == quinto_digito)
        if (par5 and (segundo_digito != primer_digito) and (segundo_digito != cuarto_digito) and (segundo_digito != quinto_digito)):
            if (primer_digito != cuarto_digito) and (primer_digito != quinto_digito) and (cuarto_digito != quinto_digito):
                par += 1
        if (par6 and (segundo_digito != primer_digito) and (segundo_digito != tercer_digito) and (segundo_digito != quinto_digito)):
           if (primer_digito != tercer_digito) and (primer_digito != quinto_digito) and (tercer_digito != quinto_digito):
                par += 1
        if (par7 and (segundo_digito != primer_digito) and (segundo_digito != tercer_digito) and (segundo_digito != cuarto_digito)):
            if (primer_digito != tercer_digito) and (primer_digito != cuarto_digito) and (tercer_digito != cuarto_digito):
                par += 1
            
        par8 = (tercer_digito == cuarto_digito)
        par9 = (tercer_digito == quinto_digito)
        if (par8 and (tercer_digito != primer_digito) and (tercer_digito != segundo_digito) and (tercer_digito != quinto_digito)):
            if (segundo_digito != primer_digito) and (primer_digito != quinto_digito) and (segundo_digito != quinto_digito):
                par += 1
        if (par9 and (tercer_digito != primer_digito) and (tercer_digito != segundo_digito) and (tercer_digito != cuarto_digito)):
            if (segundo_digito != primer_digito) and (primer_digito != tercer_digito) and (tercer_digito != segundo_digito):
                par += 1
        
        par10 = (cuarto_digito == quinto_digito)
        if (par10 and (cuarto_digito != primer_digito) and (cuarto_digito != segundo_digito) and (cuarto_digito != tercer_digito)):
            if (segundo_digito != primer_digito) and (primer_digito != tercer_digito) and (segundo_digito != tercer_digito):
                par += 1
        
        #DOS PARES, 2 pares 1 diferente
        if ((par5 and par10) and (segundo_digito != cuarto_digito)) and (segundo_digito != primer_digito and cuarto_digito != primer_digito):
            dosPares += 1
        if ((par6 and par9) and (segundo_digito != tercer_digito)) and (segundo_digito != primer_digito and tercer_digito != primer_digito):
            dosPares += 1
        if ((par7 and par8) and (segundo_digito != tercer_digito)) and (segundo_digito != primer_digito and tercer_digito != primer_digito):
            dosPares += 1
        
        if ((par2 and par10) and (primer_digito != cuarto_digito)) and (primer_digito != segundo_digito and cuarto_digito != segundo_digito):
            dosPares += 1
        if ((par3 and par9) and (primer_digito != tercer_digito)) and (primer_digito != segundo_digito and tercer_digito != segundo_digito):
            dosPares += 1
        if ((par5 and par10) and (primer_digito != tercer_digito)) and (primer_digito != segundo_digito and tercer_digito != segundo_digito):
            dosPares += 1
            
        if ((par3 and par7) and (segundo_digito != cuarto_digito)) and (segundo_digito != tercer_digito and cuarto_digito != tercer_digito):
            dosPares += 1
        if ((par1 and par10) and (segundo_digito != cuarto_digito)) and (segundo_digito != tercer_digito and cuarto_digito != tercer_digito):
            dosPares += 1
        if ((par4 and par6) and (primer_digito != segundo_digito)) and (primer_digito != tercer_digito and segundo_digito != tercer_digito):
            dosPares += 1
            
        if ((par1 and par9) and (segundo_digito != tercer_digito)) and (segundo_digito != cuarto_digito and tercer_digito != cuarto_digito):
            dosPares += 1
        if ((par2 and par7) and (segundo_digito != tercer_digito)) and (segundo_digito != cuarto_digito and tercer_digito != cuarto_digito):
            dosPares += 1
        if ((par4 and par5) and (primer_digito != segundo_digito)) and (primer_digito != cuarto_digito and segundo_digito != cuarto_digito):
            dosPares += 1
            
        if ((par2 and par6) and (primer_digito != segundo_digito)) and (primer_digito != quinto_digito and segundo_digito != quinto_digito):
            dosPares += 1
        if ((par1 and par8) and (segundo_digito != tercer_digito)) and (segundo_digito != quinto_digito and tercer_digito != quinto_digito):
            dosPares += 1
        if ((par3 and par5) and (primer_digito != segundo_digito)) and (primer_digito != quinto_digito and segundo_digito != quinto_digito):
            dosPares += 1
            
        #TERCIA, 3 iguales 2 diferentes
        igual1 = (tercer_digito == cuarto_digito == quinto_digito)
        igual2 = (segundo_digito == cuarto_digito == quinto_digito)
        igual3 = (segundo_digito == tercer_digito == quinto_digito)
        igual4 = (segundo_digito == tercer_digito == cuarto_digito)
        igual5 = (primer_digito == cuarto_digito == quinto_digito)
        igual6 = (primer_digito == tercer_digito == quinto_digito)
        igual7 = (primer_digito == tercer_digito == cuarto_digito)
        igual8 = (primer_digito == segundo_digito == quinto_digito)
        igual9 = (primer_digito == segundo_digito == cuarto_digito)
        igual10 = (primer_digito == segundo_digito == tercer_digito)
        if (igual1 and (igual1 != primer_digito and igual1 != segundo_digito)) and primer_digito != segundo_digito:
            tercia += 1
        if (igual2 and (igual1 != primer_digito and igual1 != tercer_digito)) and primer_digito != tercer_digito:
            tercia += 1
        if (igual3 and (igual1 != primer_digito and igual1 != cuarto_digito)) and primer_digito != cuarto_digito:
            tercia += 1
        if (igual4 and (igual1 != primer_digito and igual1 != quinto_digito)) and primer_digito != quinto_digito:
            tercia += 1
        if (igual5 and (igual1 != segundo_digito and igual1 != tercer_digito)) and segundo_digito != tercer_digito:
            tercia += 1
        if (igual6 and (igual1 != segundo_digito and igual1 != cuarto_digito)) and segundo_digito != cuarto_digito:
            tercia += 1
        if (igual7 and (igual1 != segundo_digito and igual1 != quinto_digito)) and segundo_digito != quinto_digito:
            tercia += 1
        if (igual8 and (igual1 != tercer_digito and igual1 != cuarto_digito)) and tercer_digito != cuarto_digito:
            tercia += 1
        if (igual9 and (igual1 != tercer_digito and igual1 != quinto_digito)) and tercer_digito != quinto_digito:
            tercia += 1
        if (igual10 and (igual1 != cuarto_digito and igual1 != quinto_digito)) and cuarto_digito != quinto_digito:
            tercia += 1
            
        #POKER, 4 iguales 1 diferente
        if (primer_digito == segundo_digito == tercer_digito == cuarto_digito) and primer_digito != quinto_digito:
            poker += 1
        if (primer_digito == segundo_digito == tercer_digito == quinto_digito) and primer_digito != cuarto_digito:
            poker += 1
        if (primer_digito == segundo_digito == quinto_digito == cuarto_digito) and primer_digito != tercer_digito:
            poker += 1
        if (primer_digito == quinto_digito == tercer_digito == cuarto_digito) and primer_digito != segundo_digito:
            poker += 1
        if (quinto_digito == segundo_digito == tercer_digito == cuarto_digito) and segundo_digito != primer_digito:
            poker += 1
        
        #FULL, 2 iguales, 3 iguales
        if (par1 and igual1) and (primer_digito != tercer_digito):
            full +=1
        if (par2 and igual2) and (primer_digito != segundo_digito):
            full +=1
        if (par3 and igual3) and (primer_digito != segundo_digito):
            full +=1
        if (par4 and igual4) and (primer_digito != segundo_digito):
            full +=1
        if (par5 and igual5) and (primer_digito != segundo_digito):
            full +=1
        if (par6 and igual6) and (primer_digito != segundo_digito):
            full +=1
        if (par7 and igual7) and (primer_digito != segundo_digito):
            full +=1
        if (par8 and igual8) and (segundo_digito != tercer_digito):
            full +=1
        if (par9 and igual9) and (segundo_digito != tercer_digito):
            full +=1
        if (par10 and igual10) and (cuarto_digito != tercer_digito):
            full +=1
   
    fO.append(pachuca)
    fO.append(par)        
    fO.append(dosPares)
    fO.append(tercia)
    fO.append(full)
    fO.append(poker)
    fO.append(quintilla)        
    
    #calculado el chi-calculado
    chi_calculado = []
    for i in range(len(fO)):
        valor = (fE[i] - fO[i])**2/fE[i]
        chi_calculado.append(valor)
    
    
    #suma del chi-calculado
    suma = sum(chi_calculado)
        
    print("Frecuencia obtenida: ",fO) 
    print("Frecuencia esperada",fE)      
    print("Suma frecuencia esperada (FE): ", sum(fE))      
    print("chi-calculado: ",chi_calculado)
    print("Grados de libertad: ",gl)
    print("Valor de la suma chi calculado: ",suma)
    print("chi-critico = ", tabla[gl-1])
    if suma <= tabla[gl-1] : print("El generador en bueno en cuanto a independencia") 
    else: print("El generador no es bueno porque el chi-calculado es mayor al chi-critico")


def generatorLineal(x0,a,c,m, cantDatos):

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
        if periodo >= 10000:
            break
            
    # retorna la cantidad de datos especificada
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
    pruebaKolmogorovSmirnov(cantDatos, 0.2, datos_rn)
    # pruebaSerie(datos_rn)
    # pruebaPoker5(datos_rn)
    

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
# generatorLineal(5, 5, 5, 32, 30)
# generatorLineal(0, 106, 1283, 6075, 1000)
# generatorLineal(5, 255, 100, 1032, 1000)

# print("\nGenerador estandar minimo")
# generadorEstandarMinimo(27, 17, 100)
# generadorEstandarMinimo(5, 12, 21)

