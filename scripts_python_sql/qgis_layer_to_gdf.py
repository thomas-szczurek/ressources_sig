# -*- coding:Utf8 -*-

# Fonctions permettant de charger une couche qgis comme Geodataframe dans l'interpreteur de Qgis et inversement

import pandas as pd
import geopandas as gpd

def layer_to_gdf(layer_name, crs):
    # PyQgisation de la couche
    vlayer = QgsProject.instance().mapLayersByName(layer_name)[0]
    # Génération de la dataframe d'attribus
    cols = [f.name() for f in vlayer.fields()]
    datagen = ([f[col] for col in cols] for f in vlayer.getFeatures())
    df = pd.DataFrame.from_records(data=datagen, columns=cols)
    for col in df.columns:
        if (str(type(df.loc[0,col])) == "<class 'PyQt5.QtCore.QDateTime'>") == True:
            df[[col]] = df[[col]].astype('str')
    # Génération de la GeoSerie
    gs = gpd.GeoSeries.from_wkt([feature.geometry().asWkt() for feature in vlayer.getFeatures()])
    # Génération de la Geodataframe
    gdf = gpd.GeoDataFrame(df, geometry=gs, crs=crs)
    return gdf

def gdf_to_layer(gdf_name):
    vlayer = QgsVectorLayer(gdf_name.to_json(),"test","ogr")
    QgsProject.instance().addMapLayer(vlayer)
    return vlayer

# Nom de la couche à geopandaiser
layer_name = 'surface_z13'
# srid de la projection de la couche
crs = 2154
my_gdf = layer_to_gdf(layer_name, crs)
gdf_to_layer(gdf_name)
