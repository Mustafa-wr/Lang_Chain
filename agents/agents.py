import os
from dotenv import load_dotenv
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor

load_dotenv()
assert os.getenv("OPENAI_API_KEY") is not None

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

loader = WebBaseLoader("https://docs.smith.langchain.com/")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
vectordb = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vectordb.as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "search for information about langsmith for any question about LangSmith use this tool"
)

tools = [wiki, arxiv, retriever_tool]

llm = ChatOpenAI(model="gpt-4", temperature=0)  # Changed from gpt-4o-mini to gpt-4

# Get prompt from hub
prompt = hub.pull("hwchase17/openai-functions-agent")

# Create agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Setup agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    result = agent_executor.invoke({"input": "What is the latest news on LangSmith?"})
    print(result)

if __name__ == "__main__":
    main() 