import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


#loading the data
@st.cache_data
def load_data():
    path='data\kc_house_data.csv'
    df = pd.read_csv(path)
    return df



