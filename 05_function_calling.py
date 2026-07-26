"""
05: Real function calling / tool use.

Instead of just constraining output to JSON, we define a "tool" the
model can call with structured arguments. This is the actual mechanism
used in agent systems later in the roadmap.
"""

import ollama
#Define a tool the model can call

tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_person_info",
            "description": "Extract structured info about a person from text",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "number"},
                    "job": {"type": "string"},
                    "city": {"type": "string"},
                    "email": {"type": "string"},
                },
                "required": ["name"],
            },
        },
    }
]

text = "Anish Potta is 25 year old computer science in Los Angeles, reachable at anish.potta@dusd.org"

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": text}],
    tools=tools,
)

message = response["message"]

if message.get("tool_calls"):
    for call in message["tool_calls"]:
        print("Model wants to call:", call["function"]["name"])
        print("With arguments:", call["function"]["arguments"])
    else:
        print("Model didn't call a tool. Raw response:")
        print(message["content"])

#tool_calls fixed part of API response