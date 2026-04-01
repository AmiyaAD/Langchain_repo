from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
import os

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm=HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5",
    task="text-generation",
    huggingfacehub_api_token=hf_token

)

# llm = HuggingFacePipeline(
#     model_id="zai-org/GLM-5",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         temperature = 0.5,
#         max_new_tokens=100
#     )
# )
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of india")

print(result.content)