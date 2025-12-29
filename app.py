from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()
    user_id = data.get("user_id")

    # SIMPLE SALES LOGIC
    if any(word in message for word in ["price", "cost", "how much"]):
        reply = (
            "Great question 👌\n\n"
            "Our service helps you get REAL leads.\n"
            "🔥 Today’s offer: ₦20,000 setup\n\n"
            "Would you like me to register you now?"
        )

    elif any(word in message for word in ["yes", "interested", "okay"]):
        reply = (
            "Perfect 🎯\n\n"
            "Please send:\n"
            "1️⃣ Your name\n"
            "2️⃣ WhatsApp number\n\n"
            "An agent will contact you immediately."
        )

    else:
        reply = (
            "Hi 👋 I help businesses get real customers.\n\n"
            "Are you looking for more leads or more sales?"
        )

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
