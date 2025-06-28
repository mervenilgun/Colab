"""
❌ DocstoreExplorer artık birçok LangChain sürümünde kaldırıldı veya experimental hale getirildi.
REACT_DOCSTORE agent türü ve ona bağlı DocstoreExplorer aracı:

LangChain 0.0.x – 0.1.0 arası sürümlerde vardı,

Ama 2024 ortası itibariyle deprecated (artık önerilmiyor),

Yeni langchain_community yapısında modül yolu değişti ya da tamamen kaldırıldı.
✅ Çözüm: Aynı işlevi WikipediaAPIWrapper + ZERO_SHOT_REACT_DESCRIPTION ile yap
"""


from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv
import os

# Ortam değişkenlerini yükle
load_dotenv()

# LLM modeli
llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

# Wikipedia wrapper (dil Türkçe olabilir)
wiki = WikipediaAPIWrapper(lang="tr")

# Tool olarak sar
tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Wikipedia üzerinden bilgi aramak için kullanılır"
    )
]

# Agent (ZERO_SHOT_REACT_DESCRIPTION ile REACT yapısı benzeri)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Soru sor
soru = "Türkiye'nin coğrafi bölgeleri nelerdir?"
cevap = agent.run(soru)

print("📌 Cevap:", cevap)
