from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
output = generator("Once upon a time in a land far away,", max_length=50, temperature=0.7)
print(output[0]['generated_text'])


