#https://huggingface.co/settings/tokens
import requests
API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/mT5_multilingual_XLSum"

import os
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}


#Özetleme
data = {
    "inputs": "Hugging Face is a great platform for NLP.",
    "parameters": {"max_new_tokens": 60}
}

response = requests.post(API_URL, headers=headers, json=data)

try:
    response.raise_for_status()
    result = response.json()
    print("📘 Modelden Gelen Çıktı:\n", result[0]['summary_text'])
except Exception as e:
    print("❌ Hata oluştu:", e)
    print("🔍 Yanıt:\n", response.text)