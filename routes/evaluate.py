from fastapi import APIRouter
from services.parser import extract_criteria, extract_bidder_info
from services.matcher import evaluate

router = APIRouter()

@router.post("/evaluate")
def evaluate_docs(tender_text: str, bidder_text: str):
    criteria = extract_criteria(tender_text)
    bidder_data = extract_bidder_info(bidder_text)

    result = evaluate(criteria, bidder_data)

    return {
        "criteria": criteria,
        "bidder_data": bidder_data,
        "evaluation": result
    }