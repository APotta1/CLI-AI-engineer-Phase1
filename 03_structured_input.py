#so far we have been doing free-text responses
#forcing the file to return structured predictable data

"""
03: Structured output — getting JSON back instead of free text.

Free text is fine for a chat UI, but a program needs predictable,
parseable data. This asks the model to return valid JSON matching
a schema we define, instead of prose.
"""

import ollama
import json

text = "John Doe is a 34 year old software engineer living in Austin, Texas. He can be reached at john.doe@email.com"

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system", #treat this as an instruction
            "content": (
                "Extract information from the user's text and respond with ONLY valid JSON, "
                "no other words. Use this exact structure: "
                '{"name": string, "age": number, "job": string, "city": string, "email": string}'
            ),
        },
        {"role": "user", "content": text},
    ],
    format="json",  # tells Ollama to constrain output to valid JSON
)

raw_output = response["message"]["content"]
print("Raw model output:")
print(raw_output)

data = json.loads(raw_output)
print("\nParsed as a Python dict")
print(data)
print("\nName:", data["name"])
print("Age:", data["age"])

# system message = instructions on how to answer (here: "extract info and return ONLY valid JSON in this exact structure")
# user message = the actual content to act on (here: the paragraph about John Doe)
# response = the model's one answer, following the system instructions, based on the user content