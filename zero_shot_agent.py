# pip install -U langchain langchain-community langchain-openai google-search-results python-dotenv
#https://serpapi.com/manage-api-key
from langchain.agents import initialize_agent # type: ignore
from langchain_community.agent_toolkits.load_tools import load_tools # type: ignore
from langchain.agents.agent_types import AgentType # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langchain_core.messages import SystemMessage # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Ortam değişkenlerini yükle
load_dotenv()

# OpenAI LLM
llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4",  # veya "gpt-3.5-turbo"
)

# SerpAPI aracını LLM'e bağlı şekilde yükle
tools = load_tools(["serpapi"], llm=llm)

# Türkçe sistem mesajı
system_message = SystemMessage(
    content="Sen Türkçe konuşan, akıllı bir yapay zekâ asistanısın. Cevaplarını daima Türkçe ver. Bilgi ararken mümkün olduğunca Türkçe kaynaklara öncelik ver."
)

# Agent yapılandırması
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={"system_message": system_message}
)

# 🧪 Soru
soru = "Türkiye hakkında bilgi ver"

# ✅ Yeni tavsiye edilen çağırma yöntemi
cevap = agent.invoke(soru)

print("\n🧠 Cevap:", cevap)
print("\n🧠 Cevap:", cevap["output"])
