import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gpa=pd.read_csv("promedio_tabla.csv")

st.title("promedio")

tab1, tab2= st.tabs(["tab1","tab2"])

with tab1:
    st.header("analisis univariado")
    fig, ax=plt.subplots(1,4, figsize=(10,5))
    ax[0].hist(gpa["edad"])
    conteo=gpa["sexo"].value_counts()
    ax[1].bar(conteo.index,conteo.values)
    conteo=gpa["hermanos"].value_counts()
    ax[2].bar(conteo.index,conteo.values)
    ax[3].hist(gpa["promedio"])

    st.pyplot(fig)

with tab2:
    st.header("analisis multivariado")

    fig, ax=plt.subplots(1,3, figsize=(10,5))
    sns.scatterplot(data=gpa, y="promedio", x="edad", ax=ax[0])
    sns.boxplot(data=gpa, y= "promedio", x= "sexo", ax=ax[1])
    sns.boxplot(data=gpa, y="promedio", x= "hermanos", ax=ax[2])
    fig.tight_layout()

    st.pyplot(fig)
