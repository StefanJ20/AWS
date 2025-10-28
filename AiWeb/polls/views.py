import json
from django.http.response import JsonResponse
from django.shortcuts import render
from openai import OpenAI # type: ignore
from services.ai import chat_with_history # type: ignore
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    return render(request, "index.html")

def memes(request):
    return render(request, "memes.html")

def trim_by_turns(history, max_turns=6):
    return history[-max_turns:]

@csrf_protect
def chat_api(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)  
    user_message=(data.get("message") or "").strip()
    if not user_message:
        return JsonResponse({"error": "Message is required"}, status=400)
    history = request.session.get("chat_history", [])
    history.append({"role": "user", "content": user_message})
    history = trim_by_turns(history, max_turns=6)

    reply = chat_with_history(history)
    
    history.append({"role": "assistant", "content": reply})
    request.session["chat_history"] = history
    request.session.modified = True

    return JsonResponse({"reply": reply})
    