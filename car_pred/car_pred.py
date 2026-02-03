import streamlit as st
import joblib
import sklearn
from streamlit_option_menu import option_menu
import base64
import plotly.express as px
import pickle
import streamlit.components.v1 as components

st.set_page_config(page_title='CarPredictor',page_icon='🏎️')

menu = option_menu(menu_title='',options=['Home','Prediction','Analysis'],icons=['list-ul','bar-chart-fill','graph-up-arrow'],orientation='horizontal')

model = joblib.load('car_model.joblib')
fuelmod=pickle.load(open('fuel.pkl','rb'))
ownmod = pickle.load(open('own.pkl','rb'))
transmod = pickle.load(open('trans.pkl','rb'))



if menu=='Home':
   st.title('𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗣𝗥𝗜𝗖𝗘 𝗘𝗦𝗧𝗜𝗠𝗔𝗧𝗢𝗥')
   st.image('https://images.pexels.com/photos/70912/pexels-photo-70912.jpeg?cs=srgb&dl=pexels-tdcat-70912.jpg&fm=jpg')

   st.subheader(
    "Get an instant, machine-learning–based estimate of your car’s resale value."
)


   st.markdown("""
## 📘 About

This **Car Price Prediction** application uses **Machine Learning** to estimate the resale value of a car based on key features such as car age, fuel type, transmission, kilometers driven, seller type, and owner count.

The model is trained on historical car sales data and is designed to provide quick, data-driven price estimates to help users make informed decisions.
               

""")
   st.markdown("""
### 📊 Factors affecting price
- Newer cars tend to have higher resale value  
- Lower mileage increases price  
- Fuel type and transmission impact demand  
- Fewer owners usually increase value
""")
   
   st.markdown("""
### 👥 Who can use this?
- Individuals planning to sell a used car  
- Buyers evaluating a fair market price  
- Learners exploring real-world ML applications
""")
   
   st.subheader("""⚠️ Important Note
Predictions are reliable only for inputs that fall within the range of the training data. Extreme or unrealistic values may produce inaccurate results.""")



elif menu=='Prediction':
    # st.subheader('ō͡≡o ✇⛟ ⚡︎⏲')
    i1=st.number_input('𝗖𝗔𝗥 𝗔𝗚𝗘 ⏳',min_value=1,max_value=20,value=2)
    i2=st.number_input('𝗣𝗥𝗘𝗦𝗘𝗡𝗧 𝗣𝗥𝗜𝗖𝗘 💰',min_value=0.0,max_value=25.00,value=5.0)
    i3= st.number_input('𝗞𝗠𝗦 𝗗𝗥𝗜𝗩𝗘𝗡 📏',min_value=0,value=5000)

    fuel= st.selectbox("𝗙𝗨𝗘𝗟 ⛽",fuelmod.classes_)
    fuell=fuelmod.transform([fuel])[0]

    own= st.selectbox("𝗢𝗪𝗡𝗘𝗥 𝗖𝗢𝗨𝗡𝗧 🧑‍💼",ownmod.classes_)
    # ownn=own.transform([own])[0]

    trans = st.selectbox("𝗧𝗥𝗔𝗡𝗦𝗠𝗜𝗦𝗦𝗜𝗢𝗡 ⚙️",transmod.classes_)
    transs=transmod.transform([trans])[0]



    st.session_state.pred=[i1,i2,i3,fuell,own,transs]


    btn1= st.button('Submit')
    if btn1:
     res = model.predict([st.session_state.pred])
     st.write(res)
     st.success('Done')

else:
    st.title('Analysis')
