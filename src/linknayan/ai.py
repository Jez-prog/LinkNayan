import json
from pathlib import Path
from dotenv import load_dotenv
import os
from openai import OpenAI
from .config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL, MAX_TOKENS
import time

client = OpenAI(
    base_url= OPENROUTER_BASE_URL,
    api_key = OPENROUTER_API_KEY,
)



def detect_crisis(text):
    text_lower = text.lower()
    
    crisis_keywords = {
        "english": [
            "suicide", "kill myself", "end my life", "don't want to live",
            "harm myself", "self harm", "cutting", "overdose", "jump",
            "want to die", "going to die", "dead", "hopeless forever"
        ],
        "tagalog": [
            "gusto kong mamatay", "papatayin ko sarili ko", "suicide",
            "ayoko nang mabuhay", "walang pag-asa", "sasaktan ko sarili ko",
            "mag-overdose", "magsusuffer lang", "mamatay na lang"
        ]
    }

    for lang in crisis_keywords:
        for keyword in crisis_keywords[lang]:
            if keyword in text_lower:
                return True

    return False


def call_ai(promt, system_message):

    try:
        message = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": promt}
        ]

        tubag = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.7,
            messages=message
        )
        return tubag.choices[0].message.content
    
    except Exception as e:
        print(f"Something failed: {e}")
        return None




if __name__ == "__main__":
    print(detect_crisis("I want to kill myself."))
    print(detect_crisis("I feel anxious today"))
    print(detect_crisis("gusto kong mamatay maem"))
    print(detect_crisis("gi kapoy najud ko bai ai shet"))

    test_promt = "Hello! Who are You?"
    test_system = "You are Gay Nigger."

    resul = call_ai(test_promt, test_system)
    print(f"The efing result is: {resul}")
    time.sleep(5)
"""
outputs:
 uv run python -m src.linknayan.ai
congrats it exist!
True
False
True
False
(linknayan) [inconJeshztion@inconJeshztion linknayan]$ git 

"""


    
