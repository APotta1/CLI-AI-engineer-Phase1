"""
01: Your first local LLM call via Ollama

NO API key, no cost - this runs entirely on your machine
"""

import ollama

response = ollama.chat(
    model = "llama3.2",
    messages =[
       {"role": "system", "content": "You are a concise statement. Answer in 2-3 sentences"},
       {"role": "user", "content": "Explain what a vector embedding is, for someone who knows ML but not LLMs."},
    ],
)

print(response["message"]["content"])
print("\n---")
print("Prompt tokens:", response.get("prompt_eval_count"))
print("Response tokens:", response.get("eval_count"))