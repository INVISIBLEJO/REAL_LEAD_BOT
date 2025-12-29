def score_lead(data):
    score = 0
    if data["intent"] == "buy": score += 20
    if "immediately" in data["timeline"].lower(): score += 20
    if len(data["contact"]) >= 10: score += 30
    return score