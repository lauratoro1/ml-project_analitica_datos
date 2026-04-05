
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
st.set_page_config(page_title="App Analítica", layout="wide")

st.title("📊 Análisis de Datos - Seguros")

# -----------------------------
# CARGA DE DATOS
# -----------------------------
@st.cache_data
def load_data():
    # Ruta absoluta segura
    base_path = os.getcwd()
    ruta = os.path.join(base_path, "data", "raw", "dataset_regresion.csv")
    
    df = pd.read_csv(ruta, sep=";")
    
    # Convertir columnas a numéricas
    df["charges"] = pd.to_numeric(df["charges"], errors="coerce")
    df["bmi"] = pd.to_numeric(df["bmi"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    
    return df

# 🔥 IMPORTANTE: cargar datos
df = load_data()

# -----------------------------
# VISTA PREVIA
# -----------------------------
st.subheader("🔹 Vista previa")
st.dataframe(df.head())

# -------------------------
# VISTA GENERAL
# -------------------------
st.subheader("📌 Vista previa")
st.dataframe(df.head())

st.subheader("📊 Estadísticas descriptivas")
st.write(df.describe())

st.subheader("🧾 Tipos de datos")
st.write(df.dtypes)


# -------------------------
# IMPUTACIÓN
# -------------------------
st.subheader("🧹 Imputación de datos")

df_imputado = df.copy()

for col in df_imputado.select_dtypes(include="number").columns:
    df_imputado[col] = df_imputado[col].fillna(df_imputado[col].mean())

st.write("Datos después de imputación:")
st.dataframe(df_imputado.head())


# -------------------------
# CORRELACIÓN
# -------------------------
st.subheader("🔗 Matriz de correlación")

corr = df_imputado.corr(numeric_only=True)

fig_corr, ax_corr = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax_corr)
st.pyplot(fig_corr)


# -------------------------
# GRÁFICOS
# -------------------------
st.subheader("📈 Gráficos principales")

columnas_numericas = df_imputado.select_dtypes(include="number").columns

col_x = st.selectbox("Selecciona variable X", columnas_numericas)
col_y = st.selectbox("Selecciona variable Y", columnas_numericas)

fig, ax = plt.subplots()
ax.scatter(df_imputado[col_x], df_imputado[col_y])
ax.set_xlabel(col_x)
ax.set_ylabel(col_y)

st.pyplot(fig)


# -------------------------
# PRUEBAS ESTADÍSTICAS
# -------------------------
st.subheader("🧪 Pruebas estadísticas")

if len(columnas_numericas) >= 2:
    col1 = columnas_numericas[0]
    col2 = columnas_numericas[1]
    
    # Pearson
    corr_pearson, p_value = stats.pearsonr(
        df_imputado[col1], df_imputado[col2]
    )
    
    st.write(f"📌 Correlación de Pearson entre {col1} y {col2}: {corr_pearson:.4f}")
    st.write(f"📌 p-valor: {p_value:.4f}")

    # Test normalidad
    stat, p = stats.shapiro(df_imputado[col1])
    st.write(f"📌 Test de normalidad (Shapiro) en {col1}: p = {p:.4f}")

else:
    st.warning("No hay suficientes variables numéricas para pruebas estadísticas")


# -------------------------
# FILTRO
# -------------------------
st.subheader("🔎 Filtro de datos")

columna_filtro = st.selectbox("Selecciona columna para filtrar", df.columns)

valores = df[columna_filtro].unique()

valor = st.selectbox("Selecciona valor", valores)

df_filtrado = df[df[columna_filtro] == valor]

st.dataframe(df_filtrado)