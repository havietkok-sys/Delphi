from transformers import pipeline

generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")


def ask_model(prompt: str) -> str:

    result = generator(prompt, max_new_tokens=50, do_sample=True)
    print(prompt)
    print("=" * 50)
    print(result)

    return result[0]["generated_text"]


prompt = """
You are a helpful assistant.

Question:
What is the capital of Sweden?

Answer:
"""

answer = ask_model(prompt)

print(answer)
