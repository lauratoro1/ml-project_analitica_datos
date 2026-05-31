import streamlit as st
import joblib
import pandas as pd
import numpy as np

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Despliegue de Modelos ML",
    page_icon="🤖",
    layout="centered"
)

# =====================================================
# CARGAR MODELOS
# =====================================================

modelo_regresion = joblib.load(
    "notebooks/models/model_regresion.joblib"
)

modelo_clasificacion = joblib.load(
    "notebooks/models/model_classification.joblib"
)

# =====================================================
# TÍTULO
# =====================================================

st.title("🤖 Aplicación de Machine Learning")

st.write("""
Aplicación desarrollada con Streamlit para realizar
predicciones usando modelos de regresión y clasificación.
""")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Configuración")

tipo_modelo = st.sidebar.selectbox(
    "Seleccione el modelo",
    (
        "Regresión",
        "Clasificación"
    )
)

# =====================================================
# MODELO REGRESIÓN
# =====================================================

if tipo_modelo == "Regresión":

    st.header("📈 Predicción de Costos Médicos")

    age = st.slider(
        "Edad",
        18,
        100,
        30
    )

    sex = st.selectbox(
        "Sexo",
        (
            "female",
            "male"
        )
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.slider(
        "Número de hijos",
        0,
        10,
        0
    )

    smoker = st.selectbox(
        "Fumador",
        (
            "yes",
            "no"
        )
    )

    region = st.selectbox(
        "Región",
        (
            "southwest",
            "southeast",
            "northwest",
            "northeast"
        )
    )

    # =================================================
    # DATAFRAME
    # =================================================

    datos = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    # =================================================
    # PREDICCIÓN
    # =================================================

    if st.button("Predict"):

        try:

            prediccion = modelo_regresion.predict(datos)

            st.success(
                f"💰 Costo médico estimado: ${prediccion[0]:,.2f}"
            )

        except Exception as e:

            st.error(f"Error: {e}")

# =====================================================
# MODELO CLASIFICACIÓN
# =====================================================

else:

    st.header("🩺 Predicción Enfermedad Renal")

    age = st.slider(
        "Edad",
        1,
        100,
        40
    )

    bp = st.slider(
        "Presión arterial",
        50,
        180,
        80
    )

    sg = st.number_input(
        "Gravedad específica",
        value=1.02
    )

    al = st.slider(
        "Albumina",
        0,
        5,
        0
    )

    su = st.slider(
        "Azúcar",
        0,
        5,
        0
    )

    datos = pd.DataFrame({
        "age": [age],
        "bp": [bp],
        "sg": [sg],
        "al": [al],
        "su": [su]
    })

    # =================================================
    # PREDICCIÓN
    # =================================================

    if st.button("Predict"):

        try:

            clase = modelo_clasificacion.predict(datos)

            st.success(
                f"🧪 Clase predicha: {clase[0]}"
            )

            if hasattr(modelo_clasificacion, "predict_proba"):

                probabilidad = modelo_clasificacion.predict_proba(datos)

                st.info(
                    f"📊 Probabilidad máxima: {np.max(probabilidad):.2f}"
                )

        except Exception as e:

            st.error(f"Error: {e}")