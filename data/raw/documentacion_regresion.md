# REGRESIÓN

## Nombre de la base de datos
**Insurance Charges Dataset – Base de datos de cargos médicos**

---

## Fuente
https://media.geeksforgeeks.org/wp-content/uploads/20240522154112/insurance%5B1%5D.csv

---

## Descripción general del problema

La base de datos Insurance Charges contiene información sobre los costos médicos facturados por compañías aseguradoras de salud a diferentes personas.

El propósito del estudio es analizar cómo ciertas características demográficas y de salud influyen en el costo individual de los servicios médicos o del seguro de salud.

Este tipo de análisis es relevante en:

- Economía de la salud  
- Análisis actuarial  
- Compañías aseguradoras  
- Estudios de riesgo médico  

Los datos representan patrones realistas de facturación médica y son utilizados principalmente con fines educativos y de análisis estadístico.

Actualmente esta base es difundida en plataformas académicas y repositorios de ciencia de datos para el estudio de modelos de regresión y predicción de costos médicos.

---

## Objetivo del análisis

Construir un modelo estadístico que permita:

- Explicar el costo médico  
- Predecir el costo médico individual  

Cada observación corresponde a una persona asegurada.

---

## Variable objetivo

**Charges**

- Tipo: Cuantitativa continua  
- Describe: Costo total médico o de seguro  
- Unidad: Dólares  

✔ Este es un problema de **regresión**

---

## Diccionario de variables

### Age
- Tipo: Cuantitativa discreta  
- Descripción: Edad  

---

### Sex
- Tipo: Cualitativa nominal  
- Descripción: Sexo  

---

### BMI
- Tipo: Cuantitativa continua  
- Descripción: Índice de masa corporal  

---

### Children
- Tipo: Cuantitativa discreta  
- Descripción: Número de hijos  

---

### Smoker
- Tipo: Cualitativa binaria  
- Valores:
  - yes = fumador  
  - no = no fumador  

---

### Region
- Tipo: Cualitativa nominal  
- Descripción: Región  

---

### Charges
- Tipo: Cuantitativa continua  
- Descripción: Cargos médicos  

---

## Tamaño del dataset

- Número de observaciones: **1338 personas**  
- Número de variables: **7**

---

## Hipótesis

### Hipótesis general

- H₀: Las características no influyen en el costo médico  
- H₁: Al menos una característica influye  

---

### Hipótesis específicas

#### Hábito de fumar
- H₀: No influye  
- H₁: Sí influye  

#### Edad
- H₀: No influye  
- H₁: Sí influye  

#### BMI
- H₀: No influye  
- H₁: Sí influye  

#### Número de hijos
- H₀: No influye  
- H₁: Sí influye  

---

## Técnicas estadísticas

- Estadística descriptiva  
- Diagramas de dispersión  
- Correlación  
- Prueba t de medias  
- ANOVA  
- Regresión lineal múltiple  
- Diagnóstico de residuos  
- Transformación logarítmica  

---

## Conclusión

Esta base permite analizar los factores que determinan el costo médico individual mediante modelos de regresión, siendo ampliamente utilizada en estudios predictivos de seguros de salud.