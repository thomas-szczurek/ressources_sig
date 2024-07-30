# Distributions a 1 dimension

## Mode

(valeur d'une série pour laquelle l'effectif est le max)

### Derterminer le mode pour des classes d'amplitude inégales

Calculer la densité de chaque classe :

> d = effectif/aplitude

La classe avec la densité la plus élevée est celle où se situe le mode.

> mode =
> ((min_classe * (densité - densité_classe-1)) + (max_classe * (densité - densité_classe+1))
> / ((densité - densité_classe-1) + (densité - densité_classe+1)))

## Médiane

### Determiner médiane (ou autre quantile) de classes de valeurs continues par interpolation linéaire

Déterminer classe où se situe la médiane (ou autre quantile) puis :

> Médiane = min classe + (((50-frequence cumulée min) * diff min/max classe) / diff frequences cumulées)

Pour une classe 30/40 avec fréquences 46,2% et 86,7% :

![img_mediane](https://github.com/thomas-szczurek/ressources_sig/tree/master/cheatsheets/img/mediane.png)

Mediane = 30 +((3,68*10) / 35,38)

## Moyennes

### Moyenne géométrique (et taux de variation)

#### Simple

S'utilise principalement pour le calcul des taux de variation moyens (quand on connait les taux entre chaque année)

Soit n observations d'un fichier indiduel : x1, x2, x..., xn (ou x serait un taux d'évolution)

> Moyenne = racine n**ième** de (x1 * x2 * x... * xn)

> Taux de variation annuel : (val finale / val initiale) - 1
> Taux de variation annuel moyen (quand on ne connait pas les valeurs intermédiaires) :
> racine n**ième** de ((val finale / val initiale) - 1)

#### Pondérée

Par exemple avec des classes d'année. On met alors en puissance la valeur de chaque x par le nombre d'année de la classe. La racine est celle du total des années concernées.

### Moyenne Harmonique

#### Simple

S'utilise principalement pour le calcul des moyennes de pourcentages, ou plus généralement des ratios, notamment pour des durées ou des vitesses moyennes

> 1/Moy = 1/n * (1/x1 + 1/x2 + 1/xn)

Ou n est le nombre d'observations, x leur valeur

Ex : 2 personnes déposent 1200 et 1000 sur un compte et epargne jusqu'à obtenir 60000. 50 ans pour le 1er, 60 ans pour le 2nd, 55 en moyenne.
Quelle est leur épargne moyenne mensuelle ?

> 1/moyenne = 1/2*(1/1200 + 1/1000) = 0,00091

Soit moyenne = 1090,9090

#### Pondérée

1/x1 devient n1/x1

Part de femmes dans les csp
Ex:
csp_a 49,7% 14573
csp_b 48,6% 84807
csp_c 62,9% 15048

> 1/moyenne = 1/114428 * (14573/49,7 + 84807/48,6 + 15048/62,9)

### Moyenne Quadratique

S'utilise pour calculer les moyennes d'écarts par rapport à une valeur centrale donnée par un paramètre de position. (les carrées permettent donc de ne manipuler que des écarts positifs)

#### Simple

Se calcule par la racine carée de la moyenne arithmétique des carrés des valeurs de la série

> racine((x1² + x2² + xn²) / n)

Soit 3 parcelles de 30, 45 et 60m². Quelle est la taille par le côté d'une parcelle moyenne ?

> racine((30² + 45² + 60²) / 3) = 46,64m

#### Pondérée

Se calcule comme pour une moyenne arithmétique : x1² devient n*x1² et on divise pas la somme de n

## Ecarts élémentaires

### Ecarts interquantiles

> Q3 - Q1 écart interquartile
> D9 - D1 écart interdécile
> C99 - C1 écart intercentile

### Ecart absolu moyen par rapport à la moyenne

Moyenne des écarts à la moyenne absolus.
Peut se calculer en pondéré à condition de d'abord calculer la moyenne pondérée puis de pondérer l'écart de chaque modalité par son nombre d'individus

### Ecart type

**A préférer à l'écart absolu moyen** (pour éviter de travailller avec des valeurs absolues)

**Est synonyme d'écart quadratique moyen**

> *variance* = ((x1-xmoy)² + (x2-xmoy)² + (xi-xmoy)² + (xn-xmoy)²) / 2 : s'exprime dans le carré de l'unité de la variable
> ou formule développée (plus rapide à calculer) = ((x1² + x2² + xi² + xn²) / n) - xmoy²
> *écart type* = racine(variance)

La variance peut se pondérer de la même manière que pour les autres `estimateurs`

### Dispersion relative

L'écart type, comme la moyenne... sont exprimés dans la même unité que la variable. De ce fait il est impossible de comparer la dispersion de séries statistiques qui ne sont pas exprimés dans la même unité ou ayant des ordres de grandeurs différents (département vs Etat).

Pour y pallier on défini `l'écart absolu moyen relatif` ou `le cefficient de variation`.

#### Ecart moyen relatif

> écart relatif = écart absolu moyen / moyenne.arithmétique (exprimé en %)

#### Coefficient de variation

Comme pour l'écart type **A préférer à l'écart moyen relatif**

> coefficient de variation = écart type / moyenne.arithmétique (exprimé en %)

## La Médiale

Au contraire des `estimateurs` de dispersion, on s'interesse ici à la notion de concentration.

### Valeurs globales

Les valeurs globales s'obtiennent en multipliant les valeurs xi par leur effectif ni

> valeurs globales = xi * ni

Elles débouches sur les valeurs globales relatives (qi)

> Qi = (ni * xi) / somme (x * n) * 100 %

On peut ainsi en déterminer les fréquences cumulées croissantes pour chaque valeur de x.

### Médiale

Il s'agit de la valeur pour laquelle Qi = 50 %

Elle se calcule de la même manière que la médiane, soit graphiquement, soit algébriquement. (voir médiane)

### Ecart médiale-médiane

De manière générale, on dit qu'il y a `concentration` lorsqu'on observe de fortes disparités entre la part que représente chaque modalité en terme d'effectifs, et celle qu'elle occupe au niveau des valeurs globales. L'écart médiale-médiane constitue l'un des indicateurs permettant d'évaluer cette concentration.
