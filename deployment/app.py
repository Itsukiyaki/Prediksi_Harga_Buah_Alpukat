import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA','Prediksi Harga Buah Alpukat'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()