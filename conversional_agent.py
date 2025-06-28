# pip install -U langchain langchain-openai langchain-community python-dotenv google-search-results

from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# .env dosyasından API anahtarlarını yükle
load_dotenv()

# LLM tanımı
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# SerpAPI aracını yükle
tools = load_tools(["serpapi"], llm=llm)

# Konuşma geçmişini hatırlayan bellek
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Chat Conversational Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Diyalog
soru1 = "Fransa nerede?"
cevap1 = agent.run(soru1)
print("🧠 Cevap 1:", cevap1)

soru2 = "Başkentinde ne meşhur?"
cevap2 = agent.run(soru2)
print("🧠 Cevap 2:", cevap2)

soru3 = "Oraya gitmek için vize gerekiyor mu?"
cevap3 = agent.run(soru3)
print("🧠 Cevap 3:", cevap3)
