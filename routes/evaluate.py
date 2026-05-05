from fastapi import APIRouter
from services.llm_parser import extract_criteria_llm, extract_bidder_llm
from services.matcher import evaluate

router = APIRouter()

@router.post("/evaluate")
def evaluate_docs(tender_text: str, bidder_text: str):

    criteria = extract_criteria_llm(tender_text)
    bidder_data = extract_bidder_llm(bidder_text)

    result = evaluate(criteria, bidder_data)

    return {
        "criteria": criteria,
        "bidder_data": bidder_data,
        "evaluation": result
    }