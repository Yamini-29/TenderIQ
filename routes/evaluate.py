from fastapi import APIRouter
from services.agents.criteria_agent import run_criteria_agent
from services.agents.extraction_agent import run_extraction_agent
from services.matcher import evaluate

router = APIRouter()

@router.post("/evaluate")
def evaluate_docs(tender_text: str, bidder_text: str):

    criteria = run_criteria_agent(tender_text)
    bidder_data = run_extraction_agent(bidder_text)

    results = evaluate(criteria, bidder_data)

    return {
        "criteria": criteria,
        "bidder_data": bidder_data,
        "evaluation": results
    }