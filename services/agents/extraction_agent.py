from services.llm_parser import extract_bidder_llm

def run_extraction_agent(bidder_text):
    return extract_bidder_llm(bidder_text)