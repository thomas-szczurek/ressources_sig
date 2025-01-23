# -*- coding:Utf8 -*-

# Ce script exporte une mise en page en fixant l'étendue de la carte principale de cette dernière sur celle du canevas de carte courant.
# Peut être utile dans une Actions Qgis, pour éviter de présenter le composeurs à des utilisateurs "simples".

# Nécessite d'avoir une mise en page de constituée dans le composeur ici appellée "MeP_A3_Paysage_Rouge", a remplacer par la votre dans le paramètre de la fonction, comme en ligne 27

from datetime import datetime
from qgis.utils import iface
import os
from PyQt5.QtWidgets import QFileDialog

def print_mep(nom_mep)
    uri = QFileDialog.getSaveFileName(None, u'Sauvegarder le pdf', u'export', '*.pdf')[0][:-4]
    try:
        os.startfile(uri[0:uri.rfind('/')])
    except:
        print('Veuillez sélectionner un fichier')
    project = QgsProject.instance()
    dt = datetime.now().strftime('%Y-%m-%d-%Hh%Mmin%Ssec')
    manager = QgsProject.instance().layoutManager()
    layout = manager.layoutByName(nom_mep)
    map = layout.referenceMap()
    map.zoomToExtent(iface.mapCanvas().extent())
    exporter = QgsLayoutExporter(layout)
    exporter.exportToPdf(uri+'-'+dt+'.pdf', QgsLayoutExporter.PdfExportSettings())
    os.startfile(uri[0:uri.rfind('/')])
    return

nom_mep = "MeP_A3_Paysage"
print_mep(nom_mep)