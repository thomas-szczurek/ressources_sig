
# Ressources SIG
## POSTGRES
Voir dépot ref_postgresql

## WebSig
### Portails
 * [Mapstore](https://www.geosolutionsgroup.com/technologies/mapstore/) Portail WebSIG par Geosolutions
* [mviewer](https://mviewer.netlify.app/fr/) Portail WebSIG proposé par Geobretagne

### Autres solutions WEB
* [Geoserver](https://geoserver.org/) Serveur cartographique
* [GeoNetwork](https://geonetwork-opensource.org/) Gestion de metadonnées
* [GeoNetwork Ui](https://github.com/geonetwork/geonetwork-ui) Refonte graphique de GeoNetwork
* [GeoNode](https://www.geosolutionsgroup.com/technologies/geonode/) IDG complète par Geosolutions

### Serveurs de tuile
* [trex](https://t-rex.tileserver.ch/) Serveur de tuiles vectorielles
* [tilemaker](https://github.com/systemed/tilemaker/) Génération de tuiles vectorielles à partir d'OSM

### Projets Qgis sur le Web
* [Lizmap](https://www.lizmap.com/)
* [G3W-Suite](https://g3wsuite.it/en/g3w-suite-publish-qgis-projects/)

## Base de données

### SGBDR :
* [Postgresql](https://www.postgresql.org/) coeuravélesdoigts. A partir du moment où on connait l'existance de Postgres, aucun intérêt de présenter les autres sgbdr en mode serveur, ils n'en ont aucun.
* [SQlite](https://www.sqlite.org/index.html) SGBDR embarqué dans un fichier, non en mode serveur
* [Duckdb](https://duckdb.org) Nouvelle aternative à SQLite pour système embarqué. Plus orienté analyse (orienté colonnes, fonctionalités modernes avec pîvots directs...), mais ne gère pas certaines choses en "oltp" (cascade...). Leur spatial est au 15/01/2024 encore trop limité (pas d'index spatial...).

### Outils :
#### Gestionnaires
* [Dbeaver](https://dbeaver.io/) Gestionnaire universel
* [DataGrip](https://www.jetbrains.com/fr-fr/datagrip/) Autre gestionnaire universel, payant

#### Autres
* [SqliteTools](https://www.sqlite.org/download.html) Bundle d'outils en ligne de commande pour Sqlite : shell, sqldiff et sql analizer (permet d'analyser une base existante)

### Plate-forme Nocode :
* [Nocodb](https://nocodb.com/) Plate forme de création de base de données en nocode, peut se brancher sur une base Postgres déjà existante

### Applications externes :
* [SQLPage](https://sql.ophir.dev/) Client d'application générant des pages web à partir de requêtes sql

## Python

### Livres
* [Geocomputation with Python](https://py.geocompx.org/) Apprendre la géomatique avec Python (axé Geopandas et Rasterio)

### IDE
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) IDE généraliste
* [Spyder](https://www.spyder-ide.org/) IDE orientée DataScience

### Frameworks
* [Django](https://www.djangoproject.com/)/[GeoDjango](https://docs.djangoproject.com/fr/5.0/ref/contrib/gis/) Puissant mais complexe
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) Reconnu pour être adapté aux matériels embarqués
* [Shiny for Python](https://shiny.posit.co/py/) RShiny, pour Python. Création de pages web, "simple".

### Bibliothèques
* [Numpy](https://numpy.org/)/[MatPlotlib](https://matplotlib.org/)/[pandas](https://pandas.pydata.org/) Classiques de la datascience
* [xarray](https://docs.xarray.dev/en/stable/) Alternative à Numpy à la mode gérant les arrays muti-dimentionnels
* [Geopandas](https://geopandas.org/en/stable/) DataAnalyse géospatiale vectorielle. Dépendances [Shapely](https://shapely.readthedocs.io/en/stable/) (manipulation d'objets géométriques) et [Fiona](https://pypi.org/project/fiona/) (ogr pythonesque)
* [MovingPandas](https://movingpandas.org/) Librairie pour l'analyse des mouvements et des trajectoires sur un réseau
* [Seaborn](https://seaborn.pydata.org/) Surcouche de matplotlib simplifiant la création de graphiques
* [Rasterio](https://rasterio.readthedocs.io/en/stable/) Accès à aux données géospatiales raster
* [Requests](https://pypi.org/project/requests/) Librairie http simple et élégante
* [Levenstein](https://pypi.org/project/python-Levenshtein/) Permet de calculer la distance entre deux chaines de caractères
* [Sqlite3](https://docs.python.org/3/library/sqlite3.html) Interface pour bdd Sqlite
* [Duckbd](https://duckdb.org/#quickinstall) Interface pour bdd DuckDb
* [Psycopg](https://www.psycopg.org/) Interface pour bdd PostGres
* [Pillow](https://pypi.org/project/pillow/) Manipulation d'images, fork de PIL
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) Moteur de templates
* [Pandoc](https://pandoc.org/) Conversion entre formats de languages à balises (markdown, html, epub ...). Necessite d'installer le logiciel avant d'appeler son API python.
* [Jupyter](https://jupyter.org/) Systèmes de notebooks
    * [Jupysql](https://jupysql.ploomber.io/en/latest/quick-start.html) Intégration du sql aux notebooks Jupyter 
* [Quarto](https://quarto.org/index.html) système de publication à partir de markdown ou de notebooks Jupyter

## QGIS
### Plugins
* [Autofiltre] Permet de filtrer la couche active avec les objets sélectionnés
* [Bezier editing] dessiner du vecteur en utilisant des courbes de bezier (à la Inkspace/Illustrator)
* [cadastre] accès aux données du cadastre
* [ChangeDataSource] changer la source des données d’une/plusieurs couches de façon aisée
* [CustomToolBar] Création de barres d’outils personnalisées
* [Dataplotly] Création de graphiques dans Qgis à partir des données d’une couche
* [Dimensioning] Pour dessiner facilement des lignes de côtes
* [geometric attributes table] Permet de voir les attributs géométriques des entités vectorielles et notamment de sélectionner les entités multipart ou vides. Ne se trouve plus dans le dépôt officiel...
* [ICEtool] Calculs d’îlots de Chaleur (dépend de UMEP, voir plus bas)
* [LayerBoard] visualiser et modifier les propriétés de couches vecteur ou raster dans une table
* [mask] Création de masques
* [menu_from_project] ajout de barres de menus permettant l’ajout de couches d’un projet (pratique pour configurer un qgis pour utilisateur non averti)
* [multipart split] Permet de corriger/séparer les entités multipart qui peuvent provoquer des erreurs de traitement
* [multiple_layers_tools] outils pour travailler sur plusieurs couches en même temps
* [MultipleLayerSelection] sélection dans plusieurs couches
* [nettoyeur] nettoyeur de couches (dépôt du ministère du DD)
* [NNJoin] calculs de plus proches voisins de points à points
* [OrfeoToolBox Provider] Ajout des algorithmes d’OrfeoToolBox à Qgis (logiciel de télédétection de l’Agence Spatiale Européenne), ce plugin est intégré par défaut à Qgis
* [pg_metadata] gestion de métadonnées dans qgis à partir d'une base Postgres
* [processing_r] ajouter des scripts en R aux processus de traitement
* [processing_saga_nextgen] ajout des algorithmes de SAGA aux processus de traitement. Gère SAGA 9.x
* [qad] Le plugin qui offre les outils d'autocad à QGIS
* [qfieldsync] synchronisation de plusieurs qfield/qgis grace aux services cloud
* [qgis hub plugin] Accès aux ressources du hub communautaire Qgis
* [qgis_resource_sharing] mise en commun de ressources (sympboles, mais aussi modèles, scripts R…)
* [QNEAT3] puissant outil de calcul d’itinéraires (matrices de distances etc.)
* [QompliGIS] Validation de données à partir d’un modèle
* [quick_map_services] accès à plusieurs fonds de cartes WMS (OSM, ESRI, NASA…)
* [QuickOSM] Récupérer facilement de la donnée OSM
* [SemiAutomaticClassificationPlugin) Logiciel de télédétection complet
* [SpreadsheetLayers] import des xls/xlsx dans qgis
* [UMEP] multiple analyses urbaines
* [valuetool] ajoute un panneau pour visualiser les valeurs d’un raster au survol souris
* [VectorBender] permet de géoréférencer du vecteur
* [ViewshedAnalysis] outil d’analyse de visibilité
* [wbt_for_qgis] ajout des algorithmes de WhiteBoxTool aux processus de traitement

### Autre
* [Dépot générateur de géométrie](https://gitlab.com/GIS-projects/qgis-geometry-generator-examples) Un déport compremant de nombreux examples d'utilisation du générateur de géométrie
* [Dépot d'expressions Qgis](https://github.com/geographyclub/qgis-expressions) Un dépot comprenant de nombreuses expressions Qgis prêtes à l'emploi

## Ressources Web
### Podcasts :
* [mapscaping](https://mapscaping.com/podcasts/) Podcast en anglais autour de la géomatique et de la cartographie
* [Postgres FM](https://postgres.fm/) podcast en anglais spécialisé sur Postgres

### Blogs
* [Paul Ramsay blog](http://blog.cleverelephant.ca/)Blog d'un des créateurs de Postgis

### Sites
* [Site d'Anita Graser](https://anitagraser.com/) réflexions et tutos SIG orientés python
