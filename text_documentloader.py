from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence,RunnableLambda, RunnableBranch
import os
load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)


model = ChatHuggingFace(llm = llm1)

prompt1 = PromptTemplate(
    template='Write a summary for the following poem --> \n {text}',
    input_variables=['text']
)


parser = StrOutputParser()

loader = TextLoader(r"Documents_loader\poem.txt")

docs = loader.load()
print(len(docs))
print(type(docs))
# print(len(docs[0]))
print(type(docs[0]))
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt1 | model | parser

print(chain.invoke({'text': docs[0].page_content}))