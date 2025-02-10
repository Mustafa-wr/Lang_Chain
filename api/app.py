from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
    title="langchain",
    description="A language model serving API",
    version="1.0",
)

openai_model = ChatOpenAI()
llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_template("write a simple story about {topic}")
prompt2 = ChatPromptTemplate.from_template("write a simple poem about {topic}")

add_routes(app, prompt | openai_model, path="/story")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
