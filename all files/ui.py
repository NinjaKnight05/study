import streamlit as st
import re


st.set_page_config(page_title='My Site',page_icon='🗡️')


with st.sidebar:
    menu=st.radio('Menu',options=['Home','About','Contact','Form-Fill'])
if menu=='Form-Fill':
    
   st.title('Form Submission 👻')
   st.subheader('Fill Here‼️')

   with st.form(key='key'):
        col1,col2=st.columns(2)
        with col1:
         name= st.text_input('Name',max_chars=20,placeholder='Enter Your Name......')
         password=st.text_input('Password',type='password',placeholder='password')
         gender=st.radio('Gender',options=['Male','Female','Others'],horizontal=True)
      
        with col2:
          age=st.number_input('Age',min_value=10)
          state=st.selectbox('State',options=['Punjab','Hp','Mp','Up','Haryana'])
          hoobies=st.multiselect("Hobbies",options=['Coding','Music','Dance','Games','Adventure'])
          st.write('☠️')
        condition=st.checkbox('Terms and Conditions')
        btn=st.form_submit_button('Submit')

elif menu=='Contact':
    with st.form(key='contact'):
       st.title("Contact US 😂")
       name1=st.text_input('Name',max_chars=10,placeholder='Name......')
       email=st.text_input('Email',icon='✉️',placeholder='Your Mail.....')
       phone = st.text_input("Phone Number", placeholder="+91 123-456-7890")
       message=st.text_area('Message',placeholder='Write Your Message.......')
       btn1=st.form_submit_button('Send')
elif menu=='About':
   st.title('About Us 💀')
   st.subheader('Some Good Points')
   st.write('Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.Welcome to our platform! We are commiExplor reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.')
   st.subheader('Some Bad points')
   st.write('Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. Explore our features, connect with others, and enjoy everything we have to offer.Welcome to our platform! We are committed to providing the best experience for our users. Our team works hard to ensure quality, reliability, and fun. ')
else:
   st.title('Welcome To Our Site')
   st.image('https://images.hdqwalls.com/wallpapers/cars-3-animated-movie-hd.jpg')

   
