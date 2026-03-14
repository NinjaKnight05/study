from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model='phi3:mini',temprature=1.5)

memory=[]

while True:
    a=input("Enter Something : ")
    # memory.append(a)
    if a.lower() in ['exit','quit']:
        print('exit sucess')
        # print(memory)
        break
        
    else:
        res = llm.invoke(a)
        # memory.append(res)
        print(res.content)
