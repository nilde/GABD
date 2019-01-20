--EX3:
CREATE MATERIALIZED VIEW ex3_view
SELECT ex.conf, ex.repeticio, ex.method, ex.k, ex.m, ex.sigma, ex.id, dt.name, v.dades
FROM v2_experiments ex, v2_datasets dt, v2_vectors v, v2_outliers ou
WHERE dt.name=v.id_dataset and dt.name=ou.id_dataset;


--consulta 1:
SELECT ex.id, ex.conf, ex.method, ex.repeticio
FROM v2_experiments ex
WHERE ex.method="HOAD"

CREATE INDEX consulta1_ex3 ON experiments (id, conf, method, repeticio);

--amb index:
SELECT ex.id, ex.conf, ex.method, ex.repeticio
FROM v2_experiments ex WITH(INDEX(consulta1_ex3))
WHERE ex.method="HOAD"

--consulta 2:
SELECT ex.method, ex.id, ex.conf, ex.conf
FROM experiments ex, datasets dt
WHERE dt.name="Iris"

CREATE INDEX consulta2_ex3 ON experiments (conf, repeticio, method, id);

--amb index:
SELECT ex.method, ex.id, ex.conf, ex.conf
FROM experiments ex WITH(INDEX(consulta2_ex3)), datasets dt
WHERE dt.name="Iris"