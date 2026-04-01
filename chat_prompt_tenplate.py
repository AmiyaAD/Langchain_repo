from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system','You are a help-full {domain} expart'),
    ('human', 'Explain in simple terms, what is  {topic}')
    # SystemMessage(content="You are a help-full {domain} expart"),
    # HumanMessage(content="Tell me about whit is {topic}")
])

prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic': 'tell'
})

print(prompt)