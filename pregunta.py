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
    index = 0
    while index < len(data):
        if data[index] != '':
            cadena += ' ' + data[index]
        else:
            lista.append(cadena)
            cadena = ''
        index +=1


    lista = [line.strip() for line in lista]   #quitar espacios

    info = []
    for index in lista:
        regular = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', index)
        linea = regular.group(1) + '*' + regular.group(2) + '*' + regular.group(3) + '.' + regular.group(5) + '*' + regular.group(7)
        info.append(linea)
    datos = [line.split('*') for line in info]
    df = pd.DataFrame(columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    #df = pd.DataFrame(columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    #convertir lista de listas a df
    index = 0
    while index < 4:
        df[list(df.columns)[index]] = [element[index] for element in datos]  #asignar a cada titulo una columna
        index +=1
        
     #df = pd.DataFrame(df)
    
     df["principales_palabras_clave"] = [line.replace('   ', ' ') for line in df["principales_palabras_clave"]]
     df["principales_palabras_clave"] = [line.replace('  ', ' ') for line in df["principales_palabras_clave"]]
     df["principales_palabras_clave"] = [line.replace('.', ' ') for line in df["principales_palabras_clave"]]
        
    #[line.replace('   ', ' ') for line in principales_palabras_clave]
    
     df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype('float')
    
    return df
