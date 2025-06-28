from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Ortam değişkenlerini yükle (.env dosyasından API key alınır)
load_dotenv()

# GPT-4 veya GPT-3.5 tanımı
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# Hafıza sistemi
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

print("\n🧠 Asistan başlatıldı. Çıkmak için 'çık' yazın.\n")

while True:
    user_input = input("👤 Soru: ")
    if user_input.lower() in ["çık", "exit", "quit"]:
        print("🛑 Asistan kapatıldı.")
        break

    # Geçmişi al
    history = memory.load_memory_variables({})["chat_history"]
    formatted_history = "\n".join([f"{m.type.capitalize()}: {m.content}" for m in history])

    # Model için özel prompt
    full_prompt = (
        f"Aşağıda bir kullanıcıyla önceki konuşmalar yer alıyor.\n"
        f"{formatted_history}\n\n"
        f"Kullanıcının yeni sorusu: {user_input}\n"
        f"Geçmiş konuşmalara uygun ve bağlamlı Türkçe bir cevap ver."
    )

    # LLM yanıtı
    try:
        response = llm.invoke(full_prompt)
        print("🤖 Cevap:", response.content, "\n")
        # Hafızaya ekle
        memory.chat_memory.add_user_message(user_input)
        memory.chat_memory.add_ai_message(response.content)
    except Exception as e:
        print("❌ Hata:", e)
