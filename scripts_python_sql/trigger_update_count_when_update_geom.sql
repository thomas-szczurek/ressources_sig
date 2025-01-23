-- Fonctionne pour SQLIte et non pour PostgreSQL où il faudrait adapter

-- Ce trigger permet de mettre à jour un champ contenant un count d'objets d'une autre
-- table (type polygone contenant des points) lors d'une modification de sa géométrie

CREATE TRIGGER trig_name
AFTER UPDATE OF geom ON t1
FOR EACH ROW
BEGIN
	UPDATE t1
	SET champ = (
		SELECT
			CAST(count(t2.fid) AS INTEGER)
		FROM t1 AS t1, t2
		WHERE "t2"."CYCLE 2" = 'MATERNELLE' AND 
			st_contains(t1.geom, t2.geom) AND
			t1.fid = new.fid
		GROUP BY t1.Denomination, t1.validite
			)
	WHERE t1.fid = new.fid;
END;
