def evaluate(criteria, bidder_data):
    results = []

    for c in criteria:
        criterion_text = c.get("criterion", "").lower()

        decision = "Needs Review"
        reason = "Insufficient data"
        confidence = 0.5
        value = ""

        # TURNOVER
        if "turnover" in criterion_text:
            value = bidder_data.get("turnover", {}).get("value", "")
            confidence = bidder_data.get("turnover", {}).get("confidence", 0.5)

            if not value or "unclear" in value.lower() or confidence < 0.6:
                decision = "Needs Review"
                reason = "Turnover data unclear"
            elif "6" in value or "7" in value:
                decision = "Eligible"
                reason = "Turnover satisfies requirement"
            else:
                decision = "Not Eligible"
                reason = "Turnover below requirement"

        # PROJECTS
        elif "project" in criterion_text:
            value = bidder_data.get("projects_completed", {}).get("value", "")
            confidence = bidder_data.get("projects_completed", {}).get("confidence", 0.5)

            if not value or confidence < 0.6:
                decision = "Needs Review"
                reason = "Project data unclear"
            elif "5" in value or "4" in value:
                decision = "Eligible"
                reason = "Sufficient projects completed"
            else:
                decision = "Not Eligible"
                reason = "Insufficient projects"

        # GST
        elif "gst" in criterion_text:
            value = bidder_data.get("gst", {}).get("value", "")
            confidence = bidder_data.get("gst", {}).get("confidence", 0.5)

            if not value:
                decision = "Needs Review"
                reason = "GST missing"
            else:
                decision = "Eligible"
                reason = "GST present"

        results.append({
            "criterion": c.get("criterion"),
            "decision": decision,
            "confidence": confidence,
            "explanation": {
                "value": value,
                "reason": reason
            }
        })

    return results