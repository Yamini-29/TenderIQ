from services.llm_parser import extract_criteria_llm

def run_criteria_agent(tender_text):
    return extract_criteria_llm(tender_text)