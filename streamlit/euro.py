import streamlit as st  
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("ATLAS_USER")
password = os.getenv("ATLAS_PASSWORD")

url =f"mongodb+srv://{user}:{password}@bdmlpt2501.62jmk.mongodb.net/test?authSource=admin&replicaSet=atlas-kvqvwn-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Beta&ssl=true"

euro = MongoClient(url).get_database("bdmlpt2501").euro

paises_euro=st.slider("Selecion de Paises",1,20)

data = euro.find({"Paises":paises_euro})

st.json(data)