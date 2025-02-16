# LangChain AI Applications

This repository contains various AI applications built using LangChain, demonstrating different capabilities like chatbots, RAG (Retrieval Augmented Generation), agents, and API integrations.

## Features

### 1. Agents
- Implements intelligent agents using LangChain
- Integrates with Wikipedia, arXiv, and custom knowledge bases
- Uses OpenAI's GPT models for processing
- Located in `agents/`

### 2. API Integration
- FastAPI-based server for language model serving
- Supports both OpenAI and Ollama models
- Streamlit client for user interface
- Located in `api/`

### 3. Chatbots
- OpenAI-powered chatbot implementation
- Local LLaMA model integration
- Streamlit-based user interface
- Located in `chatbot/`

### 4. Groq Integration
- High-performance Groq model integration
- Document retrieval and QA capabilities
- Vector store implementation with FAISS
- Located in `groq/`

### 5. RAG (Retrieval Augmented Generation)
- Document loading and processing
- Vector store implementations (FAISS, Chroma)
- Question-answering system
- Located in `rag/`

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd langchain-applications
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
```

## Usage

### Running the API Server
```bash
cd api
python app.py
```

### Running the Chatbot
```bash
cd chatbot
python app.py
```

### Running the Groq Application
```bash
cd groq
python app.py
```

### Using the Agents
```bash
cd agents
python agents.py
```

### Using RAG
Open and run the Jupyter notebook:
```bash
cd rag
jupyter notebook rag.ipynb
```

## Requirements

- Python 3.8+
- LangChain
- OpenAI
- Groq
- FastAPI
- Streamlit
- FAISS
- Other dependencies listed in `requirements.txt`


