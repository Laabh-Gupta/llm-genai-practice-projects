from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import asyncio
from langchain_community.document_loaders.sitemap import SitemapLoader




#Function to fetch data from website
# https://python.langchain.com/docs/integrations/document_loaders/sitemap/
# here we are passing a limit value of 5 so that we dont end up getting every link as its just a demo project
def get_website_data(sitemap_url, limit=5):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loader = SitemapLoader(
    sitemap_url
    )

    docs = loader.load()

    return docs[:limit]

#Function to split data into smaller chunks
def split_data(docs):

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
    )

    docs_chunks = text_splitter.split_documents(docs)
    return docs_chunks

#Function to create embeddings instance
def create_embeddings():

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#Function to push data to Pinecone
def push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,docs):

    Pinecone(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name
    #PineconeStore is an alias name of Pinecone class, please look at the imports section at the top :)
    index =  PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
    return index

#Function to pull index data from Pinecone
def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):

    Pinecone(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name
    #PineconeStore is an alias name of Pinecone class, please look at the imports section at the top :)
    index = PineconeVectorStore.from_existing_index(index_name, embeddings)
    return index

#This function will help us in fetching the top relevent documents from our vector store - Pinecone Index
def get_similar_docs(index,query,k=2):

    similar_docs = index.similarity_search(query, k=k)
    return similar_docs


