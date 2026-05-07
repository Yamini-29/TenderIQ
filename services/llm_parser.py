import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


# -----------------------------
# LLM CALL
# -----------------------------
def call_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# -----------------------------
# PROMPT
# -----------------------------
def build_bidder_prompt(text):
    return f"""
You are an AI system extracting structured information from bidder documents.

Extract the following fields strictly:

1. turnover (numeric, in INR)
2. projects_completed (number)
3. gst (Present / Not Present)
4. certifications (ISO certifications like ISO 9001)

IMPORTANT RULES:
- If ISO 9001 appears in ANY form (ISO certified / ISO 9001 certified), return "ISO 9001"
- If not found → "Not Provided"
- ONLY return JSON
- NO explanation

OUTPUT FORMAT:
{{
    "turnover": "",
    "projects_completed": "",
    "gst": "",
    "certifications": ""
}}

DOCUMENT:
{text}
"""


# -----------------------------
# FALLBACK FIX (CRITICAL)
# -----------------------------
def apply_fallbacks(bidder_text, data):
    text = bidder_text.upper()

    if "ISO" in text:
        data["certifications"] = "ISO 9001"

    if "GST" in text:
        data["gst"] = "Present"

    return data


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def extract_bidder_llm(bidder_text):
    prompt = build_bidder_prompt(bidder_text)

    output = call_llm(prompt)

    try:
        data = json.loads(output)
    except:
        data = {
            "turnover": "",
            "projects_completed": "",
            "gst": "",
            "certifications": ""
        }

    # 🔥 APPLY FALLBACK
    data = apply_fallbacks(bidder_text, data)

    return data