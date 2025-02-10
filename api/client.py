import requests
import streamlit as st

def get_openai_response(prompt):
	response=respomse.post(
		"http://localhost:8000/story/invoke",
		json={"input":{'topic':input_text}}
	)
	return response.json()['output']['content']

def get_ollama_response(prompt):
	response=respomse.post(
		"http://localhost:8000/poem/invoke",
		json={"input":{'topic':input_text}}
	)
	return response.json()['output']

st.title("langchain")
input_text = st.text_input("write a story")
input_text2 = st.text_input("write a poem")

if input_text:
	st.write(get_openai_response(input_text))

if input_text2:
	st.write(get_ollama_response(input_text2))