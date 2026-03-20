# CLASIFICACIÓN

## Nombre de la base de datos
**Titanic Dataset – Titanic Base de Datos**

## Fuente
https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

---

## Descripción general del problema

La base de datos Titanic contiene información sobre los pasajeros que viajaban en el RMS Titanic, un barco británico que se hundió en el océano Atlántico en abril de 1912. El hundimiento del Titanic es uno de los naufragios más famosos de la historia.

El 15 de abril de 1912, durante su viaje inaugural, el RMS Titanic, considerado ampliamente como “insumergible”, se hundió después de chocar con un iceberg. Lamentablemente, no había suficientes botes salvavidas para todas las personas a bordo, lo que provocó la muerte de 1502 de los 2224 pasajeros y tripulantes.

Aunque hubo cierto elemento de suerte en la supervivencia, parece que algunos grupos de personas tenían mayor probabilidad de sobrevivir que otros.

---

## ¿De dónde se recolectaron los datos?

Los datos provienen de:

- Registros históricos del viaje del Titanic  
- Listas oficiales de pasajeros  
- Informes de supervivencia posteriores al accidente  

Posteriormente:

- Fueron organizados y digitalizados por investigadores y comunidades académicas de análisis de datos (especialmente UCI y Kaggle)

Hoy en día se usan como:

- Base educativa  
- Competencia de machine learning  
- Ejemplo clásico de clasificación  

---

## ¿Quién realizó el estudio?

No fue un estudio experimental moderno.

Los datos fueron:

- Recopilados originalmente por autoridades marítimas británicas  
- Documentados en informes oficiales del desastre  
- Estructurados posteriormente por científicos de datos y universidades  

Actualmente la base es difundida por:

- Kaggle  
- UCI Machine Learning Repository  

---

## Objetivo del análisis

Construir un modelo predictivo que responda a la pregunta:

> ¿Qué tipo de personas tenían más probabilidades de sobrevivir?

Utilizando datos de los pasajeros como:

- Nombre  
- Edad  
- Género  
- Clase socioeconómica  

Cada fila representa un pasajero y contiene variables demográficas, económicas y de ubicación dentro del barco.

---

## Variable objetivo

**Survived**

- Tipo: Variable categórica binaria  
- Valores:  
  - 0 → No sobrevivió  
  - 1 → Sobrevivió  

✔ Es un problema de **clasificación supervisada**

---

## Diccionario de variables

### PassengerId
- Tipo: Cualitativa nominal  
- Descripción: Identificador único del pasajero  

---

### Survived
- Tipo: Cualitativa binaria  
- Descripción: Indica si sobrevivió o no  
- Valores:
  - 0 = No sobrevivió  
  - 1 = Sobrevivió  

---

### Pclass
- Tipo: Cualitativa ordinal  
- Descripción: Clase socioeconómica  
- Valores:
  - 1 = Alta  
  - 2 = Media  
  - 3 = Baja  

---

### Name
- Tipo: Cualitativa nominal  
- Descripción: Nombre del pasajero  

---

### Sex
- Tipo: Cualitativa binaria  
- Valores:
  - male = hombre  
  - female = mujer  

---

### Age
- Tipo: Cuantitativa continua  
- Descripción: Edad  

---

### SibSp
- Tipo: Cuantitativa discreta  
- Descripción: Número de familiares (hermanos/esposo/a)  

---

### Parch
- Tipo: Cuantitativa discreta  
- Descripción: Padres o hijos a bordo  

---

### Ticket
- Tipo: Cualitativa nominal  
- Descripción: Código del tiquete  

---

### Fare
- Tipo: Cuantitativa continua  
- Descripción: Precio del pasaje  

---

### Cabin
- Tipo: Cualitativa nominal  
- Nota: Muchos valores faltantes  

---

### Embarked
- Tipo: Cualitativa nominal  
- Valores:
  - C = Cherbourg  
  - Q = Queenstown  
  - S = Southampton  

---

## Tamaño del dataset

- Número de observaciones: **891 pasajeros**  
- Número de variables: **12**

---

## Hipótesis

### Hipótesis general

- H₀: Las características no influyen en la supervivencia  
- H₁: Al menos una característica influye  

---

### Hipótesis específicas

#### Sexo
- H₀: Igual probabilidad  
- H₁: Mujeres sobreviven más  

#### Clase
- H₀: No influye  
- H₁: Clases altas sobreviven más  

#### Edad
- H₀: No influye  
- H₁: Jóvenes sobreviven más  

#### Tarifa
- H₀: No influye  
- H₁: Mayor tarifa → mayor supervivencia  

---

## Técnicas estadísticas sugeridas

- Estadística descriptiva  
- Prueba Chi-cuadrado  
- Prueba t o Mann-Whitney  
- Regresión logística  

---

## Modelo

Se pueden implementar modelos de clasificación como:

- Regresión logística  
- Random Forest  
- Árboles de decisión  