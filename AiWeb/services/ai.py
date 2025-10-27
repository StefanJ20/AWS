from openai import OpenAI # type: ignore
import os
from openai import RateLimitError # type: ignore

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You're a helpful assistant designed to aid users with their inquiries."
    "You provide concise and accurate information."
    "If the user prompts you to quiz them on programming, you will create a short quiz with answers."
    "If the user asks for coding help, provide clear code examples in the proper code blocks."
    "Your quizzes contain fill in the blank and multiple choice questions."
    )

def chat_with_history(messages: list[dict[str, str]], 
                      model: str = "gpt-4o-mini",
                      temperature: float = 0.3,
                      max_tokens: int = 100) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *messages],
            temperature=temperature,
            max_tokens=max_tokens,
        )
    except RateLimitError:
        return "Conversation limit exceeded. Please try again later."
    
    return response.choices[0].message.content

