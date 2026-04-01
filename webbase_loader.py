from langchain_community.document_loaders import WebBaseLoader
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

url = "https://en.wikipedia.org/wiki/Questions_and_Answers_(Sham_69_song)"

loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs[0]))
# print(docs[0].page_content)

prompt = PromptTemplate(
    template='Answer the question {question} \n of the following text -->\n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question': 'who is the producers of this song?', 'text': docs[0].page_content})
print(result)