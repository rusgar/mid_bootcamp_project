# import streamlit as st
# import pandas as pd
# import numpy as np  
# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
# load_dotenv()

# user = os.getenv("ATLAS_USER")
# password = os.getenv("ATLAS_PASSWORD")

# url =f"mongodb+srv://{user}:{password}@bdmlpt2501.62jmk.mongodb.net/test?authSource=admin&replicaSet=atlas-kvqvwn-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Beta&ssl=true"

# euro = MongoClient(url).get_database("core").euro

# paises_euro=st.slider("Selecion de Paises",1,20)

# info = euro.find({"Goles Metidos":8})
# data =list(info)



# st.subheader("Paises")
# st.write(data)

import  streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Informacion de la EURO 2020")

st.sidebar.subheader("Visualizacion")

carga_datos = st.sidebar.file_uploader(
            label = "Solo necesitas un archivo correcto",
            type =['csv','xlsx'] )


global df
if carga_datos is not None:
    print(carga_datos)
    print("hola")
    try:
        df = pd.read_csv(carga_datos)
    except Exception as e:
        print(e)
        df = pd.read_excel(carga_datos)


global numero_columnas
try:    
    st.write(df)
    numero_columnas = list(df.select_dtypes(["float","int"]).columns)
except Exception as e:
    print(e)
    st.write ("Solo necesitas un archivo correcto")


chart_select = st.sidebar.selectbox(
            label= "Seleccion de diagrama",
            options =["Scatterplots", "Lineplots", "Histogram","Boxplot"]
 )



if chart_select == "Scatterplots":
    st.sidebar.subheader("Scatterplots settings")
    try:
         x_values = st.sidebar.selectbox("x axis", options=numero_columnas)
         y_values = st.sidebar.selectbox("y axis", options=numero_columnas)
         plot = px.scatter(data_frame=df, x=x_values, y=y_values)
         st.plotly_chart(plot)
    except Exception as e:
        print(e)

