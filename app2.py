import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel('Kopie van 241017 Export beste keuzes Amsterdam (geanonimiseerd).xlsx')




st.title('Leerlingen in ODB')


# Calculate the counts of each unique school
school_counts = df['School'].value_counts()

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(school_counts)

# Streamlit bar chart (without x and stack arguments)
st.bar_chart(school_counts)