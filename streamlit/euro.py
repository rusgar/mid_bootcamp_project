import streamlit as st
import pandas as pd
import numpy as np  
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("ATLAS_USER")
password = os.getenv("ATLAS_PASSWORD")

url =f"mongodb+srv://{user}:{password}@bdmlpt2501.62jmk.mongodb.net/test?authSource=admin&replicaSet=atlas-kvqvwn-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Beta&ssl=true"

euro = MongoClient(url).get_database("core").euro

paises_euro=st.slider("Selecion de Paises",1,20)

info = euro.find({"Goles Metidos":8})
data =list(info)



st.subheader("Paises")
st.write(data)
