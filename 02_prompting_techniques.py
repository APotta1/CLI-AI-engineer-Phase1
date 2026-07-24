import ollama

question = "Should I use a list or a dictionary in Python to store user records?"
# one fixed question
prompts = {
    "no_system_prompt": None,
    "concise": "Answer in one sentence. No explanation.",
    "expert": "You are a senior Python engineer. Give a technical, precise answer with a code example.",
    "beginner_friendly": "You are teaching someone who just started coding. Use simple words and an analogy.",
}
#What changes each time is the system prompt
#shapes how the system should act

for label, system_prompt in prompts.items():
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": question}) 
#The loop one API call per system
#preparing what to send


    response = ollama.chat(model = "llama3.2", messages = messages) #this talks to model

    print(f"=== {label} ===")
    print(response["message"]["content"])
    print()