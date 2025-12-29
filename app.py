from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# In-memory storage (replace with DB later)
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

    # Initialize user
    if user_id not in user_states:
        user_states[user_id] = {
            "stage": "start",
            "lead": {}
        }

    state = user_states[user_id]

    # ===============================
    # STAGE 1: START
    # ===============================
    if state["stage"] == "start":
        state["stage"] = "intent"
        return jsonify({
            "reply":
            "🏡 Welcome to Smart Property Assistant\n\n"
            "Are you looking to:\n"
            "1️⃣ Buy property\n"
            "2️⃣ Sell property\n"
            "Reply BUY or SELL"
        })

    # ===============================
    # STAGE 2: BUY OR SELL
    # ===============================
    if state["stage"] == "intent":
        if "buy" in msg:
            state["lead"]["type"] = "buyer"
            state["stage"] = "buyer_location"
            return jsonify({
                "reply":
                "Great choice 👌\n"
                "Which city or area are you looking to buy in?"
            })

        if "sell" in msg:
            state["lead"]["type"] = "seller"
            state["stage"] = "seller_location"
            return jsonify({
                "reply":
                "Excellent 👍\n"
                "Where is the property located?"
            })

        return jsonify({"reply": "Please reply BUY or SELL"})

    # ===============================
    # BUYER FLOW
    # ===============================
    if state["stage"] == "buyer_location":
        state["lead"]["location"] = message
        state["stage"] = "buyer_budget"
        return jsonify({
            "reply":
            "💰 What is your budget range?\n"
            "Example: ₦50m – ₦80m"
        })

    if state["stage"] == "buyer_budget":
        state["lead"]["budget"] = message
        state["stage"] = "buyer_contact"
        return jsonify({
            "reply":
            "📞 Almost done!\n"
            "Please send your full name and WhatsApp number."
        })

    # ===============================
    # SELLER FLOW
    # ===============================
    if state["stage"] == "seller_location":
        state["lead"]["location"] = message
        state["stage"] = "seller_price"
        return jsonify({
            "reply":
            "💵 What price are you selling at?"
        })

    if state["stage"] == "seller_price":
        state["lead"]["price"] = message
        state["stage"] = "seller_contact"
        return jsonify({
            "reply":
            "📞 Please send your full name and WhatsApp number."
        })

    # ===============================
    # FINAL CONTACT CAPTURE
    # ===============================
    if state["stage"] in ["buyer_contact", "seller_contact"]:
        state["lead"]["contact"] = message
        state["lead"]["timestamp"] = str(datetime.datetime.now())

        leads.append(state["lead"])
        state["stage"] = "completed"

        return jsonify({
            "reply":
            "✅ Thank you!\n\n"
            "A certified real-estate agent will contact you shortly.\n"
            "Serious buyers & sellers only — we value your time.\n\n"
            "🏡 Smart deals. Smart investments."
        })

    # ===============================
    # LOCK AFTER COMPLETION
    # ===============================
    if state["stage"] == "completed":
        return jsonify({
            "reply":
            "✅ Your request has been received.\n"
            "Our agent will contact you on WhatsApp shortly."
        })

    # Fallback
    return jsonify({
        "reply": "Please refresh and start again."
    })

if __name__ == "__main__":
    app.run()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
