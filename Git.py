import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st

# Descargar datos históricos de Bitcoin
BTC = yf.download('BTC-USD', start='2024-09-25')


BTC.to_csv('output.csv')

st.title('Prueba de Streamlit')
st.write('¡Streamlit está funcionando!')

file=pd.read_csv('output.csv')

Out=pd.DataFrame(file)


st.dataframe(Out.iloc[::-1].round(2), use_container_width=True)