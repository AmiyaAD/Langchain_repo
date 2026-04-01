from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"C:\Users\amiya\Downloads\Social_Network_Ads.csv")

docs = loader.load()
print(len(docs))
print(docs[0])
print(docs[10])