import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def run():
    
    # Title
    st.title('Prediksi Harga Buah Alpukat')
    
    # Sub Header
    st.subheader('Page Mengenai Exploratory Data Analysis dari Dataset Avocado Price')
    
    # Menampilkan Gambar
    image = Image.open('images.jpg')
    st.image(image, caption='Avocado')
    
    # Teks
    st.write('Page ini dibuat untuk memenuhi Milestone 2 FTDS-RMT-040, dibuat oleh **Eldi MS**')
    
    # Menampilkan Data Frame
    data = pd.read_csv('avocado.csv')
    data.drop(columns='Unnamed: 0',inplace=True)
    col = ['Total Volume', '4046', '4225', '4770', 'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags']
    data[col] = data[col].astype(int)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    st.dataframe(data)
    st.write('Dataset Source:')
    st.link_button('Kaggle','https://www.kaggle.com/datasets/neuromusic/avocado-prices')
    
    # Membuat Histogram
    option = st.selectbox('Pilih Kolom : ', ('Date', 'AveragePrice', 'Total Volume', 
                                             '4046', '4225', '4770','Total Bags', 'Small Bags', 'Large Bags', 
                                             'XLarge Bags', 'type', 'year','region'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option],bins=30,kde=True)
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    run()