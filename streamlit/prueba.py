import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title ("prueba de eurocopa 2020")

@st.cache
def load_data (nrows):
    data= pd.read_csv("../data/clean_euro_data.csv",nrows=nrows)
    return data


informacion= load_data(1000)

st.subheader("clean_data")
st.write (informacion)
if st.checkbox("Graficas"):
    st.bar_chart(informacion["Paises"])
    df = pd.DataFrame(informacion[:24], columns = ["Goles Metidos","Goles Encajados"])
    df.hist()
    st.pyplot()


    st.line_chart(df)
    chart_data = pd.DataFrame(informacion[:24], columns = ["Tiros a Puerta","Posesion por Partido"])
    st.area_chart(chart_data)


