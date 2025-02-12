
# Ressources SIG
## POSTGRES
Voir dépot [ref_postgresql](https://github.com/Jean-Roc/ref_postgresql/blob/main/references.md)

## WebSig
### Portails
* [Mapstore](https://www.geosolutionsgroup.com/technologies/mapstore/) Portail WebSIG par Geosolutions
* [mviewer](https://mviewer.netlify.app/fr/) Portail WebSIG proposé par Geobretagne
* [Mapbender](https://mapbender.org/en/) Portail WebSiG 

### Serveurs spatiaux
* [Geoserver](https://geoserver.org/) Serveur cartographique
* [Qgis serveur](https://docs.qgis.org/3.34/en/docs/server_manual/index.html) Serveur cartographique se basant sur Qgis
* [BBOX](https://www.bbox.earth/installation.html) Server OGC API modulaire complet en Rust. [Voir](https://kalberer.org/pirmin/blog/bbox-0-5-0-release/) (Features, Maps, Tiles, Process...)
* [trex](https://t-rex.tileserver.ch/) Serveur de tuiles vectorielles (porbablement supplanté par BBOX du même créateur)

### IDG
* [GeOrchestra](https://www.georchestra.org/fr/) IDG, complète créée pour répondre à INSPIRE
* [GeoNode](https://www.geosolutionsgroup.com/technologies/geonode/) IDG complète par Geosolutions

### Autres solutions WEB

* [Leaflet](https://leafletjs.com/) Librairie JavaScript de Webmapping
* [Maplibre](https://maplibre.org/) Librairie JavaScript de Webmapping
* [GeoNetwork](https://geonetwork-opensource.org/) Gestion de metadonnées
* [GeoNetwork Ui](https://github.com/geonetwork/geonetwork-ui) Refonte graphique de GeoNetwork
* [tilemaker](https://github.com/systemed/tilemaker/) Génération de tuiles vectorielles à partir d'OSM

### Projets Qgis sur le Web
* [Lizmap](https://www.lizmap.com/)
* [G3W-Suite](https://g3wsuite.it/en/g3w-suite-publish-qgis-projects/)
* [QWC](https://github.com/qgis/qwc2) Qgis Web Client, fait pour fonctionner avec qgis serveur.

### Projets Qgis en applications mobiles
* [Qfield](https://qfield.org/) transforme un projet qgis en application mobile collaborative (partenaire fr : oslandia)
* [Mergin Maps](https://fr.merginmaps.com/) transforme un projet qgis en application mobile collaborative (partenaire fr : camptocamp)

### Storymaps
* [Storymap js](https://storymap.knightlab.com/) Création de story maps.

## Base de données

### SGBDR :
* [Postgresql](https://www.postgresql.org/) coeuravélesdoigts. A partir du moment où on connait l'existance de Postgres, aucun intérêt de présenter les autres sgbdr en mode serveur, ils n'en ont aucun.
* [SQlite](https://www.sqlite.org/index.html) SGBDR embarqué dans un fichier, non en mode serveur
* [Duckdb](https://duckdb.org) Nouvelle aternative à SQLite pour système embarqué. Plus orienté analyse (orienté colonnes, fonctionalités modernes avec pîvots directs...) et permet d'attaquer des sources externes très diverses, mais ne gère pas certaines choses en "oltp" (cascade...). Leur spatial commence a être viable au 30/10/2024.

### Outils :
#### Gestionnaires
* [Dbeaver](https://dbeaver.io/) Gestionnaire universel, community edition

#### Modélisateurs
* [Pgmodeler](https://pgmodeler.io/) Modélisateur dédié à Postgresql
* [Looping](https://www.looping-mcd.fr/) Modelisation de modèle Entité Relation, UML

#### Autres
* [Supabase](https://supabase.com) Déployer et gérer une instance PostgreSQL cloud via une GUI 
* [SqliteTools](https://www.sqlite.org/download.html) Bundle d'outils en ligne de commande pour Sqlite : shell, sqldiff et sql analizer (permet d'analyser une base existante)

### bdd orientée Graphs
* [Neo4j](https://neo4j.com/) Versio ncommunautaire

### Applications externes :
* [SQLPage](https://sql.ophir.dev/) Client d'application générant des pages web à partir de requêtes sql

## Plate-formes data

### ETL
* [Singer](https://www.singer.io/) Complètement Open Source
* [Pentaho](https://www.hitachivantara.com/en-us/products/pentaho-plus-platform/data-integration-analytics/pentaho-community-edition.html) Community edition

### Dashboards
* [Observablehq](https://observablehq.com/) Création de "datappa" avec Dahsboards, rapports...
* [Apache Superset](https://superset.apache.org/) plateforme de d'eploration et de visualisation de données
* [redash](https://github.com/getredash/redash) Fait aussi un peu de CDC
* [Grafana](https://grafana.com/) Dashboard, rapports..., peut se brancher sur une base Postgres déjà existante

### Consultation en mode "tableau" :
* [Nocodb](https://nocodb.com/) Plate forme de création d'interface de données en nocode, peut se brancher sur une base Postgres déjà existante

## 3D / Point Cloud / Lidar
* [assimp](https://assimp.org/) Le gdal de la 3d
* [pdal](https://pdal.io/en/2.6.3/) Le gdal des nuages de points
* [Geogram](https://github.com/BrunoLevy/geogram/wiki) librairie de traitements géométriques, de mesh...
* [pdal-parallelizer](https://pypi.org/project/pdal-parallelizer/) Parallélisation de processing pdal
* [Cloudcompare](https://www.cloudcompare.org/main.html) Logiciel de visualisation et traitements de nuages de points
* [Tyler](https://github.com/3DGI/tyler) Créer des 3d tiles à partir de Cityjson
* [CityForge](https://oslandia.com/2024/03/19/citybuilder-faciliter-la-reconstruction-3d/) (et son plugin Qgis) Générer du Cityjson
* [Piero](https://oslandia.com/2024/03/14/piero-lapplication-web-3d-sig-bim-open-source/) Appli web de visualiation 3d (Point Cloud, Cityjson ...)
* [Cityjon2Gltf](https://github.com/tudelft3d/CityJSON2glTF) Convertir du Cityjson en gltf
* [CityjonsIO](https://github.com/cityjson/cjio) CLI Python pour manipuler du Cityjson
* [cjdb](https://github.com/cityjson/cjdb) CityJson to Postgresql
* [Py3dtiles](https://gitlab.com/py3dtiles/py3dtiles/) CLI python pour manipuler des 3dtiles

## Traitement image (teledec, segmentation...)
* [TerrSt LiberaGIS](https://github.com/ClarkCGA/terrset) Logiciel de télédec. Anciennement Idrissi passé libre
* [OrfeoToolBox](https://www.orfeo-toolbox.org/) Processing d'imagerie sattelitaire / Téldétection
* [Upscayl](https://www.upscayl.org/) Permet d'augmenter la résolution d'une image
* [Immarkus](https://github.com/rsimon/immarkus/wiki) Segmentation sémentique
* [samgeo](https://github.com/opengeos/segment-geospatial/) segment anything sur du spatial

## Hors SIG
* [tad](https://tadviewer.com) Visualisateur de fichier parquet, avec possibilité de pivots, d'aggrégats...
* [ParquetViewer](https://github.com/mukunku/ParquetViewer/releases/) Visualisateur de fichiers parquet simple
* [ConEmu](https://conemu.github.io/) Terminal avancé pour Windows
* [Zeal](https://zealdocs.org/) Lecteur de documentation offline
* [Jq](https://jqlang.github.io/jq/) processeur de json en ligne de commande (slice, transformation...)
* [Kgeotag](https://kgeotag.kde.org/) Geotagger des photos, Linux (KDE frameworks)
* [exiftool](https://exiftool.org/) Geotagger des photos, Windows

### Reseau
* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) Client telnet / client SSH (tunnel SSH, permet de rerouter un port d'écoute...)

## Python

### IDE
* [VSCodium](https://vscodium.com/) VsCode, libre et sans Microsoft
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) IDE généraliste, community edition
* [Spyder](https://www.spyder-ide.org/) IDE orientée DataScience

### Frameworks
* [Django](https://www.djangoproject.com/)/[GeoDjango](https://docs.djangoproject.com/fr/5.0/ref/contrib/gis/) Puissant mais complexe
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) Reconnu pour être adapté aux matériels embarqués
* [Dash](https://dash.plotly.com/) Création d'applications data en python
* [Shiny for Python](https://shiny.posit.co/py/) RShiny, pour Python. Création de pages web, "simple".

### Bibliothèques
* [Numpy](https://numpy.org/)/[MatPlotlib](https://matplotlib.org/)/[pandas](https://pandas.pydata.org/) Classiques de la datascience
* [Scipy](https://scipy.org/) Algotithmes mathématiques scientifiques
* [Scikit-learn](https://scikit-learn.org/stable/) Machine Learning et stats avancées
* [xarray](https://docs.xarray.dev/en/stable/) Alternative à Numpy à la mode gérant les arrays muti-dimentionnels
* [Geopandas](https://geopandas.org/en/stable/) DataAnalyse géospatiale vectorielle. Dépendances [Shapely](https://shapely.readthedocs.io/en/stable/) (manipulation d'objets géométriques) et [Fiona](https://pypi.org/project/fiona/) (ogr pythonesque). [pyogrio](https://pyogrio.readthedocs.io/en/latest/introduction.html) va supplanter Fiona.
* [MovingPandas](https://movingpandas.org/) Librairie pour l'analyse des mouvements et des trajectoires sur un réseau
* [T4gpd](https://t4gpd-docs.readthedocs.io/en/latest/) Bibliothèque complémentaire à GeoPandas ajoutant de nombreuses fonctions d'analyse
* [Pysal](https://pysal.org) Python Spatial Analisys librairy (et ses nombreux modules : esda, mgwr ...)
* [Topojson](https://mattijn.github.io/topojson/) Permet d'encoder et de manipuler des objets topojson (gérant les raltions topologiques)
* A suivre (pas prêt) : [Polar](https://pola.rs/) / [Geopolar](https://geopolars.org/latest/) Pandas / Geopandas écrit en Rust, conçu pour la parallélisation et orienté colonnes.
* [cartogramPy](https://github.com/danlewis85/cartogrampy) Cartogrammes avec Python
* [Seaborn](https://seaborn.pydata.org/) Surcouche de matplotlib simplifiant la création de graphiques
* [Rasterio](https://rasterio.readthedocs.io/en/stable/) Accès à aux données géospatiales raster
* [Rioxarray](https://corteva.github.io/rioxarray/html/rioxarray.html) Alternative à rasterio utilisant xarray
* [Rasterstats](https://pythonhosted.org/rasterstats/) Statistiques sur des rasters
* [Requests](https://pypi.org/project/requests/) Librairie http simple et élégante
* [Dask](https://www.dask.org/) Parrallélisation de workflow Python
* [PyArrow](https://arrow.apache.org/docs/python/index.html) Bindings Python pour Apache Arrow
* [Levenstein](https://pypi.org/project/python-Levenshtein/) Permet de calculer la distance entre deux chaines de caractères
* [Sqlite3](https://docs.python.org/3/library/sqlite3.html) Interface pour bdd Sqlite
* [Duckbd](https://duckdb.org/#quickinstall) Interface pour bdd DuckDb
* [Sqlglot](https://github.com/tobymao/sqlglot) Transpilation de dialectes SQL (Postgres, Oracle, SQLite, Duckdb...)
* [Psycopg](https://www.psycopg.org/) Interface pour bdd PostGres
* [Pypdf](https://pypi.org/project/pypdf/)/[Repotlab toolkit](https://www.reportlab.com/software/opensource/rl-toolkit/download/) Edition de pdf
* [Pillow](https://pypi.org/project/pillow/) Manipulation d'images, fork de PIL
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) Moteur de templates
* [Pandoc](https://pandoc.org/) Conversion entre formats de languages à balises (markdown, html, epub ...). Necessite d'installer le logiciel avant d'appeler son API python.
* [Folium](https://python-visualization.github.io/folium/latest/) Visualiser ses cartes avec leaflet
* [Jupyter](https://jupyter.org/) Systèmes de notebooks
    * [Jupysql](https://jupysql.ploomber.io/en/latest/quick-start.html) Intégration du sql aux notebooks Jupyter 
    * [Leafmap](https://leafmap.org/) package python pour l'analyse spatiale et la cartographie interactive dans des notebooks Jupyter
* [Contextily](https://contextily.readthedocs.io/en/latest/) Permet de récupérer des tuiles vectorielles sur le web pour faire des fonds de plans de cartes MatPlotLib
* [Quarto](https://quarto.org/index.html) système de publication à partir de markdown ou de notebooks Jupyter

## QGIS

### Plugins

#### Ajout de fonctionalités

* [Dataplotly] Création de graphiques dans Qgis à partir des données d’une couche
* [QompliGIS] Validation de données à partir d’un modèle
* [Dataset QA workbench] Outils de validation QA d'une couche
* [SemiAutomaticClassificationPlugin] Logiciel de télédétection complet
* [OrfeoToolBox Provider] Ajout des algorithmes d’OrfeoToolBox à Qgis (logiciel de télédétection de l’Agence Spatiale Européenne), ce plugin est intégré par défaut à Qgis
* [Simple ETL] Un ETL des couches chargées dans qgis
* [pg_metadata] gestion de métadonnées dans qgis à partir d'une base Postgres
* [Layer Metadata Search] Recherche de couche à partir de leurs metadonnées Postgres (peut se coupler à pgmetadata)
* [qgis animation workbench] Création d'animations video à partir de qgis
* [qfieldsync] synchronisation de plusieurs qfield/qgis grace aux services cloud
* [qgis2web] générer une page web à partir d'un projet qgis

#### QoL

* [QGIST Workbench] système de plans de travail pour l'interface de qgis
* [Memory Layer Saver] Permet de sauvegarder les couches virtuelles en mémoire dans un qgz
* [Layer from clipboard] Création de couches attributaires à partir du contenu du presse papier
* [valuetool] ajoute un panneau pour visualiser les valeurs d’un raster au survol souris
* [Map Swipe tool] "masquer" une couche avec un glissement de souris dans le canevas. Utilse pour comparer des données.
* [stats_by_polygon] statistiques d'un raster à partir d'un polygone plus poussées que celles de base et avec graphiques intégrés
* [layer Tree Toggle labels Widget] ajout d'un widget de couches pour afficher ou non ses étiquettes (propriété de la couche -> légende -> Contrôles disponibles)
* [Autofiltre] Permet de filtrer la couche automatiquement active avec les objets sélectionnés
* [DataSourcePanel] Ajout d'un panneau dédié aux sources de données de projet
* [cigeoe_toggle_vertex_visibility] Afficher les vertices de polygones via le panneau liste des couches
  
#### Digitalisation

* [AutoCorrectBorders](https://github.com/OnroerendErfgoed/brdrQ) Permet d'aligner les limites des polygones d'une couche sur celles d'une couche de référence (pas dans les dépots officiels, à récupérer sur le lien)
* [qad] Le plugin qui offre les outils d'autocad à QGIS
* [Bezier editing] dessiner du vecteur en utilisant des courbes de bezier (à la Inkspace/Illustrator)
* [Spline] Travailler avec des Splines (avec un outil lines to spline)
* [Digitizing tools] Ajout de nouveaux outils de digitalisation
* [Dimensioning] Pour dessiner facilement des lignes de côtes
* [geometry shape] Création de formes géométriques simples avec mesures
* [cigeoe_translate_to_fit_to_adjacent_polygon] Auto translate d'un polygone pour l'accrocher au plus proche
* [cigeoe_reverse_line] inverse le sens de tracé d'une ligne existante

#### Analyse

* [processing_r] ajouter des scripts en R aux processus de traitement
* [processing_saga_nextgen] ajout des algorithmes de SAGA aux processus de traitement. Gère SAGA 9.x
* [LFTools] Divers algorithmes spatiaux (dans la veine de white box tool, 80 % est une copie de trucs existant, 20 % est interessant)
* [wbt_for_qgis] ajout des algorithmes de WhiteBoxTool aux processus de traitement. Necessite l'installation de White Box Tools open core.
* [ProcessX] Outils d'nalyse spatiale
* [Spatial Analyzer] Outils d'analyse spatiale (tendence, dispersion, cluster...)
* [Spatial Analysis Toolbox] Outils d'analyse spatiale Python (dépendances python : pandas, geopandas, libpysal, esda, mgwr)
* [Scipy Filter] Ajout d'algorithmes Scipy
* [NNJoin] calculs de plus proches voisins de points à points
* [Nearest with greater value] Obtenir l'entitée vectorielle la plus proche avec une valeur attributaire définie
* [Nearest neighbor method for linear features] : Nearest neighbor avec des lignes
* [ICEtool] Calculs d’îlots de Chaleur (dépend de UMEP, voir plus bas)
* [UMEP] multiple analyses urbaines
* [QNEAT3] puissant outil de calcul d’itinéraires (matrices de distances etc.)
* [Networks] outils d'analsyse réseau compléntaires de QNEAT3
* [ViewshedAnalysis] outil d’analyse de visibilité

#### Personalisation GUI

* [CustomToolBar] Création de barres d’outils personnalisées
* [Layers menu_from_project] ajout de barres de menus permettant l’ajout de couches d’un projet (pratique pour configurer un qgis pour utilisateur non averti)

#### Cartographie

* [Cartogram3] Création de cartogrammes
* [mask] Création de masques
* [Relief Vizualiazation Toolblox] Ajout de fonctions d'ombrages avancées
* [Terrain shading] Ajout de fonctions d'ombrages avancées
* [Modular Grid] Permet de tracer des lignes d'accroches réfulièrement espacées pour une nouvelle mise en page

#### Jeux de données

* [IDG] accès aux données de la Geoplateforme, de Geo2France, DataGrandEst, GeoBretagne
* [quick_map_services] accès à plusieurs fonds de cartes WMS (OSM, ESRI, NASA…)
* [QuickOSM] Récupérer facilement de la donnée OSM

#### Partage de ressources

* [qgis hub plugin] Accès aux ressources du hub communautaire Qgis
* [qgis_resource_sharing] mise en commun de ressources (sympboles, mais aussi modèles, scripts R…)

#### Autres

* [Project packager] Empaqueter les couches d'un projet et le fichier projet dans un geopackage 
* [VectorBender] permet de géoréférencer du vecteur
* [qtiles] création de mbtiles
* [PyQgis ressource Browser] explorateur des différentes icones utilisables avec pyqgis
* [cadastre] accès aux données du cadastre
* [ChangeDataSource] changer la source des données d’une/plusieurs couches de façon aisée
* [LayerBoard] visualiser et modifier les propriétés de couches vecteur ou raster dans une table
* [multiple_layers_tools] outils pour travailler sur plusieurs couches en même temps
* [MultipleLayerSelection] sélection dans plusieurs couches
* [Project Full Text Search] Du FTS (Full Text Saerch) dans les couches et attributs d'un projet Qgis (**en alpha, à surveiller**)

## Ressources Web

### Podcasts :
* [mapscaping](https://mapscaping.com/podcasts/) Podcast en anglais autour de la géomatique et de la cartographie
* [Postgres FM](https://postgres.fm/) podcast en anglais spécialisé sur Postgres

### Blogs
* [Configuration de paramètres pg](https://stormatics.tech/blogs/key-postgresql-configuration-parameters-for-enhanced-performance)
* [Configuration de paramètres pg2](https://blog.dalibo.com/2024/07/22/lp2.html) Sur le blog Dalibo
* [Paul Ramsay blog](http://blog.cleverelephant.ca/) Blog d'un des créateurs de Postgis
* [Crunchy data](https://www.crunchydata.com/blog) Blog d'une entreprise spécialisé sur Postgres. Enormement de conseils et de bonnes pratiques, avec sql de haut niveau
* [EverSQL](https://www.eversql.com/blog/) SQL et BDD généraliste, mais beaucoup de Postgres
 
### Sites
* [Site d'Anita Graser](https://anitagraser.com/) réflexions et tutos SIG orientés python
* [Planet PostgreSQL](https://planet.postgresql.org/) Agrégateur sur PostgreSQL
* [Planet OSGeo](https://planet.osgeo.org/) Agrégateur géomatique open source

### Livres
* [Computational modelling of terrains](https://tudelft3d.github.io/terrainbook/) Modélisation de la représentation numérique du terrain
* [Théorie des graphs](https://www.imo.universite-paris-saclay.fr/~ruette/mathsdiscretes/polygraph-Sigward.pdf) Introduction a la théorie des grahs par l'Université Paris-Saclay
* [Geocomputation with Python](https://py.geocompx.org/) Apprendre la géomatique avec Python (axé Geopandas et Rasterio)
* [The internals of PostgreSQL](https://www.interdb.jp/pg/) Description complète du fonctionnement interne de postgresql

### Dépots git
* [Dépot Mapbox](https://github.com/mapbox/awesome-vector-tiles#servers) Tout sur les tuiles vectorielles
* [Dépot générateur de géométrie](https://gitlab.com/GIS-projects/qgis-geometry-generator-examples) Un déport compremant de nombreux examples d'utilisation du générateur de géométrie
* [Dépot d'expressions Qgis](https://github.com/geographyclub/qgis-expressions) Un dépot comprenant de nombreuses expressions Qgis prêtes à l'emploi
* [Sources données Fr](https://github.com/ljegou/geotests/blob/master/sources_donnees.md) Dépôt de L Jegou recensant un grand nombre de sources open data sur divers thématiques
* [Université d'été Dataviz](https://datagistips.github.io/universite-ete-dataviz/) histoire, tutoriels, bonne pratiques, exemples...
