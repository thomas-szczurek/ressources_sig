# -*- coding:utf8 -*-

# Script permettrant de renvoyer l'intersection d'un dossier de couches
# dans un périmètre donnée, ou un buffer autours de ce dernier
# Les données sont d'entrée/sortie sont au format FlatGeoBuf

# la couche de périmètre doit se trouver dans le dossier de la variable dir,
# lui comprenant même comprenant un dossier "donnees" contenant les couches.
# a intersecter. Un dossier "output" sera créé dans dir pour la sortie.

import os
import pandas as pd
import geopandas as gpd

# Définition du dossier de travail

dir = r''
os.chdir(dir)

# Couche de périmètre

perim = gpd.read_file('perimetre.fgb')

# Taille buffer en mètres (variable buf)

buf = 0
perim.geometry = perim.buffer(buf)

os.mkdir(dir+'\\output\\')
fichiers = [file for file in os.listdir(os.getcwd()+r'\donnees')]
for f in fichiers:
    l = gpd.read_file(os.getcwd()+'\\donnees\\'+f)
    l.geometry = l.intersection(perim.geometry.iloc[0])
    l = l[l.intersects(perim.geometry.iloc[0]) == True]
    l.to_file(os.getcwd()+'\\output\\'+f)
