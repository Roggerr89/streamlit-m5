import streamlit as st 
import pandas as pd 

st.title('Streamlit con cache')
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done !")

st.dataframe(data)