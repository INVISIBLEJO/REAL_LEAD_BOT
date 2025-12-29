def detect_intent(message):
    m = message.lower()
    if "buy" in m: return "buy"
    if "rent" in m: return "rent"
    if "sell" in m: return "sell"
    return None