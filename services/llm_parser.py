import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def clean_json(text):
    text = text.strip()

    if "```" in text:
        text = text.split("```")[1]

    start = min(
        [i for i in [text.find("{"), text.find("[")] if i != -1],
        default=0
    )
    end = max(text.rfind("}"), text.rfind("]"))

    if start != -1 and end != -1:
        text = text[start:end+1]

    return text


def call_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    raw = response.json().get("response", "")
    cleaned = clean_json(raw)
    return cleaned


def safe_json_load(text):
    try:
        return json.loads(text)
    except:
        return {
            "error": "invalid_json",
            "raw_output": text
        }


# 🔹 Criteria Extraction
def extract_criteria_llm(tender_text):
    prompt = f"""
Extract eligibility criteria from the text.

Return ONLY JSON:

[
  {{
    "criterion": "...",
    "type": "financial/technical/compliance",
    "mandatory": true,
    "confidence": 0.9
  }}
]

TEXT:
{tender_text}
"""

    output = call_llm(prompt)
    return safe_json_load(output)


# 🔹 Bidder Extraction
def extract_bidder_llm(bidder_text):
    prompt = f"""
Extract bidder details.

Return ONLY JSON:

{{
  "turnover": {{"value": "...", "confidence": 0.9}},
  "projects_completed": {{"value": "...", "confidence": 0.9}},
  "gst": {{"value": "...", "confidence": 0.9}},
  "certifications": {{"value": "...", "confidence": 0.9}}
}}

TEXT:
{bidder_text}
"""

    output = call_llm(prompt)
    return safe_json_load(output)