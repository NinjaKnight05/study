import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Quiz',page_icon='📚')

st.title('Online Quiz 📚')

if 'data' not in st.session_state:
    st.session_state.data = [] 
if 'ans' not in st.session_state:
    st.session_state.ans = [] 

with st.sidebar:
    menu=st.radio('MENU📝',options=['Create','List','Play','Update','Delete'])
if menu=='Create':
        st.subheader('Question‼️')
        ques=st.text_input('',placeholder='Write here..')
        st.subheader('Options')
        q1=st.text_input('opt-1',placeholder='.....')
        q2=st.text_input('opt-2',placeholder='.....')
        q3=st.text_input('opt-3',placeholder='.....')
        q4=st.text_input('opt-4',placeholder='.....')
    
        ans=st.selectbox('Select Correct opt',options=[q1,q2,q3,q4])
        btn1=st.button('Submit')
        if btn1:
            if all([ques, q1, q2, q3, q4]):
             st.session_state.data.append([ques, q1, q2, q3, q4])
             st.session_state.ans.append(ans)
             st.success("Question added successfully")
            else:
              st.error("All fields are required")

elif menu=='List':
    st.subheader('Questions')
    if not st.session_state.data:
        st.info('No Data Availaible')
    else:
        for i,j in enumerate(st.session_state.data):
            st.write(i+1,j)
            st.markdown("---")
elif menu=='Update':
    st.subheader('Update Questions')
    if not st.session_state.data: 
        st.info('No Data Availaible')
    else:
        a= st.number_input("Enter number",min_value=1,max_value=len(st.session_state.data))
        opt= ['Question','opt 1', 'opt 2','opt 3','opt 4']
        option= st.selectbox('what you want to update',options=opt)
        b =st.text_input('New',placeholder='....')
        btn1=st.button('Submit') 
        if btn1:
         if option == opt[0]:
            st.session_state.data[a-1][0]=b
            st.success('Updated ')
         elif option==opt[1]:
           st.session_state.data[a-1][1]=b
           st.success('Updated ')
         elif option==opt[2]:
           st.session_state.data[a-1][2]=b
           st.success('Updated ')
         elif option==opt[3]:
           st.session_state.data[a-1][3]=b
           st.success('Updated ')
         elif option==opt[4]:
           st.session_state.data[a-1][4]=b
           st.success('Updated ')  
elif menu=='Delete':
        st.subheader('Update Questions')
        if not st.session_state.data:
            st.info('No Data Availaible')
        else:
            a= st.number_input("Enter number",min_value=1,max_value=len(st.session_state.data))
            btn1=st.button('Submit') 
            if btn1:
             st.session_state.data.pop(a-1)
             st.success('Deleted Sucessfully')

elif menu == 'Play':
    st.subheader('Play Quiz 🎯')

    if not st.session_state.data:
        st.info('No questions available')
    else:
        user_answers = []

        for i in range(len(st.session_state.data)):
            q = st.session_state.data[i]

            st.write(f"Q{i+1}. {q[0]}")

            ans = st.radio('',
                [q[1], q[2], q[3], q[4]],
                key=f"q{i}"
            )

            user_answers.append(ans)
            st.markdown("---")

        if st.button('Submit Quiz'):
            score = 0

            for i in range(len(user_answers)):
                if user_answers[i] == st.session_state.ans[i]:
                    score += 1

            st.success(f"Your Score: {score} / {len(user_answers)}")

        
    
    # elif menu == 'Play':
    # st.subheader('Play Quiz 🎮')
    # if not st.session_state.data:
    #     st.info('No questions available')
    # else:
    #     score = 0
    #     for i in range(len(st.session_state.data)):
    #         q = st.session_state.data[i]

    #         st.write(f"Q{i+1}. {q[0]}")

    #         user_answer = st.radio(
    #             'Choose an option:',
    #             [q[1], q[2], q[3], q[4]],
    #             key=i
    #         )
    #         if st.button(f"Check Q{i+1}"):
    #             if user_answer == st.session_state.ans[i]:
    #                 st.success("Correct ✅")
    #             else:
    #                 st.error("Wrong ❌")
 