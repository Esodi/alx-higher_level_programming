-- showing list of tables
SET @dbname = 'mysql';
IF @dbname IS NULL THEN
	SETECT 'mysql';
ELSE
	USE @dbname;
	SHOW TABLES;
END IF;
