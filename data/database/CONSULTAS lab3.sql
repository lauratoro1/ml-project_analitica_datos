CONSULTAS PARA REGRESION 

SELECT COUNT(*) FROM regresion;

SELECT AVG(CAST(charges AS REAL)) FROM regresion;

SELECT smoker, AVG(CAST(charges AS REAL)) 
FROM regresion 
GROUP BY smoker;

SELECT sex, AVG(CAST(charges AS REAL)) 
FROM regresion 
GROUP BY sex;

SELECT COUNT(*) FROM regresion WHERE smoker = 'yes';

CONSULTAS PARA clasificacion

SELECT class, COUNT(*) 
FROM clasificacion 
GROUP BY class;

SELECT AVG(age) FROM clasificacion;

SELECT COUNT(*) FROM clasificacion WHERE htn = 'yes';

SELECT class, AVG(age) FROM clasificacion GROUP BY class;
