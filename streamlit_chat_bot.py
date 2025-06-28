# pip install streamlit langchain langchain-openai python-dotenv

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# LLM tanımı
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# Streamlit başlığı
st.set_page_config(page_title="Bağlamlı Chat Asistanı", layout="wide")
st.title("💬 Bağlamlı Yapay Zekâ Asistanı")

# SessionState içinde memory objesi oluştur
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

# Kullanıcıdan giriş al
user_input = st.text_input("👤 Sorunuzu yazın", placeholder="Örneğin: Fransa'nın başkenti nedir?", key="input")

# Gönder butonuna basıldığında çalışır
if st.button("Gönder") and user_input.strip():
    memory = st.session_state.memory

    # Geçmiş konuşmaları al ve biçimlendir
    history = memory.load_memory_variables({})["chat_history"]
    formatted_history = "\n".join([f"{m.type.capitalize()}: {m.content}" for m in history])

    # Model için özel prompt
    full_prompt = (
        f"Aşağıda bir kullanıcıyla önceki konuşmalar yer alıyor.\n"
        f"{formatted_history}\n\n"
        f"Kullanıcının yeni sorusu: {user_input}\n"
        f"Geçmiş konuşmalara uygun ve bağlamlı Türkçe bir cevap ver."
    )

    # Model cevabı
    try:
        response = llm.invoke(full_prompt)
        st.session_state.memory.chat_memory.add_user_message(user_input)
        st.session_state.memory.chat_memory.add_ai_message(response.content)

        # Son cevabı göster
        st.markdown(f"**🤖 Cevap:** {response.content}")

    except Exception as e:
        st.error(f"❌ Hata oluştu: {e}")

# Geçmiş sohbeti göster (isteğe bağlı)
with st.expander("🧠 Sohbet Geçmişi"):
    for msg in st.session_state.memory.chat_memory.messages:
        role = "👤" if msg.type == "human" else "🤖"
        st.markdown(f"{role} {msg.content}")
