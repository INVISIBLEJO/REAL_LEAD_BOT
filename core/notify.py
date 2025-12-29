import requests

BUYER_WHATSAPP = "234XXXXXXXXX"

def notify_buyer(lead):
    message = f"""
NEW HOT LEAD 🔥
Intent: {lead['intent']}
Location: {lead['location']}
Budget: {lead['budget']}
Timeline: {lead['timeline']}
Contact: {lead['contact']}
Score: {lead['score']}
"""
    # placeholder: WhatsApp API / email / Telegram
    print(message)