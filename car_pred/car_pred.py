import streamlit as st
import joblib
import sklearn
from streamlit_option_menu import option_menu
import base64
import plotly.express as px
import pickle

st.set_page_config(page_title='CarPredictor',page_icon='🏎️')

menu = option_menu(menu_title='',options=['Home','Prediction','Analysis'],icons=['list-ul','bar-chart-fill','graph-up-arrow'],orientation='horizontal')

model = joblib.load('car_model.joblib')
fuelmod=pickle.load(open('fuel.pkl','rb'))
sellmod = pickle.load(open('sell.pkl','rb'))
transmod = pickle.load(open('trans.pkl','rb'))



if menu=='Home':
    st.write('Home Page')

elif menu=='Prediction':
    # st.subheader('ō͡≡o ✇⛟ ⚡︎⏲')
    i1=st.number_input('𝗖𝗔𝗥 𝗔𝗚𝗘 ⏳',min_value=1,max_value=20,value=2)
    i2=st.number_input('𝗣𝗥𝗘𝗦𝗘𝗡𝗧 𝗣𝗥𝗜𝗖𝗘 💰',min_value=0.0,max_value=25.00,value=5.0)
    i3= st.number_input('𝗞𝗠𝗦 𝗗𝗥𝗜𝗩𝗘𝗡 📏',min_value=0,value=5000)

    fuel= st.selectbox("𝗙𝗨𝗘𝗟 ⛽",fuelmod.classes_)
    fuell=fuelmod.transform([fuel])[0]

    sell= st.selectbox("𝗦𝗘𝗟𝗟𝗘𝗥 🧑‍💼",sellmod.classes_)
    selll=sellmod.transform([sell])[0]

    trans = st.selectbox("𝗧𝗥𝗔𝗡𝗦𝗠𝗜𝗦𝗦𝗜𝗢𝗡 ⚙️",transmod.classes_)
    transs=transmod.transform([trans])[0]



    st.session_state.pred=[i1,i2,i3,fuell,selll,transs]


    btn1= st.button('Submit')
    if btn1:
     res = model.predict([st.session_state.pred])
     st.write(res)
     st.success('Done')












else:
    st.write('Analysis')