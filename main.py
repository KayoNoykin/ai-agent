import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
from openai import OpenAI
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
     raise RuntimeError("No API key found - check .env file")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User Prompt")
args = parser.parse_args()

client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

print(response.choices[0].message.content)