import streamlit as st
from streamlit_option_menu import option_menu
import base64
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Jobs Page', page_icon='🕸️')

with open('img.jpg','rb') as f:
    file=f.read()
img= base64.b64encode(file).decode()
css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url('data:image/png;base64,{img}');
        background-size:cover
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

df=pd.read_csv('Ai_imp.csv')
st.write(df)

ch1=px.bar(x=df.Job_Title.value_counts().index,y=df.Job_Title.value_counts().values)
st.plotly_chart(ch1)

col1,col2=st.columns(2)
with col1:
    ch2=px.pie(names=df.Education_Level.value_counts().index,values=df.Education_Level.value_counts().values)
    st.plotly_chart(ch2)

with col2:
    total=df['Job_Title'].value_counts()
    total








    




