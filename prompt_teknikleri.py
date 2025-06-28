from openai import OpenAI
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1️⃣ Zero-shot Prompt
zero_shot = "İklim değişikliği nedir?"

# 2️⃣ Few-shot Prompt
few_shot = (
    "Soru: Sera gazı nedir?\n"
    "Cevap: Atmosferde ısıyı tutan gazlardır.\n"
    "Soru: Ozon tabakası ne işe yarar?\n"
    "Cevap: Zararlı UV ışınlarını engeller.\n"
    "Soru: İklim değişikliği nedir?\n"
    "Cevap:"
)

# 3️⃣ Chain of Thought Prompt
chain_of_thought = (
    "Soru: İklim değişikliği nedir?\n"
    "Düşün: Atmosferdeki sera gazları güneş ışınlarını tutar. "
    "Bu gazların artışı, sıcaklıkları yükseltir ve mevsimler değişir.\n"
    "Cevap:"
)

# LLM'den yanıt al
def get_completion(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Yanıtları yazdır
print("🔵 Zero-shot:\n", get_completion(zero_shot), "\n")
print("🟡 Few-shot:\n", get_completion(few_shot), "\n")
print("🔗 Chain of Thought:\n", get_completion(chain_of_thought), "\n")
