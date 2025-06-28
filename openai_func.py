from langchain.agents import initialize_agent, AgentType
from langchain.tools import StructuredTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Ortam değişkenlerini yükle (.env dosyasından OPENAI_API_KEY alınır)
load_dotenv()

# LLM tanımı (GPT-4 fonksiyon çağrısı destekli sürüm)
llm = ChatOpenAI(model="gpt-4-0613", temperature=0.7)

# Fonksiyon: Şehir ismine göre hava durumu döner
def get_weather(city: str) -> dict:
    city = city.strip().lower()
    if city in ["istanbul", "i̇stanbul"]:
        return {
            "temperature": 25,
            "condition": "parçalı bulutlu",
            "city": "İstanbul"
        }
    else:
        return {
            "temperature": None,
            "condition": None,
            "city": city.title()
        }

# Fonksiyonu LangChain aracı haline getir (StructuredTool ile!)
weather_tool = StructuredTool.from_function(
    name="get_current_weather",
    description="Bir şehir ismi girildiğinde o şehirdeki güncel hava durumunu döner.",
    func=get_weather
)

# Agent oluştur (OpenAI Functions agent tipi ile)
agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Kullanıcı sorusu
soru = "Bugün İstanbul'da hava nasıl?"
cevap = agent.run(soru)

print("📌 Cevap:", cevap)
