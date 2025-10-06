# utils.py

import re

# Pretty banner shown when the bot starts
BANNER = "=" * 50 + "\n" + "           MindMate – AI Companion\n" + "=" * 50

# Crisis detection keywords
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "want to die", "hurt myself",
    "i can’t go on", "i cant go on", "i'm going to end it", "i want to die"
]

# Crisis helpline info
HELPLINE_TEXT = (
    "If you are in immediate danger, please contact local emergency services right now.\n"
    "If you are in India, you can call AASRA at +91-22-27546669.\n"
    "If you are elsewhere, contact your local crisis helpline.\n"
)

# Checks if message contains crisis words
def check_crisis(text: str) -> bool:
    t = text.lower()
    for k in CRISIS_KEYWORDS:
        if k in t:
            return True
    return False

# Cleans extra spaces from user input
def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())
