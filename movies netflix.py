# Importamos las librerías 
import pandas as pd
import streamlit as st
import codecs

# Formato 
st.title("Netfilx movies 2")
# Display the content of the dataset if checkbox is true
st.header("Base de datos Netflix")

st.header("Esta es una base de datos de las películas de Netflix")

DATA_URL = ("movies.csv")
@st.cache
def load_data(nrows): 
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text("Loading data")
data = load_data(500)
data_load_state.text("Done")

st.dataframe(data)
#Se trabaja en el slidebar 
sidebar = st.sidebar
sidebar.title("Busca la película.")
sidebar.write("Aquí van los elementos de entrada.")
#data_load_state 
agree = st.sidebar.checkbox("Muestra data set")
if agree:
  st.dataframe(DATA_URL)

#Buscador de películas 
@st.cache
def search_data(name) : 
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_filme = data[data['name'].str.upper().str.contains(str.upper(name))]

    return filtered_data_filme


myname = st.sidebar.text_input( "Titulo del filme :")
btnmov = st.sidebar.button("Buscar filme")
if (myname): 
     filterbyname = search_data(myname)
     count_row = filterbyname.shape[0] #Número columnas
     st.write(f"Total names :  {count_row}")

     
if (btnmov): 
    st.dataframe(filterbyname)
    
#Buscador de directores
@st.cache
def search_dir(director) : 
    doc1 = codecs.open('movies.csv','rU','latin1')
    data1 = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_dir = data1[data1['director'].str.upper().str.contains(str.upper(dir))]


selected_dir = st.sidebar.selectbox("Select director", DATA_URL['director'].unique())
st.write(f"Selected Option: {selected_sex!r}")
