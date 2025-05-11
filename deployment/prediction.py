import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title='Avocado Price Prediction',
    layout='wide',
    initial_sidebar_state='expanded'
)

with open('best_rnd_reg_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
def run():
    # Membuat Form
    with st.form(key='Form_Prediksi_Harga_Buah_Alpukat'):
        total_sales = st.number_input('Jumlah hasil panen : ',min_value=1,max_value=200000)
        type = st.radio('Jenis Buah Alpukat',('Konvensional','Organik'),index=0)
        if type == 'Konvensional':
            type = 0
        else: 
            type = 1
        
        submitted = st.form_submit_button('Predict')
    
    df_inf = {
    'total_sales': total_sales,
    'type': type
    }
    
    # Convert to dataframe pandas
    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)
    
    if submitted:
        prediction = model.predict(df_inf)
        
        st.write('Prediksi Harga: $',str(round(float(prediction),2)))
        
if __name__ == '__main__':
    run()