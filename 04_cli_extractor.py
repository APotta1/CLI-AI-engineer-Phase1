"""
04: CLI Extractor — the Phase 1 milestone.

Takes a sentence as a command-line argument, asks the model to extract
structured data from it, and prints the result. Combines everything from
files 1-3: a real API call, a system prompt, and JSON-constrained output.
"""

import sys
import json
import ollama

def extract_info(text: str) -> dict:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract information from the user's text and respond with ONLY valid JSON, "
                    "no other words. Use this exact structure: "
                    '{"name": string, "age": number, "job": string, "city": string, "email": string}. '
                    'If a field is not mentioned in the text, use null for that field.'
                ),
            },
            {"role": "user", "content": text},
        ],
        format="json",
    )
    raw_output = response["message"]["content"]
    return json.loads(raw_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 04_cli_extractor.py \"some sentence about a person\"")
        sys.exit(1)

    text = sys.argv[1]
    data = extract_info(text)

    print("Extracted data:")
    for key, value in data.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()