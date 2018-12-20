/*Exercici 2. Programeu un script RMAN per fer una copia de seguretat. Feu la copia de seguretat de
l’oracle de la màquina Oracle-2.*/
connect target sys/oracle;
backup database;


/*Exercici 3. Ajudeu-vos de l’eina cron/crontab de linux per a programar còpies de seguretat periòdiques.
Feu el script que programa aquestes còpies de seguretat utilitzant el script RMAN de l’exercici anterior.*/
echo "10 0 0 0 0 oracle 'rman @PATH/scripts/backup.rman'" >> /etc/crontab

/*Exercici 4. Des de l’Oracle-2 anem a simular una pèrdua d’un datafile. Creeu un nou tablespace. Creeu
una taula test dins el tablespace. Inseriu 20 registres dins la taula test. Elimineu el datafile corresponent
al tablespace creat (prèviament feu una còpia) en el que es troben les dades de la taula test. Apagueu i
inicieu oracle (com al exercici 1a). Que ha passat? Restaura la base de dades. Com ho heu fet? Heu
pogut recuperar tota la informació?
Fes el mateix experiment però inserint 200.000 registres. Heu pogut recuperar tota la informació?
Perquè? On estaven guardades les dades que s’han pogut recuperar tenint en compte que la còpia de
seguretat era prèvia?
Nota: Per inserir les dades a la taula test ajudeu-vos d’un procediment PL/SQL que automàticament faci
els inserts corresponents.*/ 
sys/oracle as sysdba;
CREATE TABLESPACE TS_test
DATAFILE 'test.dbf'
SIZE 10M;

--insercion datos
CREATE TABLE test (
    id integer Not Null Primary Key,
    nombre varchar2(255)
)
TABLESPACE TS_test;

RMAN>connect target sys/oracle;
RMAN>backup database;

sys/oracle as sysdba;
DECLARE i INTEGER := 1;
BEGIN
  WHILE i <= 20 LOOP
   INSERT INTO test (nombre)
   values ('testingValue');
    i := i + 1;
  END LOOP;
END;

--maybe hay que poner path entero de test.dbf
ALTER TABLESPACE TS_test DROP DATAFILE 'test.dbf';

--HACER RECOVER
SHUTDOWN ABORT;
STARTUP;

sys/oracle as sysdba;
CREATE TABLESPACE TS_test2
DATAFILE 'test2.dbf'
SIZE 10M;

--insercion datos
CREATE TABLE test2 (
    id integer Not Null Primary Key,
    nombre varchar2(255)
)
TABLESPACE TS_test2;

RMAN>connect target sys/oracle;
RMAN>backup database;

sys/oracle as sysdba;
DECLARE i NUMBER := 1;
BEGIN
  WHILE i <= 200000 LOOP
   INSERT INTO test2 (nombre)
   values ('testingValue');
    i := i + 1;
  END LOOP;
END;

--maybe hay que poner path entero de test.dbf
ALTER TABLESPACE TS_test2 DROP DATAFILE 'test2.dbf';

--HACER RECOVER
shutdown abort;
startup mount;


/*Exercici 5. Igual que a l’exercici 4 anem a simular una pèrdua d’un datafile però en aquest cas amb el
ARCHIVELOG activat. Explica que passa si repetim el experiment de l’exercici 4 (feu directament el cas
de 200.000 registres). Ha pogut recuperar totes les dades? On estaven guardades les dades que s’han
pogut recuperar tenint en compte que la copia de seguretat era prèvia?*/

sys/oracle as sysdba;
archive log list;
show parameter recovery_file_dest;
--SQL> alter system set log_archive_dest_1 = ""

--activar
alter database archivelog;
alter database open;

--Revisar archivelog activado
archive log list;

CREATE TABLESPACE TS_test3
--quiza hay q poner otro dbf diferente
DATAFILE 'test3.dbf'
SIZE 10M;

--insercion datos
CREATE TABLE test3 (
    id integer Not Null Primary Key,
    nombre varchar2(255)
)
TABLESPACE TS_test3;

RMAN>connect target sys/oracle;
RMAN>backup database;

sys/oracle as sysdba;
DECLARE i NUMBER := 1;
BEGIN
  WHILE i <= 200000 LOOP
   INSERT INTO test3 (nombre)
   values ('testingValue');
    i := i + 1;
  END LOOP;
END;

--maybe hay que poner path entero de test.dbf
ALTER TABLESPACE TS_test3 DROP DATAFILE 'test3.dbf';


--SQL> shutdown immediate
shutdown abort;
startup mount;