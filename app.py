import nltk
from nltk.chat.util import Chat, reflections
import gradio as gr

# Define chatbot responses using pattern-matching pairs
pairs = [
    (r"(?i)\b(hi|hello|hey|heyy)\b", ["Hello! Welcome to our hotel booking service. How can I assist you today?"]),

    (r"(?i)\b(i want to book a room|i would like to book a room|book a hotel|i need a room|room|need room)\b",
     ["Sure! What type of room are you looking for? We offer Suite Rooms, Deluxe Rooms, and Standard Rooms."]),

    (r"(?i)\b(rooms|room details|list rooms|what rooms do you have|tell me about the rooms)\b",
     ["We offer three types of rooms:\n1. Suite Room - ₹5000 per night\n2. Deluxe Room - ₹3500 per night\n3. Standard Room - ₹2000 per night\nWhich one would you prefer?"]),

    (r"(?i)\b(suite room|deluxe room|standard room)\b",
     ["Great choice! Do you have any special requests, such as extra beds, a sea view, or a late check-in?"]),

    (r"(?i)\b(what are the prices|tell me the price|price details|pricings|price)\b",
     ["The pricing is as follows:\n- Suite Room: ₹5000 per night\n- Deluxe Room: ₹3500 per night\n- Standard Room: ₹2000 per night"]),

    (r"(?i)\b(do you have a pool|is pool available|pool)\b",
     ["Yes! We have a **swimming pool** 🏊, open from **6 AM to 10 PM** for all guests. We also provide free WiFi and other amenities. Would you like more details?"]),

    (r"(?i)\b(is wifi available|do you have wifi|wifi)\b",
     ["Yes! We offer **free high-speed WiFi** 📶 in all rooms and public areas. We also have a swimming pool, gym access, and complimentary breakfast. Would you like to know more?"]),

    (r"(?i)\b(what facilities do you offer|facilities|extra facilities)\b",
     ["Yes! We offer the following facilities:\n"
      "✅ WiFi Available** – Free high-speed WiFi in all rooms and public areas 📶\n"
      "✅ Swimming Pool** – Open from 6 AM to 10 PM 🏊\n"
      "✅ Gym Access** – Fully equipped fitness center open 24/7 💪\n"
      "✅ Complimentary Breakfast** – Served from 7 AM to 10 AM 🍽️\n"
      "✅ 24/7 Room Service** – Order food and beverages anytime 🛎️\n"
      "✅ Parking Facility** – Free and secure parking for all guests 🚗\n"
      "✅ Airport Shuttle Service** – Available on request (extra charges apply) ✈️\n"
      "Would you like more details on any specific facility?"]),

    (r"(?i)\b(how can i confirm my booking|how to confirm booking|confirm booking)\b",
     ["To confirm your booking, please visit our website or call our reservation desk at +91 9876543210."]),

    (r"(?i)\b(thank you|thanks)\b", ["You're welcome! If you need more details, visit our website. Have a great day!"]),

    (r"(?i)\b(quit|bye|goodbye)\b", ["Goodbye! Looking forward to assisting you again."]),

    # Default response for unrelated queries
    (r"(.*)", ["I'm here to assist with hotel bookings. For other queries, please visit our website: https://www.mtrhotelbooking.com"])
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Function to interact with chatbot
def chat_response(user_input):
    return chatbot.respond(user_input)

# Sample questions for user guidance
examples = [
    "Hi",
    "I want to book a room",
    "What rooms do you have?",
    "Tell me about the rooms",
    "What is the price of a Suite Room?",
    "Is pool available?",
    "Is WiFi available?",
    "What facilities do you offer?",
    "How can I confirm my booking?",
    "Thanks!"
]

# Deploy using Gradio with example questions
iface = gr.Interface(
    fn=chat_response, 
    inputs="text", 
    outputs="text", 
    title="Hotel Booking Chatbot",
    description="Ask me about hotel room bookings, pricing, and facilities. Here are some example questions you can ask:",
    examples=examples
)

iface.launch()
