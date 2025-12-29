from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# TEMP MEMORY (per user)
user_states = {}
leads = []

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    user_id = data.get("user_id")

    msg = message.lower()

    # STEP 1: If waiting for lead details
    if user_states.get(user_id) == "waiting_for_details":
        leads.append({
            "user_id": user_id,
            "details": message
        })

        user_states[user_id] = None

        reply = (
            "✅ Thank you! Your details have been received.\n\n"
            "Our agent will contact you shortly on WhatsApp.\n"
            "Looking forward to working with you 🚀"
        )

        return jsonify({"reply": reply})

    # STEP 2: Sales triggers
    if any(word in msg for word in ["price", "cost", "how much"]):
        reply = (
            "🔥 Our system helps you get REAL customers.\n\n"
            "Today’s offer: ₦20,000 setup.\n\n"
            "Are you interested?"
        )

    elif any(word in msg for word in ["yes", "interested", "okay"]):
        user_states[user_id] = "waiting_for_details"
        reply = (
            "Perfect 🎯\n\n"
            "Please send:\n"
            "1️⃣ Your full name\n"
            "2️⃣ WhatsApp number"
        )

    else:
        reply = (
            "Hi 👋 I help businesses get real customers.\n\n"
            "Are you looking for more leads or more sales?"
        )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
