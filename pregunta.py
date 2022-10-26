"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re 


def ingest_data():

    #
    # Inserte su código aquí
    #
   
    

    ### llamar base de datos
    #def load_file(url):
    with open("clusters_report.txt") as file:
      data = file.readlines()
    
    data = data[4:]  ## seleccionar sin titulos
    data = [line.replace("\n","") for line in data]   #organizar espacios y cambios de linea
    data = [line.strip() for line in data]
    lista = []
    
    cadena = ''
    indice = 0
    #ciclo para andar renglon por renglon
    while index < len(data):
        if data[indice] != '':
            cadena += ' ' + data[indice]
        else:
            lista.append(cadena)
            cadena = ''
        indice +=1


    lista = [line.strip() for line in lista]   #quitar espacios

    info = []
    for index in lista:
        regular = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', index)
        linea = regular.group(1) + '*' + regular.group(2) + '*' + regular.group(3) + '.' + regular.group(5) + '*' + regular.group(7)
        info.append(linea)
    datos = [line.split('*') for line in info]
    #nombre de columnas
    df = pd.DataFrame(columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    #convertir lista de listas a df
    index = 0
    while index < 4:
        df[list(df.columns)[index]] = [element[index] for element in datos]  #asignar a cada titulo una columna
        index +=1
        
     #df = pd.DataFrame(df)
    
    palabras = [line[3].replace('    ', ' ') for line in datos]
    palabras = [line.replace('   ', ' ') for line in palabras]
    palabras = [line.replace('  ', ' ') for line in palabras]
    palabras = [line.replace('.', '') for line in palabras]
    palabras = [line.split(',') for line in palabras]
    palabras = [[element.strip() for element in line] for line in palabras]
    palabras = [', '.join(line) for line in palabras]
    
    
    df.principales_palabras_clave = palabras
    df.cluster = df.cluster.astype('int')  #volver el numero entero
    df.cantidad_de_palabras_clave = df.cantidad_de_palabras_clave.astype('int') #volver entero
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.astype('float')
        
    return df
