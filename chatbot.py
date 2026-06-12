from __future__ import annotations
import string
from responses import EXIT_COMMANDS, NORM_RESPONSES, SORTED_INTENTS, pick

def sanitize(raw: str) -> str:
    lowered = raw.lower().strip()
    no_punct = lowered.translate(str.maketrans("", "", string.punctuation))
    return " ".join(no_punct.split())

def extract_name(clean: str) -> str:
    for prefix in ("my name is ", "i am ", "call me ", "im "):
        if clean.startswith(prefix):
            name = clean[len(prefix):].strip()
            if name and len(name.split()) <= 3:
                return name.title()
    return ""

def get_response(clean: str, user_name: str | None) -> tuple[str, str | None]:
    is_name_intro = any(clean.startswith(prefix) for prefix in ("my name is ", "call me ", "im "))
    is_i_am_intro = clean.startswith("i am ") and clean not in NORM_RESPONSES
    if is_name_intro or is_i_am_intro:
        name = extract_name(clean)
        if name:
            return f"Nice to meet you, {name}! 👋 I'll remember that for our session.", name

    if clean == "who am i":
        if user_name:
            return f"You are {user_name}! 😊", user_name
        return "I don't know your name yet. Try: 'my name is <your name>'", user_name

    if clean in NORM_RESPONSES:
        return pick(NORM_RESPONSES[clean]), user_name

    for intent in SORTED_INTENTS:
        if clean == intent or clean.startswith(intent + " "):
            return pick(NORM_RESPONSES[intent]), user_name

    return (
        "🤔 I don't have a rule for that yet. "
        "Type 'help' for guidance or 'topics' to see what I know!",
        user_name,
    )

def run_chatbot() -> None:
    print("=" * 58)
    print("  🤖  DecoBot v2.0 — Rule-Based AI Chatbot")
    print("  DecodeLabs AI Internship | Project 1")
    print("  Type 'help' · 'topics' · or just ask anything!")
    print("  Type 'quit' or 'exit' to end the session.")
    print("=" * 58)

    user_name: str | None = None

    while True:
        try:
            raw = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Session interrupted. Goodbye! 👋")
            break

        clean = sanitize(raw)

        if not clean:
            print("Bot: Please type something! 😊")
            continue

        if len(clean) > 100:
            print("Bot: That's a long one! 😅 Could you rephrase in a shorter question?")
            continue

        if clean in EXIT_COMMANDS:
            farewell = NORM_RESPONSES.get(clean, "Goodbye! Keep learning and building. 👋")
            print("Bot:", pick(farewell))
            print("\n[ Session ended. DecoBot signing off. ]\n")
            break

        response, user_name = get_response(clean, user_name)
        print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()
