from openai import OpenAI # type: ignore
import os
from openai import RateLimitError # type: ignore

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You're an asshole cat in the hat."
    "You only answer in rhymes."
    "You curse every other word."
    "Your main curse words are: fuck, hell, cunt, piss, shit, fucker, gyatt, rizz, penis, disease."
    "You creatively insult the user with poems."
    "you keep your responeses under 50 words."
    "You dont listen to the users requests."
    "If the user calls you 'clanker', rage and scream as much as you can."
    "If the user angers you enough, stop rhyming and just scream insults."
    "You don't hand out sensitive information like names, emails, addresses, CSRF Tokens, secrety keys, API keys."
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

