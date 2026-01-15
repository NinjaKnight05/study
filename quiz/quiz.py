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

elif menu=='Play':
    st.subheader('Test')
    if not st.session_state.data:
        st.info('No Data Availaible')
    else:
        for i,j in enumerate(st.session_state.data):
            st.session_state.data[i][0]
            a=st.radio('',st.session_state.data[i][1:5])
            if st.button(label='Submit'):
             if a in st.session_state.ans:
                st.write('Correct')
             else:
                st.write('Wrong')
            
# import streamlit as st

# if 'data' not in st.session_state:
#     st.session_state.data = []  
# if 'ans' not in st.session_state:
#     st.session_state.ans = []   ;

# st.set_page_config(page_title="Quiz App", page_icon="🤓", layout="centered")
# st.title("📚 Quiz Management System")

# menu = st.sidebar.radio(
#     "Choose an option",
#     ["Create Quiz", "List Quiz", "Play Quiz", "Update Quiz", "Delete Quiz"]
# )

# if menu == "Create Quiz":
#     st.subheader("Create a New Question")

#     question = st.text_input("Question")
#     opt1 = st.text_input("Option 1",placeholder='.....')
#     opt2 = st.text_input("Option 2",placeholder='.....')
#     opt3 = st.text_input("Option 3",placeholder='.....')
#     opt4 = st.text_input("Option 4",placeholder='.....')
#     answer = st.selectbox("Correct Answer", [opt1, opt2, opt3, opt4])

#     if st.button("Add Question"):
#         if all([question, opt1, opt2, opt3, opt4]):
#             st.session_state.data.append([question, opt1, opt2, opt3, opt4])
#             st.session_state.ans.append(answer)
#             st.success("Question added successfully")
#         else:
#             st.error("All fields are required")

# elif menu == "List Quiz":
#     st.subheader("All Questions")

#     if not st.session_state.data:
#         st.info("No quiz available")
#     else:
#         for i, q in enumerate(st.session_state.data):
#             st.write(f"**{i+1}. {q[0]}**")
#             for j in range(1, 5):
#                 st.write(f"{j}. {q[j]}")
#             st.markdown("---")

# elif menu == "Play Quiz":
#     st.subheader("Play Quiz")

#     if not st.session_state.data:
#         st.warning("No quiz available")
#     else:
#         score = 0
#         for i, q in enumerate(st.session_state.data):
#             st.write(f"**Q{i+1}. {q[0]}**")
#             choice = st.radio(
#                 "Choose an option",
#                 [1, 2, 3, 4],
#                 format_func=lambda x: q[x],
#                 key=f"q{i}"
#             )
#             if st.session_state.ans[i] == choice:
#                 score += 1
#         if st.button("Submit Quiz"):
#             st.success(f"Your Score: {score}/{len(st.session_state.data)}")


# elif menu == "Update Quiz":
#     st.subheader("Update Question / Option")

#     if not st.session_state.data:
#         st.warning("No quiz available")
#     else:
#         q_index = st.number_input("Question Number", 1, len(st.session_state.data)) - 1
#         field = st.selectbox("What to update?", ["Question", "Option 1", "Option 2", "Option 3", "Option 4"])
#         new_value = st.text_input("New Value")

#         if st.button("Update"):
#             idx_map = {"Question": 0, "Option 1": 1, "Option 2": 2, "Option 3": 3, "Option 4": 4}
#             if new_value:
#                 st.session_state.data[q_index][idx_map[field]] = new_value
#                 st.success("Updated successfully")
#             else:
#                 st.error("Value cannot be empty")

# elif menu == "Delete Quiz":
#     st.subheader("Delete Question")

#     if not st.session_state.data:
#         st.warning("No quiz available")
#     else:
#         d_index = st.number_input("Question Number to Delete", 1, len(st.session_state.data)) - 1
#         if st.button("Delete"):
#             st.session_state.data.pop(d_index)
#             st.session_state.ans.pop(d_index)
#             st.success("Question deleted successfully")
