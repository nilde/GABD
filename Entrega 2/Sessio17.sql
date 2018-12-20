0. 
GRANT CREATE ANY TRIGGER TO AA_DESENVOLUPADOR;
GRANT CREATE ANY SEQUENCE TO AA_DESENVOLUPADOR;
GRANT ALTER ANY TRIGGER TO AA_DESENVOLUPADOR;
GRANT ALTER ANY SEQUENCE TO AA_DESENVOLUPADOR;
GRANT DROP ANY TRIGGER TO AA_DESENVOLUPADOR;
GRANT DROP ANY SEQUENCE TO AA_DESENVOLUPADOR;

CONNECT AA_DESENVOLUPADOR/123456;

DROP SEQUENCE id_seq_sequence;

CREATE SEQUENCE id_seq_sequence
INCREMENT BY 1
START WITH 1 ORDER
NOMAXVALUE;

DROP TABLE A;

CREATE TABLE A (
	id_seq number Not Null Primary Key,
	conf varchar2(255),
	nom varchar2(255)
);

CREATE UNIQUE INDEX unique_A
  ON A(conf, nom);

CREATE OR REPLACE 
TRIGGER A_trigger
BEFORE INSERT ON A
FOR EACH ROW
BEGIN
:NEW.id_seq := id_seq_sequence.NEXTVAL;
END;
/

CONNECT sys/oracle as SYSDBA;

GRANT SELECT, INSERT ON AA_DESENVOLUPADOR.A TO AA_DETECTOR_OUTLIERS;

CONNECT AA_DETECTOR_OUTLIERS/12;

INSERT INTO AA_DESENVOLUPADOR.A (conf,nom) VALUES ('2-0','hola');

INSERT INTO AA_DESENVOLUPADOR.A (conf,nom) VALUES ('2-0','adeu');

INSERT INTO AA_DESENVOLUPADOR.A (conf,nom) VALUES ('2-0','bonaTarda');

select * from AA_DESENVOLUPADOR.A;

1.
--tables already created

GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.DATABASEINFO TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.RESULTS_IMAGES TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.IMAGES TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.SETUPEXPERIMENT TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.NEURALNETS TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.RESULTS_VECTOR TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.VECTOR TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.SETUPEXPERIMENTHASEXPERIMENT TO AA_DETECTOR_OUTLIERS;
GRANT INSERT, UPDATE ON AA_DESENVOLUPADOR.EXPERIMENTS TO AA_DETECTOR_OUTLIERS;


---------------------------------------------------------------------
Exercici 2

CREATE FUNCTION loadVectorData(my_dataSet IN VARCHAR2)
	RETURN VARCHAR2 AS
IS
	v_test VARCHAR2;
	CURSOR c1
	IS
		SELECT ATTRIBUTEINFORMATION FROM DATABASEINFO WHERE TITLE = my_dataSet;
BEGIN
	OPEN c1;
		FETCH c1 INTO v_test;
	CLOSE c1;
RETURN v_test;
END;




---------------------------------------------------------------------
Exercici 3

CREATE FUNCTION loadVectorOutliers(my_dataSet IN VARCHAR2, my_configuracio IN VARCHAR2, my_repetition IN VARCHAR2)
	RETURN VARCHAR2 AS
IS
	v_test VARCHAR2;
	CURSOR c1
	IS
		SELECT ATTRIBUTEINFORMATION FROM DATABASEINFO 
		WHERE TITLE = my_dataSet
		AND Configuracio = my_configuracio
		AND repetition = my_repetition;
BEGIN
	OPEN c1;
		FETCH c1 INTO v_test;
	CLOSE c1;
RETURN v_test;
END;


---------------------------------------------------------------------
Exercici 4

CREATE FUNCTION insertExperiment(my_dataSet IN VARCHAR2)
	RETURN int AS
IS
	v_test VARCHAR2;
	CURSOR c1
	IS
		SELECT ID FROM DATABASEINFO WHERE TITLE = my_dataSet;
BEGIN
	OPEN c1;
		FETCH c1 INTO v_test;
	CLOSE c1;
RETURN v_test;
END;

---------------------------------------------------------------------
Exercici 5

CREATE FUNCTION insertVectorOutliers()
	RETURN VARCHAR2 AS
IS

BEGIN

END;

---------------------------------------------------------------------
Exercici 6

CREATE FUNCTION insertResultats()
IS

BEGIN

END;


---------------------------------------------------------------------

procedures: https://www.tutorialspoint.com/plsql/plsql_procedures.htm












