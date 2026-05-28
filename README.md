# 🚀 Overview:

This project leverages the CrewAI framework to orchestrate specialized AI agents that execute a sequential financial analysis workflow. The backend is powered by FastAPI, with a user-friendly Streamlit frontend. To ensure production readiness, the system integrates with Azure Cloud for data persistence and artifact storage, and utilizes LangSmith for deep execution tracing.  

# 🧠 The AI Crew Architecture:
The system utilizes a separation-of-concerns architecture, assigning distinct roles and tools to specialized agents:

### 1. The Quantitative Analyst
A math-driven agent that evaluates companies strictly on hard data, balance sheets, earnings growth, and volatility. It ignores market hype and focuses purely on rigorous valuation metrics.  Tools: yfinance integration.  Capabilities: Fetches fundamental metrics (P/E, EPS, Beta, Market Cap) and calculates relative historical performance against the S&P 500 (SPY).  

### 2. The Chief Investment StrategistA qualitative agent that synthesizes the quantitative numbers with broader market sentiment.  
Tools: Firecrawl semantic web scraping.  
Capabilities: Scrapes the full markdown content of recent news and analyst ratings to understand the market "narrative". It synthesizes this narrative with the Quant's hard numbers to formulate a final, reasoned 'Buy', 'Sell', or 'Hold' recommendation.  

## 🛠️ Tech Stack AI Orchestration: 
CrewAI, LangChain, LangSmithBackend: FastAPI, Python (managed via uv)Frontend: StreamlitData Sources: Yahoo Finance API (yfinance), Firecrawl APICloud Infrastructure: Azure Blob Storage (Document Artifacts), Azure PostgreSQL (Structured Metadata)

## ⚙️ Installation & Setup: 
To run this system locally, you will need to set up the environment and run both the FastAPI backend and the Streamlit frontend.1. Clone the Repository:

`git clone https://github.com/YourUsername/Multi-Agent-Financial-Analyzer.git`

`cd Multi-Agent-Financial-Analyzer`

# 2. Environment Configuration
Create a .env file in the root directory and add the following required API keys and connection strings:

### AI Models
OPENAI_API_KEY=your_openai_api_key

### Tools
FIRECRAWL_API_KEY=your_firecrawl_api_key

### Cloud Storage & Database
AZURE_BLOB_CONNECTION_STRING=your_azure_blob_string
AZURE_POSTGRES_URL=your_postgres_connection_url

### Tracing (Optional but recommended)
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_PROJECT=Multi-Agents

### 3. Run the Application
It is recommended to use uv for fast dependency management and execution. You will need two terminal windows.

uv run uvicorn src.api.main:app --reload

uv run streamlit run frontend/app.py
