# pip install -U langchain langchain-openai langchain-community google-search-results python-dotenv

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import SerpAPIWrapper
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# .env içinden anahtarları yükle
load_dotenv()

# OpenAI LLM ayarı
llm = ChatOpenAI(temperature=0.7)

# SerpAPI Wrapper
search = SerpAPIWrapper()  # Burada API key env dosyasından çekilir

# Agent için gerekli tool
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="Kısa ve gerçek bilgi aramak için kullanılır."
    )
]

# SELF_ASK_WITH_SEARCH Agent oluştur
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.SELF_ASK_WITH_SEARCH,
    verbose=True
)

# Soru
soru = "Boğaziçi Üniversitesi hangi şehirde ve kaç yılında kuruldu?"
cevap = agent.run(soru)

print("📌 Cevap:", cevap)
