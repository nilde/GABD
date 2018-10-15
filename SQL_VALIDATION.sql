

--Obtener la lista de usuarios y privilegios

SELECT * FROM master.sys.server_principals
SELECT * FROM USER_SYS_PRIVS; 
SELECT * FROM USER_TAB_PRIVS;
SELECT * FROM USER_ROLE_PRIVS;

--Para la validacion de consultas conectaremos con los usuarios creados y comprobaremos nuestros permisos:

SELECT count(*)
FROM   schema_name.table_name
where  1=0;

INSERT INTO schema_name.table_name
SELECT *
FROM   schema_name.table_name
WHERE  1=0;

DELETE FROM schema_name.table_name
WHERE  1=0;

UPDATE schema_name.table_name
SET    column_name = column_name
WHERE  1=0;