def extract_criteria(text):
    criteria = []

    lines = text.split("\n")
    for line in lines:
        if "₹" in line or "GST" in line or "projects" in line:
            criteria.append(line.strip())

    return criteria


def extract_bidder_info(text):
    data = {}

    for line in text.split("\n"):
        if "Turnover" in line:
            data["turnover"] = line
        elif "Projects" in line:
            data["projects"] = line
        elif "GST" in line:
            data["gst"] = line
        elif "ISO" in line:
            data["iso"] = line

    return data