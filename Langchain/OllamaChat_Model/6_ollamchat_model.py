from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model='phi3:mini')

while True:
    a=input("Enter your query: ")
    if a.lower() in ['exit', 'quit']:
        print("Exiting the bot")
        break
    else:
        result = llm.invoke(a)
        print(result.content)

