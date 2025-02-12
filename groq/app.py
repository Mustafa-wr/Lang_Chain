import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retriever_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
import os
from langchain_core.prompts import ChatPromptTemplate
import time
from langchain_community.embeddings import OllamaEmbeddings

from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

if "vector" not in st.session_state:
	st.session_state.embeddings=OllamaEmbeddings()
	st.session_state.loader("https://docs.smith.langchain.com/")
	st.session_state.docs=st.session_state.loader.load()
	st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
	st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
	st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)


st.title("LangChain Documentation Chatbot")
llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama3-8b-8192",temperature=0)
prompt=ChatPromptTemplate.from_template("""
You are a helpful assistant that can answer questions about the LangChain documentation.
<context>
{context}
</context>

Question: {question}

""")
document_chain=create_stuff_documents_chain(llm,prompt)
retriever=st.session_state.vectors.as_retriever()

retriever_chain=create_retriever_chain(retriever,document_chain)

prompt=st.text_input("Enter your question:")


if prompt:
	start_time=time.time()
	response=retriever_chain.invoke({"input":prompt})
	print(f"Time taken: {time.time()-start_time} seconds")
	st.write(response["answer"])

	with st.expander("Document Similarity Search"):
		for i, doc in enumerate(response["context"]):
			st.write(doc.page_content)
			st.write("--------------------------------")


