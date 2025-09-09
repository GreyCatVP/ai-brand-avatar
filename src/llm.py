import os
from openai import OpenAI

class LLMClient:
    def __init__(self, model="gpt-4o"):
        self.model = model
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def __call__(self, prompt: str, temperature=0.3) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return resp.choices[0].message.content
