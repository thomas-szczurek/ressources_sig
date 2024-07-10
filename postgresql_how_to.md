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

### Contraintes d'intégrité

#### Désactivation des triggers (y comprit ceux des checks de clefs étrangère) d'une table

```sql
ALTER TABLE schema.table_name DISABLE TRIGGER ALL;
-- Do your things
ALTER TABLE schema.table_name ENABLE TRIGGER ALL;
```

#### Désactivation d'un trigger en particuler

```sql
SELECT tgname,
       tgtype
FROM pg_trigger
WHERE tgrelid = '<schema>.<table>'::regclass
  AND tgisinternal;

-- Ensuite

ALTER TABLE <schema>.<mytable>
   DISABLE TRIGGER "<tgname>"
```

### json

#### Remplacer le nom d'une clef dans un champ json/jsonb

```sql
create table example(id int primary key, champ jsonb);
insert into example values
    (1, '{"nme": "test"}'),
    (2, '{"nme": "second test"}');

update example
set champ = champ - 'nme' || jsonb_build_object('name', champ -> 'nme')
where champ ? 'nme'
returning *;
```

#### Remplacer la valeur d'une clef dans un champ json/jsonb

```sql
update example
set champs = champs - 'name' || jsonb_build_object('name', replace((champs ->> 'name'),'<from>','<to>'))
where champ ? 'name'
returning *;
```
