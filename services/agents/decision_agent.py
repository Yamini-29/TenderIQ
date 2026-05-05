def decision_logic(match, confidence):
    if confidence < 0.6:
        return "Needs Review"
    elif match:
        return "Eligible"
    else:
        return "Not Eligible"