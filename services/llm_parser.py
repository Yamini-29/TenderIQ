import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def clean_json(text):
    text = text.strip()

    if "```" in text:
        text = text.split("```")[1]

    start = min([i for i in [text.find("{"), text.find("[")] if i != -1], default=0)
    end = max(text.rfind("}"), text.rfind("]"))

    if start != -1 and end != -1:
        text = text[start:end+1]

    return text


def call_llm(prompt):
    res = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False}
    )
    return clean_json(res.json()["response"])


def safe_json(text):
    try:
        return json.loads(text)
    except:
        return []


def extract_criteria_llm(text):
    prompt = f"""
Extract eligibility criteria as JSON list:
[{{"criterion": "...", "type": "financial/technical/compliance", "confidence": 0.9}}]

TEXT:
{text}
"""
    return safe_json(call_llm(prompt))


def extract_bidder_llm(text):
    prompt = f"""
Extract bidder info as JSON:
{{
 "turnover": {{"value": "...", "confidence": 0.9}},
 "projects_completed": {{"value": "...", "confidence": 0.9}},
 "gst": {{"value": "...", "confidence": 0.9}},
 "certifications": {{"value": "...", "confidence": 0.9}}
}}

TEXT:
{text}
"""
    return safe_json(call_llm(prompt))