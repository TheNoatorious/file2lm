from dotenv import load_dotenv
from langchain.document_loaders import TextLoader

load_dotenv()

loader = TextLoader("./assets/facts.txt")
docs = loader.load() # Extract all content from the loader

print(docs) # Output of the docs

