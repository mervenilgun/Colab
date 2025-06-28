# pip install langchain langchain-community langchain-openai python-dotenv google-search-results

from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle (.env dosyasından)
load_dotenv()

# LLM ayarı (OpenAI GPT-3.5 veya GPT-4)
llm = ChatOpenAI(temperature=0.7)

# SERP API aracı yükleniyor
tools = load_tools(["serpapi"], llm=llm)

# Sistem mesajı
system_message = SystemMessage(content="Sen Türkçe konuşan, akıllı bir asistansın. Cevaplarını Türkçe ver.")

# Agent oluşturuluyor: STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={"system_message": system_message}
)

# Soru soruluyor
soru = "Türkiye'nin 2023 yapay zeka çalışmaları hakkında Türkçe bilgi verir misin?"
cevap = agent.invoke({"input": soru})

# Sadece çıktıyı yazdır
print("📌 Cevap:", cevap["output"])
