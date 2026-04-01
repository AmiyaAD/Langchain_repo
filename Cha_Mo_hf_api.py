# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os

# # print(load_dotenv)
# load_dotenv()

# hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# print(hf_token)
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen3-Coder-Next",
#     task="text-generation",
#     huggingfacehub_api_token=hf_token
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of india")

# print(result.content)
# print("Hagging face chatmodel")
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Initialize Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-Next",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)
model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.title("LangChain + Hugging Face Chat")
user_input = st.text_input("Ask me something:")

if st.button("Submit"):
    if user_input:
        result = model.invoke(user_input)
        st.write("### Response:")
        st.write(result.content)
