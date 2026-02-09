import streamlit as st
import joblib
import pickle
from streamlit_option_menu import option_menu

st.set_page_config(page_title='CarPredictor', page_icon='🏎️')

menu = option_menu(
    menu_title='',
    options=['Home', 'Prediction', 'Analysis'],
    icons=['house', 'speedometer', 'graph-up'],
    orientation='horizontal'
)

# ================= LOAD MODELS =================
model = joblib.load('car_model.joblib')
fuelmod = pickle.load(open('fuel.pkl', 'rb'))
ownmod = pickle.load(open('own.pkl', 'rb'))
transmod = pickle.load(open('trans.pkl', 'rb'))

# ================= HOME =================
if menu == 'Home':
    st.title('𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗣𝗥𝗜𝗖𝗘 𝗘𝗦𝗧𝗜𝗠𝗔𝗧𝗢𝗥')
    st.image(
        'https://images.pexels.com/photos/70912/pexels-photo-70912.jpeg',
        use_container_width=True
    )

    st.subheader("Get an instant ML-based estimate of your car’s resale value.")

    st.markdown("""
### 📘 About
This app predicts **used car prices** using a Machine Learning model trained on historical data.

### 📊 Factors
- Car age  
- Present price  
- Kilometers driven  
- Fuel type  
- Transmission  
- Owner count  

⚠️ Predictions are valid **only within training data limits**.
""")

# ================= PREDICTION =================
elif menu == 'Prediction':

    st.subheader("Enter Car Details")

    car_age = st.number_input('𝗖𝗔𝗥 𝗔𝗚𝗘 ⏳', 1, 20, 2)
    present_price = st.number_input('𝗣𝗥𝗘𝗦𝗘𝗡𝗧 𝗣𝗥𝗜𝗖𝗘 (₹ Lakhs) 💰', 0.0, 25.0, 5.0)
    kms_driven = st.number_input('𝗞𝗠𝗦 𝗗𝗥𝗜𝗩𝗘𝗡 📏', 0, 500000, 5000)

    fuel = st.selectbox('𝗙𝗨𝗘𝗟 ⛽', fuelmod.classes_)
    fuel_enc = fuelmod.transform([fuel])[0]

    owner = st.selectbox('𝗢𝗪𝗡𝗘𝗥 𝗖𝗢𝗨𝗡𝗧 🧑‍💼', ownmod.classes_)
    owner_enc = ownmod.transform([owner])[0]

    trans = st.selectbox('𝗧𝗥𝗔𝗡𝗦𝗠𝗜𝗦𝗦𝗜𝗢𝗡 ⚙️', transmod.classes_)
    trans_enc = transmod.transform([trans])[0]

    # 🔴 MUST MATCH TRAINING FEATURE ORDER
    model_input = [
        present_price,   # Present_Price
        kms_driven,      # Kms_Driven
        owner_enc,       # Owner
        fuel_enc,        # Fuel
        trans_enc,       # Transmission
        car_age          # Car_Age
    ]

    st.write("🔍 Model Input:", model_input)

    if st.button('Predict Price'):
        prediction = model.predict([model_input])[0]
        st.success(f"💰 Estimated Resale Price: ₹ {prediction:.2f} Lakhs")

# ================= ANALYSIS =================
else:
    st.title('Analysis')
    st.info('Add charts, feature importance, or dataset insights here.')
