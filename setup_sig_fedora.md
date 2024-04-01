# Setup SIG Fedora

On s'interesse ici à une version desktop, pour ce qui va être serveur (qgis-server, geoserver, websig, apache ...) on préférera faire ça sur une machine didiée (et sous Debian)

## Fedora

Bien penser à ajouter l'utilisateur au groupe sudo à l'installation de l'os, sinon :

```bash
sudo adduser user-name sudo
```

### Drivers Nvidia

Ajouter le dép$ot rpmfusion non free :

```bash
# tout d'abord le dépôt libre
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
# puis le dépoît non free
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf update
```

Puis les drivers

```bash
sudo dnf install akmod-nvidia
```

Et on reboot le pc

Tout de suite le gros morceau :

## Postgres / Postgis

### Installation

> Ici Fedora 39, Postgres 16. Retourner sur le sie de [postgres](https://www.postgresql.org/download/linux/redhat/) pour mettre à jour les commandes si versions différentes. Notamment l'adresse du dépôt et la version de Postgres à installer.

On active le dépôt :

```bash
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/F-39-x86_64/pgdg-fedora-repo-latest.noarch.rpm
```

On installe postgres

```bash
sudo dnf install -y postgresql16-server
```

On initialise la base de donnée et on fait démarer le service automatiquement :

```bash
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
sudo systemctl enable postgresql-16
sudo systemctl start postgresql-16
```

En bonus on peut s'installer l'extension Hydra columnar pour la gestion de tables orientées colonnes avec une première compilation depuis les sources facile.

```bash
PATH=/usr/pgsql-16/bin:$PATH # ajout au PATH

# D'abord on installe les dépendances 
sudo dnf install liblzf liblzf-devel libcurl-devel zstd zstd-devel

# installation des entêtes de développement de Postgres
sudo dnf install postgresql16-devel

# on clone le dépôt dans home/user
git clone https://github.com/hydradatabase/hydra.git
```


Avec le terminal on se rend dans le dossier home/user/hydra/columnar puis :
```
./configure
make install USE_PGXS=1
```

Et enfin Postgis et son support Just In Time compilation (JIT).

> Penser à mettre à jour les numéros de version. Ici 34 correspond à Postgis3 3.4 et 16 à Postgres 16.

```bash
sudo dnf install postgis postgis34_16-llvmjit

# On en profite pour s'installer le foreign data wrapper ogr et son support JIT
sudo dnf install ogr_fdw_16 ogr_fdw_16-llvmjit
```


Si on a du courage, on installe le fdw parquet (car contrairement à gdal/ogr, le fdw ogr ne gère pas le parquet).

```bash
# installation des dépendances libarrow et libparquet
sudo dnf install libarrow libarrow-devel parquet-libs

# installation des entêtes de développement de Postgres
sudo dnf install postgresql16-devel
```

On télécharge le [parquet_fdw](https://github.com/adjust/parquet_fdw)

Ouvrir un terminal dans l'archive décompressée, puis :

```bash
PATH=/usr/pgsql-16/bin:$PATH # ajout au PATH
make install
```


### pgAdmin

Désinstaller toute version de pgAdmin préalablement installée par exemple :

```bash
sudo rpm -e pgadmin4-fedora-repo
```

On active le dépôt

```bash
sudo rpm -i https://ftp.postgresql.org/pub/pgadmin/pgadmin4/yum/pgadmin4-fedora-repo-2-1.noarch.rpm
```

Et on installe :

```bash
sudo dnf install pgadmin4-desktop
```

### Configuration

On attribue un mot de passe à l'utilisateur postgres

```bash
sudo -u postgres psql
# Une fois connecté à psql
\password
# attribuer un mot de passe
\q
```

On est fainénant et on fait pas comme les vrais durs en ligne de commande, on va passer par pgAdmin
(mais apprendre psql, c'est bien)

Dans pgadmin :
1) clic droit sur "servers" -> Register -> Server
2) Donner un nom au serveur par exemple "localhost"
3) Dans l'onglet connection, indiquer 127.0.0.1 dans "Host name/address"
4) Dans password indiquer le mot de passe de l'utilisateur postgres préalablement défini
5) Maintenant se rendre sur "Login/Group" qui vient d'apparaitre et créer un groupe/role avec les droits élargis mais non superutilisateur qui sera nontre compte courant.


Maintenant se créer notre base de donnée, on préférera la créer avec notre utilisateur nouvellement créé afin de lui donner tous les droits sur cette base par défaut et se simplifier la vie.
(pour rappel, dans pgAdmin, clic droit sur notre serveur -> properties -> connection -> changer "Username" puis se déconnecter du serveur et se reconnecter, toujours avec un clic droit sur notre serveur "localhost")

Une fois reconnecté avec notre utilisateur, on créé la base :

1) Clic droit sur "Database" -> "Create" -> "Database"
2) lui donner un nom et se rendre dans "définition"
3) Dans "Collation" et "Characer type" selectionner : "fr_FR.UTF-8". Laisser "Tablespace" et "Stategy" (on est en local, activer le WAL est un peu overkill à mon humble avis) vide sauf si bien sur on désire les modifier.
4) Dans sécurity, donner tous les "Privileges" au groupe/role créé

Maintenant se reconnecter avec l'utilisateur postgres pour créer les extensions sur cette base (clic droit sur "localhost" -> properties ...)
Une fois sur notre base, clic droit sur extensions -> create -> extension.
Liste d'extensions obligatoires / interessantes par défaut :

- postgis
- postgis_raster
- postigs_topology
- postgis_sfcgal (fonctions issues de la puissante ilbrairie cgal)
- postgres_fdw (foreign data wrapper sur une autre base postgres)
- file_fdw (foreign data wrapper sur des fichiers plats type csv)
- ogr_fdw (foreign data wrapper utilsant ogr, a condition de l'avoir installé)
- parquet_fdw (si installé)
- columnar (tables orientées colonnes avec hydra, si installé)
- pg_stat_statements (statistiques sur l'utilisation de la base)
- tablefunc (fonctions de pivots de tables)
- btree_gin (permet la création d'index mixant btree et gin, utile pour du multi-champs mixant données classiques et json)


### Paramétrage

Se rendre sur  [pgtunes]([https://pgtune.leopard.in.ua/) et indiquer notre configuration matéielle.
Bien faire attention au "db type". Dans notre cas, comme il s'agit d'une base sur laquelle tournera un qgis en continu, on choisis "Desktop application".

Quelques explication des paramètres dont pgtunes vous donne les valeurs adaptées à votre config  :

- `shared_buffers` : La taille de la mémoire ram que postgres pourra utliser comme mémoire tampon.
- `work_mem`: Défini la taille de la mémoire qui pourra être utilisée par une requête. Attention ! On peut être plusieurs utilisateurs, un utilisataur peut exécuter plusieurs requêtes en même temps... ce qui peut saturer la mémoire si ce paramètre est trop élevé. Dépend aussi du nombre de processeurs disponibles pour la parallélisation. (voir  [episode PostgresFM](https://postgres.fm/episodes/work_mem) pour les méandres du paramétrage de work_mem).
- `random_page_cost` : le cout estimé d'un scan séquentiel d'une page utilisé par le planificateur de requête interne.
- `maintenance_work_mem` : la mémoire disponible pour les opérations de maintenance (aut-vacuum ...).
- `max_parallel_workers` : le nombre maximum de workers (de "processeurs") que pourra utiliser postgres quand il parallélise une requête.
- `max_worker_processes` : défini le nombre de processus d'arrière plan que le système supportera.
- `max_parallel_maintenance_workers` : le nombre de processus qu'utilisera postgres pour ses opérations d'auto-vaccum.

Pour définir ces paramètres, plusieurs options sont possibles (modifier postgres.conf...). Par sécurité et être sur que les modifications sont bien prises, je préfère la méthode des ALTER SYSTEM même si plus fastidieuse.

On se reconnecte à psql avec l'utilisateur posgres (on doit être superuser pour modifier ces paramètres)

```bash
sudo -u postgres psql -n nom_de_la_base
# remplacer nom de la base par ... le nom de votre base
```

Puis on lance les commandes

```sql
ALTER SYSTEM SET nom_param TO valeur;
# valeur prendra des guillements simples si texte (ex : '4GB'), si juste nombre alors pas de guillements
# attention a bien respecter la casse sur les unités de mémoire 'GB' 'kB'...
```

Où nom_param est le nom du paramètre à modifier et valeur la valeur donnée par pgtunes.

exemple
```sql
ALTER SYSTEM SET shared_buffers TO '4GB';
```

> De plus on modifira le paramètre `listen_addresses` qui indique les adresses ip que le serveur postgres écoutera. Par défaut cette valeur est 127.0.0.1 (c'est à dire que postgres n'écoute que votre pc). Pour que notre serveur puisse écouter des ip d'autres ordinateurs sur un réseau (local, internet ...) on passe ce paramètre à '*' (spéciale cacedédi à mon rrsi).

Et on redémare le serveur pour prendre en compte les modifications :

```bash
sudo systemctl restart postgresql-16
```

On peut véfifier la nouvelle valeur des paramètres avec la commande sql :

```sql
SHOW nom_param;
```

---
Si on a installé Hydra columnar, on passera cette commande sql pour activer le cache sur les tables orientées colonnes qui n'est 
pas activé par défaut dans la version open source.

```sql
set columnar.enable_column_cache = 't';

-- on peut ajuster la taille maximum de celui-ci avec
set columnar.column_cache_size = 'xxxxMB';
-- Attention, la valeur est par process, donc sera multiplié
-- par max_parallel_processes. Entre 200 et 20000, par défaut 200MB.
```

Puis on véfiera que les tables sont bien créés en "heap" par défaut 

```sql
SHOW default_table_access_method;
```

On utilise CREATE TABLE [...] USING columnar; pour spécifier celles colonnes.

---

Et voilà ! Restaurer un dump d'une base précédente si necessaire.


### Autres programmes relatifs aux bdd

Pgdmodeler

Il s'agit d'un modélisateur de sgbdr dédié à postgres très puissant, capable de lire vos bases existantes.

```bash
sudo dnf install pgmodeler
```

Dbeaver community edition

Logiciel de gestion de bases universel qu'on utilisera pour les bases sqlite (et geopackage), duckdb...

Se rendre sur le [https://dbeaver.io/download/](site de Dbeaver) et télécharger le rpm qu'il suffira de lancer.

Et si on veut pousser le vice et qu'on utilise KDE on installe umbrello (modélisateur UML austère qui fait aussi de l'entité relation)

```bash
sudo dnf install umbrello
```

## Mamba

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
# puis
bash Miniforge3-$(uname)-$(uname -m).sh
```

Conda installé de cette manière aura les dépôt conda-forge configurés par défaut.

Puis initialiser mamba :

```bash
source "${HOME}/miniforge3/etc/profile.d/conda.sh"
source "${HOME}/miniforge3/etc/profile.d/mamba.sh"
conda activate
conda init
mamba create -n env_name
mamba activate env_name
```

Si on désire que mamba ne s'active pas automotiquement au lancement d'un shell passer cette commande

```bash
conda config --set auto_activate_base false
```

### qgis

l'avantage de passer par un environnement, c'est que tout le support des paquets python sera bien intégré dans l'interpreteur de qgis.
Le dépôt qgis spécifique fedora (dani/qgis) n'est de tout façon plus maintenant au moment où ces lignes sont écrites.

Tout d'abord on va installer grass et son support dans qgis via grass-provider, hors envionnement mamba :

```bash
sudo dnf install qgis-grass
```

Les algorithmes de grass seront ainsi disponibles dans la boîte à outils de traitement de qgis.

Pour installer qggis :

``` bash
mamba install qgis
# ou pour une ltr
mamaba install qgis=3.34.3 #(indiquer le numéro de la vesion ltr actuelle)
```

On pense à bien se créer un profil tout de suite.

Pour mettre en raccourci dans le lanceur d'applications :

- Clic droit sur le bureau -> ajouter des conmposantes graphiques -> choisir "lancement rapide"
- Clic droit sur le lanceur et choisir "Ajouter un lanceur"
- Indiquer chemin votre_installation_miniforge/miniforge3/envs/nom_de_votre_env/bin/qgis
- En cliquant droit et en choisissant "modifier un lanceur" on peut lui attribuer une icone dédiée
- Glisser ce lanceur parmis votre autres icones
- Et maintenant clic droit sur le lanceur initial et le supprimer

Si on a installé une non ltr, on peut se créer un environnement vierge ne comprenant alors qu'une ltr à des fins de test et de vérification.

### ide python spyder

```bash
mamba install spyder
```

Lui créer un raccourci avec l'astuce utilisée ci-dessus pour qgis

### Autre spaquets

On préfère installer qgis avant quoi que ce soit pour avoir des dépendances propres. Puis on installe les paquets avec :

```bash
mamba install nom_paquet
```

## Autres logiciels

### Autres

[SAGA-GIS](https://saga-gis.sourceforge.io/en/index.html) (dont on va ajouter les algorithmes à qgis via saga-provider)

```bash
# On ajoute le dépôt
dnf copr enable megger/saga
# et on installe
dnf install saga
```

Puis dans Qgis ajouter l'extension "Processing Saga NextGen"

[Pycharm community edition](https://www.jetbrains.com/fr-fr/pycharm/download/?section=linux)

Télécharger et extraire l'archive dans le lien. Configurer pour utiliser l'environement mamba (Customize -> All settings -> python interpreter -> Add interpreter -> Conda -> sélectionner l'environnement)

[Git Kraken](https://www.gitkraken.com/download/linux-rpm]) Télécharger le rpm en lien et le lancer.

### Flatpak

Flatpak est installé par défaut sur Fedora, il faut juste activer le dépôt :

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

Ensuite blender :

```bash
flatpak install flathub org.blender.Blender
# puis
flatpak run org.blender.Blender
```
On installe ensuite QT Designer (pour pouvoir concevoir des interfaces qt) et Cloudcompare via discover (versions flatpak)
