import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Home Page', page_icon='🛖')

st.title('Zomato Page 💀')
df=pd.read_csv('zomato_dataset.csv')
st.write(df.shape)
df.dropna(axis=0,inplace=True)
st.write(df.shape)
df.drop_duplicates(inplace=True)
st.write(df.shape)

st.write(df)
res_index=df.loc[:,"Restaurant Name"].value_counts().index
st.write(res_index)
with st.sidebar:
    selected_res=st.selectbox(label='Select Restaurant',options=res_index)
df_selected=df[df.loc[:,'Restaurant Name']==selected_res]
df_selected=df_selected.sort_values(by='Votes',ascending=False)
st.write(df_selected)

ch=px.bar(df_selected[:20],x='Item Name',y='Votes',color="City")
st.plotly_chart(ch)

ch1=px.pie(df_selected[:20],names='Item Name',values='Votes')
st.plotly_chart(ch1)

ch2=px.pie(df_selected[:10],names='Item Name',values='Prices')
st.plotly_chart(ch2)

