import re


def extract_number(text):
    if not text:
        return None

    nums = re.findall(r"\d+\.?\d*", text.replace(",", ""))
    if nums:
        return float(nums[0])
    return None


def match_turnover(criterion, value):
    required = extract_number(criterion)
    actual = extract_number(value)

    if actual is None:
        return "Needs Review", "Turnover not found"

    if actual >= required:
        return "Eligible", f"{actual} ≥ {required}"
    return "Not Eligible", f"{actual} < {required}"


def match_projects(criterion, value):
    required = extract_number(criterion)
    actual = extract_number(value)

    if actual is None:
        return "Needs Review", "Projects not found"

    if actual >= required:
        return "Eligible", f"{actual} ≥ {required}"
    return "Not Eligible", f"{actual} < {required}"


def match_gst(value):
    if value and "present" in value.lower():
        return "Eligible", "GST available"
    return "Not Eligible", "GST missing"


def match_iso(value):
    if not value:
        return "Needs Review", "Certification missing"

    val = value.upper()

    if "ISO" in val:
        return "Eligible", "ISO certification present"

    return "Not Eligible", "ISO missing"


# -----------------------------
# MAIN EVALUATOR
# -----------------------------
def evaluate(criteria, bidder_data):
    results = []

    for c in criteria:
        text = c["criterion"].lower()

        if "turnover" in text:
            decision, reason = match_turnover(text, bidder_data.get("turnover"))

        elif "project" in text:
            decision, reason = match_projects(text, bidder_data.get("projects_completed"))

        elif "gst" in text:
            decision, reason = match_gst(bidder_data.get("gst"))

        elif "iso" in text:
            decision, reason = match_iso(bidder_data.get("certifications"))

        else:
            decision, reason = "Needs Review", "Unknown criterion"

        results.append({
            "criterion": c["criterion"],
            "decision": decision,
            "reason": reason,
            "confidence": 0.9 if decision != "Needs Review" else 0.6
        })

    return results