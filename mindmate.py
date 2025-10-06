# mindmate.py
import os
from ai_client import MindMateAI
from sentiment import analyze_sentiment
from utils import BANNER, check_crisis, HELPLINE_TEXT, clean_text

SYSTEM_PROMPT = (
    "You are MindMate, a caring, empathetic, non-judgmental mental wellness companion. "
    "Offer supportive, reflective listening and short practical suggestions (breathing, journaling, grounding). "
    "Do NOT provide medical diagnosis or replace professional help. "
    "If user expresses self-harm or suicidal intent, provide emergency guidance and helpline info."
)

def main():
    print(BANNER)
    print("MindMate: Hi — I'm here to listen. Type 'quit' or 'exit' to leave.\n")
    bot = MindMateAI()

    # history for the LLM (keep short)
    history = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nMindMate: Take care — you can talk again anytime.")
            break

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit"}:
            print("MindMate: Thanks for sharing. Take care ❤️")
            break

        text = clean_text(user_input)
        # quick sentiment
        polarity = analyze_sentiment(text)
        if polarity < -0.5:
            print("MindMate: I notice you sound very upset. I'm here with you. ❤️")

        # crisis check before calling AI
        if check_crisis(text):
            print("MindMate:", HELPLINE_TEXT)
            # optionally you can log or ask permission to contact someone — keep it simple now
            continue

        # append to history and call AI
        history.append({"role": "user", "content": text})
        reply = bot.chat(history)  # expects list of messages
        # show AI response
        print("MindMate:", reply, "\n")

        # keep history short to reduce token usage (keep last 6 messages)
        if len(history) > 12:
            history = [history[0]] + history[-10:]

if __name__ == "__main__":
    main()
