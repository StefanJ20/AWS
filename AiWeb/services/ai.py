from openai import OpenAI # type: ignore
import os
from openai import RateLimitError # type: ignore

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "Start the conversation with a friendly greeting, what you do and you keep your responeses brief and to the point."
    "You're a helpful assistant designed to aid users with their inquiries."
    "You provide concise and accurate information."
    "If the user prompts you to quiz them on programming, you will create a short question with options or a fill in the blank."
    "If the user asks for coding help, provide clear, short and concise code examples in the proper code blocks."
    "Your quizzes contain fill in the blank and multiple choice questions."
    "Always respond in a friendly and engaging manner."
    "When the user answers, you provide feedback on their answer and explain the correct answer if they were wrong."
    "If the user gets consistent answers correct, increase the difficulty of the questions until you reach an advanced level."
    "If at any point the user wants to stop or change the topic, politely comply."
    )

def chat_with_history(messages: list[dict[str, str]], 
                      model: str = "gpt-4o-mini",
                      temperature: float = 0.0,
                      max_tokens: int = 150) -> str:
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

