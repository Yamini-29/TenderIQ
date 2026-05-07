import re

def extract_number(text):
    if text is None:
        return None
    nums = re.findall(r"\d+", str(text))
    return int(nums[0]) if nums else None


def evaluate(criteria, bidder):
    results = []

    for c in criteria:
        text = c.get("criterion", "").lower()

        decision = "Needs Review"
        reason = "Unknown"
        confidence = 0.5
        value = None
        required = None

        if "turnover" in text:
            value = bidder.get("turnover", {}).get("value")
            confidence = bidder.get("turnover", {}).get("confidence", 0.5)
            actual = extract_number(value)
            required = extract_number(text)

        elif "project" in text:
            value = bidder.get("projects_completed", {}).get("value")
            confidence = bidder.get("projects_completed", {}).get("confidence", 0.5)
            actual = extract_number(value)
            required = extract_number(text)

        elif "gst" in text:
            value = bidder.get("gst", {}).get("value")
            confidence = bidder.get("gst", {}).get("confidence", 0.5)
            decision = "Eligible" if value else "Needs Review"
            reason = "GST present" if value else "Missing GST"

        else:
            actual = None

        if "turnover" in text or "project" in text:
            if actual is None or required is None or confidence < 0.6:
                decision = "Needs Review"
                reason = "Low confidence"
            elif actual >= required:
                decision = "Eligible"
                reason = f"{actual} >= {required}"
            else:
                decision = "Not Eligible"
                reason = f"{actual} < {required}"

        results.append({
            "criterion": c.get("criterion"),
            "decision": decision,
            "confidence": confidence,
            "explanation": {
                "value": value,
                "required": required,
                "reason": reason
            }
        })

    return results