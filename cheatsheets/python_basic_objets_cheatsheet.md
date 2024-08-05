## Python basic objects spreedcheat

### texte

```python
texte.replace()
```

remplacer un caractère

### listes

#### accéder à un élément d'une liste

```python
liste[index] 
```

### Dictionnaires

#### accéder à un élement d'un dictionnaire

```python
dict[element] 
```

#### accéder à la liste des clefs d'un dictionnaire

```python
dict.keys() 
```

#### ajouter/modifier paire clef/valeur à un dictionnaire

```python
dict[key] = val
```

#### verifier la présence d'une clef dans un dict, renvoi un booléen

```python
key in dict
```

#### supprimer une paire clef/valeur

```python
del(dict[key])
```

### zip

#### afficher les élements d'un objet zip

```python
list(zip)
```

### boucles

#### sur listes

enumerate(liste) : obtenir l'index d'une liste
exemple :

```python
areas = ["name1", "name2"]
for index, a in enumerate(areas) :
	print("room " + str(index) + ": " + str(a))
```

#### sur dictionnaires

dict.items() créer une clef et une valeur pour chaque itération d'un dictionnaire
exemple :

```python
world = {"england": ["europe","english"], "france": [europe, "français"]}
for key, value in world.items():
	print(key + " -- '+  str(value))
```
key et value sont des noms arbitraires

#### sur array numpy

pour itérer sur un array multi-ligne numpy, utiliser np.nditer(my_array)
```python
for val in np.nditer(my_array):
```

#### sur dataframe pandas

pour itérer sur un dataframe pandas:
```python
for lab, row in df.iterrows():
	print(lab)
	print(row)
```python
lab = label index
row=  valeur de la ligne. On peut les spécifier : print(row["capital"])
