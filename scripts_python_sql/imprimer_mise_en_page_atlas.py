# -*- coding:Utf8 -*-

# Ce script exporte en pdf un atlas pré configuré. Peut être utile dans une Actions Qgis, pour éviter de présenter le composeurs à des utilisateurs "simples"

# Nécessite qu'un Atlas soit au préalable configuré sur la mise en page appelée en paramètre de la fonction, comme en ligne 

from datetime import datetime
import os
from PyQt5.QtWidgets import QFileDialog

def print_atlas(nom_atlas);
    uri = QFileDialog.getSaveFileName(None, u"Sauvegarder le pdf ", u"export", '*.pdf')[0][:-4]
    try:
        os.startfile(uri[0:uri.rfind('/')])
    except:
        print('Veuillez sélectionner un fichier')
    uri = uri[0][:-4]
    project = QgsProject.instance()
    dt = datetime.now().strftime('%Y-%m-%d-%Hh%Mmin%Ssec')
    manager = QgsProject.instance().layoutManager()
    layout = manager.layoutByName(nom_atlas)
    exporter = QgsLayoutExporter(layout)
    exporter.exportToPdf(layout.atlas(),r'uri'+'-'+dt+'.pdf', QgsLayoutExporter.PdfExportSettings())
    os.startfile(uri[0:uri.rfind('/')])
    return

nom_atlas = "MeP_A3_Paysage"
print_atlas(nom_atlas)