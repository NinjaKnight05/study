import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import base64 

st.set_page_config(page_title='Corn site',page_icon="🌽")
menu= option_menu(menu_title='', options=['Home','Contact','Analysis'], icons=['house-fill','phone-fill','book-fill','info-square-fill'], orientation='horizontal')

if menu=="Home":
    st.title('About Us')
    st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

    col1,col2=st.columns(2)
    with col1:
         st.subheader('Images')
         st.image("https://png.pngtree.com/thumb_back/fw800/background/20240913/pngtree-group-of-farmers-working-together-in-a-lettuce-field-tending-to-image_16188070.jpg")
         st.image("https://www.afgri.com.au/pub/media/strongready-r4a052760.jpg")
      
    with col2:
          st.subheader('Royal-In-Field')
          st.image("https://www.openaccessgovernment.org/wp-content/uploads/2021/02/dreamstime_xxl_183417536.jpg")
          st.image("https://c.files.bbci.co.uk/910A/production/_106203173_farmer1.jpg")

elif menu=='Analysis':
     with open('lst.jpg','rb') as f:
      file=f.read()
      img= base64.b64encode(file).decode()
     css=f"""
          <style>
           [data-testid="stAppViewContainer"]{{
            background-image:url('data:image/jpg;base64,{img}');
            background-size:cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
       """
     st.markdown(css, unsafe_allow_html=True)
     st.title('ALL STATES 2026 CROPS SALES🌾')
     st.subheader('Analysis🧠')
     df=pd.read_csv('market.csv')

     st.write(df)
     # res_index=df.loc[:,"Restaurant Name"].value_counts().index
     # st.write(res_index)

     # with st.sidebar:
     #  selected_res=st.selectbox(label='Select Restaurant',options=res_index)
     #  df_selected=df[df.loc[:,'Restaurant Name']==selected_res]
     #  df_selected=df_selected.sort_values(by='Votes',ascending=False)
     #  st.write(df_selected)
elif menu=='contact':
    pass


