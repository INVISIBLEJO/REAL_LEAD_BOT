from core.intent import detect_intent
from core.scoring import score_lead
from core.save import save_lead

def next_step(session, message):
    state = session["state"]
    data = session["data"]

    if state == "intent":
        intent = detect_intent(message)
        if not intent:
            return {"reply": "Buy, Rent, or Sell?"}

        data["intent"] = intent
        session["state"] = "location"
        return {"reply": "Which location?"}

    if state == "location":
        data["location"] = message
        session["state"] = "budget"
        return {"reply": "Your budget range?"}

    if state == "budget":
        data["budget"] = message
        session["state"] = "timeline"
        return {"reply": "When do you want to move?"}

    if state == "timeline":
        data["timeline"] = message
        session["state"] = "contact"
        return {"reply": "Phone or WhatsApp number?"}

    if state == "contact":
        data["contact"] = message
        data["score"] = score_lead(data)
        save_lead(data)
        return {"reply": "Thank you. An agent will contact you.", "done": True}