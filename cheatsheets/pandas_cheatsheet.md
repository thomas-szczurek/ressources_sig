## index

* df.index = [list] : redéfinir index

## création dataframe

* pf.read_csv(path, index_col = 0) :  A partir d'un csv. Optionnel : Défini la colonne à utiliser pour l'index avec index_col, pandas en créé une si non défini)

## Selection

* df["column"] : sélectionner une colonneen tant que pandas.series
* df[["column1, solumn2"]] : sélectionner une/des colonne/s en tant que pandas.dataframe
* df[1:4] : sélectionner un slice de lignes
* df.loc[index] : renvois une pandas.series contenant les informations de la ligne
* df.loc[index] : renvoi une pandas.dataframe
* df.loc[[val_index1,val_index3,val_index3],[col1,col3]] :renvoi une pandas.dataframe sur ces lignes et colonnes
* df.loc[:, [col1,col3]] : renvoi les colonnes 1 et 3 pour toutes les lignes
* sélectionner non par valeur mais pas position des élements peut se faire avec df.iloc[]

* Filtrer
* sel = df[df['critere']] : ne sélectionne que les lignes où le critère est 'True'

## Apply

```python
df[new_column_name] = df[column].apply(function)
```

## ajouter nouvelle colonne dans un loop

```python
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
```
