from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create template

chat_tempale = ChatPromptTemplate([
    ('system', 'You are a helpfull sustomer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])
# load chat history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)    

# create prompt

prompt = chat_tempale.invoke({'chat_history': chat_history, 'query': 'where is my refund'})

print(prompt)