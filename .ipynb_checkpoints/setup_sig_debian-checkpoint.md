## debian

- rendre utilisateur user-name membre du groupe sudo
```bash highlight-stlye: breezedark
su
sudo adduser user-name sudo
```

reboot pc

- drivers Nvidia 
-- /etc/apt/sources.list -> passer bookworm en sid si nécessaire
-- Ajoutez les éléments « contrib », « non-free » et « non-free-firmware » à /etc/apt/sources.list, par exemple : 
```
deb http://deb.debian.org/debian/ bookworm main contrib non-free non-free-firmware
```
```bash
sudo apt update
sudo apt install nvidia-driver firmware-misc-nonfree
sudo apt install nvidia-cuda-dev nvidia-cuda-toolkit
sudo apt install libnvoptix1
```
-- repasser sid en bookworm si modifié
-- reboot pc

## Qgis

[article geotribu](https://geotribu.fr/articles/2023/2023-01-05_installer-qgis-sur-ubuntu/#choix)
tldr;

```bash
sudo apt update
sudo apt install ca-certificates gnupg lsb-release software-properties-common
sudo mkdir -p /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/debian \
$(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/qgis.list > /dev/null

less -F /etc/apt/sources.list.d/qgis.list
sudo apt update
sudo apt install qgis-plugin-grass
```

### création de l'environnement virtuel

```bash
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv /path/to_/venv
```

- On se créé un profil qgis
- Préférences -> Options -> Système -> Desecendre à "environnement" et ajouter "ajouter à la fin | variable : PYTHONPATH | Valeur : pathtovenv/lib/python3.11/site_packages
- Pour ajouter des paquet, ouvrir un terminal dans /path_to_venv/bin, ensuite :

 ```bash
./pip install nom_du_paquet
```

## Postgres

``` bash
# Create the file repository configuration:
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql-16
```

 **Toujours installer une version spécifique** ex : apt intall postgresql-16

### pgadmin

 ```bash
 #
# Setup the repository
#

# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Install pgAdmin
#

# Install for desktop mode only:
sudo apt install pgadmin4-desktop
```

### attribution d'un mot de passe à l'utilisateur postgres

```bash
sudo -u postgres psql
# Une fois connecté à psql
\password
# attribuer un mot de passe
\q
```

### initialisation postgresql

- lancer pgadmin, sur serveurs -> register -> server
- Name : localhost | host name/adress : localhost | password : postgres_password
- files -> preferences -> display -> show template databases
- créer un nouveau groupe utilisateur et un utilisateur associé avec les droits élargis mais non superuser
- installer postgis

```bash
sudo apt install postgresql-16-postgis-3
```

- Créer la base de données pour données geo, y activer postgis, postgis raster, postgis sfgcal, postgis topology, pg_stat_statements, file_fdw, postgres_fdw
- se rendre sur le site pgtunes et indiquer la config désirée
- lancer la commande SHOW config_file en tant que postgres et se rendre à l'emplacement pour modifier postgresql.conf
- appliquer les paramètres de pgtunes
- relancer le serveur postgres

```bash
sudo systemctl stop postgresql
sudo systemctl start postgresql
```


- restaurer un dump de la base si nécessaire
- créer la connection du Qgis (avec une autentification dédiée)

## Autres installations

```bash
sudo apt install pgmodeler
sudo apt install postgresql-16-ogr-fdw
```
- installer ogr_fdw sur la base PostgreSQL
- Télécharger Pycharm et installer
- Télécharger WhiteBoxTools et installer


## mamba

- installation

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
source "${HOME}/miniforge3/etc/profile.d/conda.sh"
source "${HOME}/miniforge3/etc/profile.d/mamba.sh"
conda activate
conda init
mamba create -n envi_name
mamba activate env_name
```

- installer packages dont l'IDE spyder

```bash
mamba install package_name
mamba install spyder
```
- Configure Pycharm pour utiliser l'environnement

## sid
- /etc/apt/sources.list -> passer bookworm en sid 
- installation SAGA

```bash
sudo apt update
sudo apt install saga
```
- /etc/apt/sources.list -> passer sid en bookworm

 ```bash
sudo apt update
```
## Flatpak

```bash
sudo apt install flatpak
# plugin spécifique KDE
sudo apt install plasma-discover-backend-flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

- installer Blender, Inkscape, Scribus, Coudcompare

??? Reste OrfeoToolBox dont le Qgis Provider ne semble pas être dispo dans Qgis 3.36 installé de cette manière ??? 

