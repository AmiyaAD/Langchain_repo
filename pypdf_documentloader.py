from langchain_community.document_loaders import PyPDFLoader, P

loader = PyPDFLoader("AI & ML DIGITAL NOTES.pdf")

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata) 