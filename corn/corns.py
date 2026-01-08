import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64 

st.set_page_config(page_title='Corn site',page_icon="🌽")
menu= option_menu(menu_title='', options=['Home','Analysis','Contact'], icons=['house-fill','info-square-fill','phone-fill','book-fill'], orientation='horizontal')

if menu=='Home':
    st.title('Reliable Crop Supply for Retailers & Bulk Buyers')
    video="https://www.pexels.com/download/video/1649831/"
    components.html( 
        f"""
        <video autoplay muted loop playsline width="100%">
            <source src="{video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """,
        height=400,
     )
    st.write('Lorem Ipsm is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
    st.title('-------------About Farmers--------------')
    col1,col2=st.columns(2)
    with col1:
     st.subheader("")
     st.image("https://www.openaccessgovernment.org/wp-content/uploads/2021/02/dreamstime_xxl_183417536.jpg")
    with col2:
        
        st.subheader("")
        st.write("A farmer is a person r older definitions a farmer was a person who promotes or improves the growth of plants is usually a farm owner (landowner)her older definitions a farmer was a person who promotes or improves the growth of plants, land, or crops or raises animals (as livestock or fish) by labor and attention.ion.")

    st.title('< < < < Facts > > > > ')   
    col1,col2=st.columns(2)
    with col1:
       st.subheader('wheat')
       st.write('Wheat is one of the oldest and most important cereal crops, providing essential nutrients and serving as a staple food for billions worldwide.')
       st.write('Wheat is a stout grass of medium to tall height. Its stem is jointed and usually hollow, forming a straw. There can be many stems on one plant. It has long narrow leaves, their bases sheathing the stem, one above each joint. At the top of the stem is the flower head, containing some 20 to 100 flowers.')
       
       st.subheader('')
       st.image('https://tse4.mm.bing.net/th/id/OIP.bG8LtZ9zce2tUXH9PAJqRgHaFi?rs=1&pid=ImgDetMain&o=7&rm=3')

       st.subheader('')
       st.write('Nutritional Powerhouse: Black sesame seeds are rich in calcium, iron, magnesium, zinc, and copper, which are crucial for bone health and immune support. Heart Health: The healthy fats in black sesame seeds, including monounsaturated and polyunsaturated fats, can help reduce LDL cholesterol levels and lower the risk of heart disease and stroke. Antioxidant Properties: These seeds contain antioxidants like sesamin, sesamol, and lignans, which protect cells from oxidative damage and reduce the risk of chronic diseases')

       st.subheader('')
       st.image('https://i0.wp.com/herbaria3.org/wp-content/uploads/2021/03/iiif-service_asian_lcnclscd_2014514379_1A001_05b06a-3390x490x2997x3735-866x-0-default.jpg?w=866&ssl=1')
      
    with col2:
       st.title('')
       st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Trilla_del_trigo_en_el_Antiguo_Egipto.jpg/330px-Trilla_del_trigo_en_el_Antiguo_Egipto.jpg")
       
       st.subheader('')
       st.subheader('Corn')
       st.write('Maize (/meɪz/; Zea mays), also known as corn in North American English, is a tall stout grass that produces cereal grain. The leafy stalk of the plant gives rise to male inflorescences or tassels which produce pollen, and female inflorescences called ears')

       st.title('')
       st.subheader('Black Sesame Seeds')
       st.image('https://tse4.mm.bing.net/th/id/OIP.83ivqHWarTmNe0juipvlEQHaFo?w=800&h=608&rs=1&pid=ImgDetMain&o=7&rm=3')

       st.write('')
       st.subheader('Rice')
       st.write('Staple Food: Rice is a primary food source for more than 3.5 billion people, especially in Asia, where it forms the basis of many traditional dishes. It provides essential carbohydrates and energy. Nutritional Value: Brown rice is more nutritious than white rice, retaining its bran and germ, which provide fiber, vitamins, and minerals. Rice is naturally gluten-free, making it suitable for those with gluten intolerance.')

    
    st.title('History') 
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/KITLV_40091_-_Kassian_C%C3%A9phas_-_Relief_of_the_hidden_base_of_Borobudur_-_1890-1891.jpg/600px-KITLV_40091_-_Kassian_C%C3%A9phas_-_Relief_of_the_hidden_base_of_Borobudur_-_1890-1891.jpg')

    
    col3,col4=st.columns(2)
    with col3:
       st.write('')
       st.write('Agriculture began independently in different parts of the globe, and included a diverse range of taxa. At least eleven separate regions of the Old and New World were involved as independent centers of origin. The development of agriculture about 12,000 years ago changed the way humans lived. They switched from nomadic hunter-gatherer lifestyles to permanent settlements and farming Wild grains were collected and eaten from at least 104,000 years ago. However, domestication did not occur until much later. The earliest evidence of small-scale cultivation of edible grasses is from around 21,000 BC with the Ohalo II people on the shores of the Sea of Galilee. By around 9500 BC, the eight Neolithic founder crops – emmer wheat, einkorn wheat, hulled barley, peas, lentils, bitter vetch, chickpeas, and flax – were cultivated in the Levant.[4] Rye may have been cultivated earlier, but this claim remains controversial.')

    with col4:
       st.title('')
       st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Maler_der_Grabkammer_des_Sennudem_001.jpg/960px-Maler_der_Grabkammer_des_Sennudem_001.jpg')

    st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 100;
    }
    </style>

    <div class="footer">
        © 2026 Coder Roots | Built with Tobi
    </div>
    """,
    unsafe_allow_html=True
)

elif menu=='Analysis':
     
     st.title('ALL STATES 2026 CROPS SALES🌾')
     st.subheader('Analysis🧠')
     df=pd.read_csv('corn.csv')
     df.columns=df.columns.str.strip()

     st.write(df)
     # show=df["Commodity Group"].unique()
     # st.write(show)
     # res_index=df.loc[:,"Commodity Group"].value_counts().index

     with st.sidebar:
       selected_res = st.selectbox('Select', options=df['Commodity Group'].unique())
       df_selected = df[df['Commodity Group'] == selected_res]
     
     # st.write(df_selected1)
     st.subheader('3D View Of Stocks')
     chart1=px.scatter_3d(df_selected,x='Commodity',y='Quantity',z='Commodity Group',color="Commodity")
     st.plotly_chart(chart1)
     
     st.write(df_selected)
     
     st.subheader('Total Stock in Cold-Store')
     chart0=px.pie(df,names='Commodity',values='Quantity')
     st.plotly_chart(chart0)

     st.subheader('Price Of Corps On 1 Jan 2026')
     chart2=px.bar(df_selected,x="Commodity",y="Price 0",color='Arrived Material 1')
     st.plotly_chart(chart2)

     st.subheader('Price Of Corps On 2 Jan 2026')
     chart4=px.bar(df_selected,x="Commodity",y="Price 1",color="Arrival Material 2")
     st.plotly_chart(chart4)

     st.subheader('Price Of Corps On 3 Jan 2026')
     chart5=px.bar(df_selected,x='Commodity',y='Price 2',color="Arrival Material 3" )
     st.plotly_chart(chart5)
     
     st.subheader('New Arrived Material')
     chart3=px.line(df_selected,x="Commodity",y="Total Arrival")
     st.plotly_chart(chart3)

     
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

elif menu=='Contact':
    with st.form(key='contact'):
       st.title("CONTACT US👾")
       name1=st.text_input('Name',max_chars=10,placeholder='Name......')
       email=st.text_input('Email',icon='✉️',placeholder='Your Mail.....')
       phone = st.text_input("Phone Number", placeholder="+91 ------")
       message=st.text_area('Message',placeholder='Write Your Message.......')
       btn1=st.form_submit_button('Send')


