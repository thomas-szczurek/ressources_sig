### Description table

#### Description des champs d'une table

```sql
SELECT * FROM information_schema.columns
WHERE
  table_schema = '<schema name>' AND
  table_name = '<table name>';
```

#### Récupérer les contraintes d'une table :

```sql
SELECT con.*
       FROM pg_catalog.pg_constraint con
            JOIN pg_catalog.pg_class rel
              ON rel.oid = con.conrelid
            JOIN pg_catalog.pg_namespace nsp
              ON nsp.oid = connamespace
       WHERE nsp.nspname = '<schema name>'
             AND rel.relname = '<table name>';
```

### json

#### Remplacer une clef dans un champ json/jsonb

```sql
create table example(id int primary key, js jsonb);
insert into example values
    (1, '{"nme": "test"}'),
    (2, '{"nme": "second test"}');

update example
set js = js - 'nme' || jsonb_build_object('name', js->'nme')
where js ? 'nme'
returning *;
```

#### Remplacer la valeur d'une clef dans un champ json/jsonb

```sql
update example
set <champs> = <champs> - 'name' || jsonb_build_object('name', replace((<champs> ->> 'name'),'<from>','<to>'))
where <champ> ? 'name'
returning *;
```
