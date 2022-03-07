
base = 1600
#altura = 340
altura = 560
ancho = 600
grosor = 18
n_columnas = 2
n_filas = 2
#tablero_sep_filas = False
#is_cajones = True


mueble = {}


def if_jgm(condition = None, valor_true = None, valor_false = None):
    if condition:
        return valor_true
    else:
        return valor_false


mueble['tablero superior'] = [base-2*grosor, ancho]

mueble['tablero inferior'] = mueble['tablero superior']

mueble['tablero derecho'] = [ancho, altura]

mueble['tablero izquierdo'] = [ancho, altura]


for i in range(1, n_columnas):
    mueble['division columna '+str(i)+'_'+str(i+1)] = [ancho, altura-2*grosor]


# IDEAL PARA CALCULAR LAS DIMENSIONES DE LAS COLUMNAS
# IDEAL PARA CALCULAR LA ALTURA DE CADA CAJON
def particion_espacios(largo_disponible = None, n_divisiones = None, espacio_entre_dimensiones = False, grosor_entre_dimensiones = None):
    
    largo_disponible = largo_disponible - if_jgm(espacio_entre_dimensiones, grosor_entre_dimensiones*(n_divisiones-1), 0)
    
    residuo_aux = largo_disponible%n_divisiones
    divisor_aux = int((largo_disponible - residuo_aux)/n_divisiones)
    
    largo_columnas_aux = []
    
    for i in range(n_divisiones):
        largo_columnas_aux.append(divisor_aux + if_jgm(residuo_aux == 0, 0, 1))
        residuo_aux = residuo_aux - if_jgm(residuo_aux == 0, 0, 1)
        
    return largo_columnas_aux


largo_columnas = particion_espacios(base-2*grosor, n_columnas, True, grosor)
#largo_columnas


altura_cajones = particion_espacios(altura-2*grosor-(30*n_filas-15), n_filas, False, grosor)
#altura_cajones


def cajon_dimensiones(base = None, altura = None, profundidad = None, grosor = None, coordenadas = None):
    
    cajon = dict()
    
    if coordenadas == None:
        cajon['cajon parte delantera'] = [base-2*grosor, altura]
        cajon['cajon parte trasera'] = [base-2*grosor, altura]
        cajon['cajon parte derecha'] = [profundidad, altura]
        cajon['cajon parte izquierda'] = [profundidad, altura]
        cajon['cajon parte piso'] = [profundidad-2*grosor, base-2*grosor]

    else:
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte delantera'] = [base-2*grosor, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte trasera'] = [base-2*grosor, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte derecha'] = [profundidad, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte izquierda'] = [profundidad, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte piso'] = [profundidad-2*grosor, base-2*grosor]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' tapa delantera'] = [base+26+5*2, base+15+10]
    
    return(cajon)
 

cajones_total = dict()

for i in range(n_filas):
    for j in range(n_columnas):
        cajones_total.update(cajon_dimensiones(largo_columnas[j]-26, altura_cajones[i], profundidad = ancho-50, grosor = grosor, coordenadas = [i+1, j+1]))

cajones_total

mueble.update(cajones_total)
mueble


import pandas as pd
import numpy as np

df_final = pd.DataFrame(mueble).T.assign(
    LARGO = lambda x: x.max(axis=1),
    BASE = lambda x: x.min(axis=1)).drop(columns = [0,1])

df_final

df_final2 = df_final.value_counts().sort_index().reset_index().rename(columns={0:'CANTIDAD'})

df_final2


# FUNCIONES
###########


def if_jgm(condition = None, valor_true = None, valor_false = None):
    if condition:
        return valor_true
    else:
        return valor_false



def cajon_dimensiones(base = None, altura = None, profundidad = None, grosor = None, coordenadas = None):
    
    cajon = dict()
    
    if coordenadas == None:
        cajon['cajon parte delantera'] = [base-2*grosor, altura]
        cajon['cajon parte trasera'] = [base-2*grosor, altura]
        cajon['cajon parte derecha'] = [profundidad, altura]
        cajon['cajon parte izquierda'] = [profundidad, altura]
        cajon['cajon parte piso'] = [profundidad-2*grosor, base-2*grosor]

    else:
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte delantera'] = [base-2*grosor, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte trasera'] = [base-2*grosor, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte derecha'] = [profundidad, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte izquierda'] = [profundidad, altura]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' parte piso'] = [profundidad-2*grosor, base-2*grosor]
        cajon['cajon '+str(coordenadas[0])+'_'+str(coordenadas[1])+ ' tapa delantera'] = [base+26+5*2, base+15+10]
    
    return(cajon)



def mueble_cajonera(base = None, altura = None, ancho = None, grosor = None, n_columnas = None, n_filas = None, is_cajon = True, base_soporte = None):

    mueble = {}
    
    mueble['tablero superior'] = [base-2*grosor, ancho]
    
    mueble['tablero inferior'] = mueble['tablero superior']
    
    mueble['tablero derecho'] = [ancho, altura]
    
    mueble['tablero izquierdo'] = [ancho, altura]
    
    
    if base_soporte != None:
    
        mueble['base soporte delante'] = [base-2*grosor, base_soporte]
    
        mueble['base soporte detras'] = [base-2*grosor, base_soporte]
    
        altura = altura - base_soporte
    
    
    for i in range(1, n_columnas):
        mueble['division columna '+str(i)+'_'+str(i+1)] = [ancho, altura-2*grosor]
    
    
    # IDEAL PARA CALCULAR LAS DIMENSIONES DE LAS COLUMNAS
    # IDEAL PARA CALCULAR LA ALTURA DE CADA CAJON
    def particion_espacios(largo_disponible = None, n_divisiones = None, espacio_entre_dimensiones = False, grosor_entre_dimensiones = None):
        
        largo_disponible = largo_disponible - if_jgm(espacio_entre_dimensiones, grosor_entre_dimensiones*(n_divisiones-1), 0)
        
        residuo_aux = largo_disponible%n_divisiones
        divisor_aux = int((largo_disponible - residuo_aux)/n_divisiones)
        
        largo_columnas_aux = []
        
        for i in range(n_divisiones):
            largo_columnas_aux.append(divisor_aux + if_jgm(residuo_aux == 0, 0, 1))
            residuo_aux = residuo_aux - if_jgm(residuo_aux == 0, 0, 1)
            
        return largo_columnas_aux
    
    
    largo_columnas = particion_espacios(base-2*grosor, n_columnas, True, grosor)
    #largo_columnas
    
    
    altura_cajones = particion_espacios(altura-2*grosor-(30*n_filas-15), n_filas, False, grosor)
    #altura_cajones
    
    
    if is_cajon:
    
        cajones_total = dict()
        
        for i in range(n_filas):
            for j in range(n_columnas):
                cajones_total.update(cajon_dimensiones(largo_columnas[j]-26, altura_cajones[i], profundidad = ancho-50, grosor = grosor,
                                                       coordenadas = [i+1, j+1]))
        
        mueble.update(cajones_total)
    
    
    import pandas as pd
    #import numpy as np
    
    df_final = pd.DataFrame(mueble).T.assign(
        LARGO = lambda x: x.max(axis=1),
        BASE = lambda x: x.min(axis=1)).drop(columns = [0,1])
    
    return {'Detalle de Partes': df_final.reset_index().rename(columns={'index':'Descripcion'}),
            'Resumen de Partes': df_final.value_counts().sort_index().reset_index().rename(columns={0:'CANTIDAD'})}



base = 1600
#altura = 340
altura = 560
ancho = 600
grosor = 18
n_columnas = 2
n_filas = 2


aux1 = mueble_cajonera(base = 1700, altura = 340, ancho = 600, grosor = 18, n_columnas = 2, n_filas = 1, is_cajon= False)
aux2 = mueble_cajonera(base = 1700, altura = 1050, ancho = 600, grosor = 18, n_columnas = 2, n_filas = 1, is_cajon= False)
aux3 = mueble_cajonera(base = 1700, altura = 250, ancho = 600, grosor = 18, n_columnas = 3, n_filas = 1, is_cajon= True)
aux4 = mueble_cajonera(base = 1700, altura = 580, ancho = 600, grosor = 18, n_columnas = 2, n_filas = 2, is_cajon= True, base_soporte = 50)


p_final = pd.concat([aux1['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p1'),
                     aux2['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p2'),
                     aux3['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p3'),
                     aux4['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p4')])

q_final = pd.concat([aux1['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q1'),
                     aux2['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q2'),
                     aux3['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q3'),
                     aux4['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q4')])



aux1 = mueble_cajonera(base = 1700, altura = 340, ancho = 600, grosor = 18, n_columnas = 2, n_filas = 1, is_cajon= False)
aux2 = mueble_cajonera(base = 1700, altura = 1050, ancho = 600, grosor = 18, n_columnas = 2, n_filas = 1, is_cajon= False)
aux3 = mueble_cajonera(base = 1700, altura = 830, ancho = 600, grosor = 18, n_columnas = 3, n_filas = 3, is_cajon= True, base_soporte = 50)


p_final = pd.concat([aux1['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p1'),
                     aux2['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p2'),
                     aux3['Detalle de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'p3')])

q_final = pd.concat([aux1['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q1'),
                     aux2['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q2'),
                     aux3['Resumen de Partes'].reset_index().rename(columns={'index':'Parte'}).assign(Parte = 'q3')])


















