from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

for documents in docs:
    print(documents.metadata)