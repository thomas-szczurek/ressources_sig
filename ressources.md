
# Ressources SIG
## POSTGRES
Voir dépot [ref_postgresql](https://github.com/Jean-Roc/ref_postgresql/blob/main/references.md)

## WebSig
### Portails
 * [Mapstore](https://www.geosolutionsgroup.com/technologies/mapstore/) Portail WebSIG par Geosolutions
* [mviewer](https://mviewer.netlify.app/fr/) Portail WebSIG proposé par Geobretagne
* [Mapbender](https://mapbender.org/en/) Portail WebSiG 

### Autres solutions WEB
* [Geoserver](https://geoserver.org/) Serveur cartographique
* [Leaflet](https://leafletjs.com/) Librairie JavaScript de Webmapping
* [Maplibre](https://maplibre.org/) Librairie JavaScript de Webmapping
* [GeoNetwork](https://geonetwork-opensource.org/) Gestion de metadonnées
* [GeoNetwork Ui](https://github.com/geonetwork/geonetwork-ui) Refonte graphique de GeoNetwork
* [GeOrchestra](https://www.georchestra.org/fr/) IDG, complète créée pour répondre à INSPIRE
* [GeoNode](https://www.geosolutionsgroup.com/technologies/geonode/) IDG complète par Geosolutions

### Serveurs de tuile
* [trex](https://t-rex.tileserver.ch/) Serveur de tuiles vectorielles
* [tilemaker](https://github.com/systemed/tilemaker/) Génération de tuiles vectorielles à partir d'OSM

### Projets Qgis sur le Web
* [Lizmap](https://www.lizmap.com/)
* [G3W-Suite](https://g3wsuite.it/en/g3w-suite-publish-qgis-projects/)

### Projets Qgis en applications mobiles
* [Qfield](https://qfield.org/) transforme un projet qgis en application mobile collaborative (partenaire fr : oslandia)
* [Mergin Maps](https://fr.merginmaps.com/) transforme un projet qgis en application mobile collaborative (partenaire fr : camptocamp)

### Storymaps
* [Storymap js](https://storymap.knightlab.com/) Création de story maps.

## Point Cloud / Lidar
* [pdal](https://pdal.io/en/2.6.3/) Le gdal des nuages de points
* [pdal-parallelizer](https://pypi.org/project/pdal-parallelizer/) Parallélisation de processing pdal
* [Cloudcompare](https://www.cloudcompare.org/main.html) Logiciel de visualisation et traitements de nuages de points

## Base de données

### SGBDR :
* [Postgresql](https://www.postgresql.org/) coeuravélesdoigts. A partir du moment où on connait l'existance de Postgres, aucun intérêt de présenter les autres sgbdr en mode serveur, ils n'en ont aucun.
* [SQlite](https://www.sqlite.org/index.html) SGBDR embarqué dans un fichier, non en mode serveur
* [Duckdb](https://duckdb.org) Nouvelle aternative à SQLite pour système embarqué. Plus orienté analyse (orienté colonnes, fonctionalités modernes avec pîvots directs...), mais ne gère pas certaines choses en "oltp" (cascade...). Leur spatial est au 15/01/2024 encore trop limité (pas d'index spatial...).

### Outils :
#### Gestionnaires
* [Dbeaver](https://dbeaver.io/) Gestionnaire universel, community edition

#### Modélisateurs
* [Pgmodeler](https://pgmodeler.io/) Modélisateur dédié à Postgresql
* [Looping](https://www.looping-mcd.fr/) Modelisation de modèle Entité Relation, UMP

#### Autres
* [Supabase](https://supabase.com) Déployer et gérer une instance PostgreSQL cloud via une GUI 
* [SqliteTools](https://www.sqlite.org/download.html) Bundle d'outils en ligne de commande pour Sqlite : shell, sqldiff et sql analizer (permet d'analyser une base existante)

### bdd orientée Graphs
* [Neo4j](https://neo4j.com/) Versio ncommunautaire

### Applications externes :
* [SQLPage](https://sql.ophir.dev/) Client d'application générant des pages web à partir de requêtes sql

## Plate-formes data ("data fabric", CDC ...)

### ETL
* [Singer](https://www.singer.io/) Complètement Open Source
* [Pentaho](https://www.hitachivantara.com/en-us/products/pentaho-plus-platform/data-integration-analytics/pentaho-community-edition.html) Community edition

### Message Broker / Jobs et Workflow
* [Apache Kafka](https://kafka.apache.org/) Gestion de souscrptions / publications d'évènements
* [Apache Airflow](https://airflow.apache.org/) Concevoir et planifier des workflows / jobs

### Data pipelines
* [Meltano](https://meltano.com/) Création de data pipelines

### Query engine / Data Fabric
* [Prestodb](https://prestodb.io/) query engine
* [Dbt](https://www.getdbt.com/product/what-is-dbt) query engine
* [trino](https://trino.io/) query engine
* [Apache Spark](https://spark.apache.org/) Data Fabric

### Dashboards
* [Observablehq](https://observablehq.com/) Création de "datappa" avec Dahsboards, rapports...
* [Apache Superset](https://superset.apache.org/) plateforme de d'eploration et de visualisation de données
* [redash](https://github.com/getredash/redash) Fait aussi un peu de CDC
* [Grafana](https://grafana.com/) Dashboard, rapports..., peut se brancher sur une base Postgres déjà existante

### Consultation en mode "tableau" :
* [Nocodb](https://nocodb.com/) Plate forme de création d'interface de données en nocode, peut se brancher sur une base Postgres déjà existante

## Traitement image (sattelitaire, segmentation...)
* [OrfeoToolBox](https://www.orfeo-toolbox.org/) Processing d'imagerie sattelitaire / Téldétection

### segmentation sémantique
* [Immarkus](https://github.com/rsimon/immarkus/wiki)

## Hors SIG
* [ParquetViewer](https://github.com/mukunku/ParquetViewer/releases/) Visualisateur de fichier Parquet
* [ConEmu](https://conemu.github.io/) Terminal avancé pour Windows

### Reseau
* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) Client telnet / client SSH (tunnel SSH, permet de rerouter un port d'écoute...)

## Python

### IDE
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) IDE généraliste, community edition
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
* [Pypdf](https://pypi.org/project/pypdf/)/[Repotlab toolkit](https://www.reportlab.com/software/opensource/rl-toolkit/download/) Edition de pdf
* [Pillow](https://pypi.org/project/pillow/) Manipulation d'images, fork de PIL
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) Moteur de templates
* [Pandoc](https://pandoc.org/) Conversion entre formats de languages à balises (markdown, html, epub ...). Necessite d'installer le logiciel avant d'appeler son API python.
* [Jupyter](https://jupyter.org/) Systèmes de notebooks
    * [Jupysql](https://jupysql.ploomber.io/en/latest/quick-start.html) Intégration du sql aux notebooks Jupyter 
    * [Leafmap](https://leafmap.org/) package python pour l'aaalyse spatiale et la cartographie interactive dans des notebooks Jupyter
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
* [Project Full Text Search] Du FTS (Full Text Saerch) dans les couches et attributs d'un projet Qgis
* [qad] Le plugin qui offre les outils d'autocad à QGIS
* [qfieldsync] synchronisation de plusieurs qfield/qgis grace aux services cloud
* [qgis2web] générer une page web à partir d'un projet qgis
* [qgis hub plugin] Accès aux ressources du hub communautaire Qgis
* [qgis_resource_sharing] mise en commun de ressources (sympboles, mais aussi modèles, scripts R…)
* [QNEAT3] puissant outil de calcul d’itinéraires (matrices de distances etc.)
* [QompliGIS] Validation de données à partir d’un modèle
* [quick_map_services] accès à plusieurs fonds de cartes WMS (OSM, ESRI, NASA…)
* [QuickOSM] Récupérer facilement de la donnée OSM
* [togle_label_visibility] activer/desactiver l'affichage des étiquettes simplement
* [SemiAutomaticClassificationPlugin] Logiciel de télédétection complet
* [SpreadsheetLayers] import des xls/xlsx dans qgis
* [UMEP] multiple analyses urbaines
* [valuetool] ajoute un panneau pour visualiser les valeurs d’un raster au survol souris
* [VectorBender] permet de géoréférencer du vecteur
* [ViewshedAnalysis] outil d’analyse de visibilité
* [wbt_for_qgis] ajout des algorithmes de WhiteBoxTool aux processus de traitement. Necessite l'installation de White Box Tools open core.

### Autre
* [Dépot générateur de géométrie](https://gitlab.com/GIS-projects/qgis-geometry-generator-examples) Un déport compremant de nombreux examples d'utilisation du générateur de géométrie
* [Dépot d'expressions Qgis](https://github.com/geographyclub/qgis-expressions) Un dépot comprenant de nombreuses expressions Qgis prêtes à l'emploi

## Ressources Web
### Podcasts :
* [mapscaping](https://mapscaping.com/podcasts/) Podcast en anglais autour de la géomatique et de la cartographie
* [Postgres FM](https://postgres.fm/) podcast en anglais spécialisé sur Postgres

### Blogs
* [Paul Ramsay blog](http://blog.cleverelephant.ca/) Blog d'un des créateurs de Postgis
* [Crunchy data](https://www.crunchydata.com/blog) Blog d'une entreprise spécialisé sur Postgres. Enormement de conseils et de bonnes pratiques, avec sql de haut niveau
* [EverSQL](https://www.eversql.com/blog/) SQL et BDD généraliste, mais beaucoup de Postgres
 
### Sites
* [Site d'Anita Graser](https://anitagraser.com/) réflexions et tutos SIG orientés python
* [Planet PostgreSQL](https://planet.postgresql.org/) Agrégateur sur PostgreSQL

### Livres
* [Computational modelling of terrains](https://tudelft3d.github.io/terrainbook/) Modélisation de la représentation numérique du terrain
* [Geocomputation with Python](https://py.geocompx.org/) Apprendre la géomatique avec Python (axé Geopandas et Rasterio)

### Dépots git
* [Sources données Fr](https://github.com/ljegou/geotests/blob/master/sources_donnees.md) Dépôt de L Jegou recensant un grand nombre de sources open data sur divers thématiques
* [Université d'été Dataviz](https://datagistips.github.io/universite-ete-dataviz/) histoire, tutoriels, bonne pratiques, exemples...