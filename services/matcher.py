def evaluate(criteria, bidder_data):
    results = []

    for c in criteria:
        if "turnover" in c.lower():
            if "₹6" in bidder_data.get("turnover", ""):
                results.append((c, "Eligible"))
            else:
                results.append((c, "Not Eligible"))

        elif "projects" in c.lower():
            if "5" in bidder_data.get("projects", ""):
                results.append((c, "Eligible"))
            else:
                results.append((c, "Needs Review"))

        else:
            results.append((c, "Needs Review"))

    return results