import streamlit as st
import random
from datetime import date

# Title
st.title("🌞 Daily Motivation")

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Push yourself, because no one else is going to do it for you.",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Great things never come from comfort zones.",
    "Success is what comes after you stop making excuses.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream it. Wish it. Do it.",
    "Stay positive, work hard, make it happen.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Little things make big days."
]

# Deterministic daily quote using today's date
today = date.today()
index = today.toordinal() % len(quotes)
daily_quote = quotes[index]

# Display quote
st.write(f"### 📝 Quote for {today.strftime('%B %d, %Y')}")
st.success(daily_quote)

# Optional: add a button to generate a random one
if st.button("🎲 Show Another Random Quote"):
    st.info(random.choice(quotes))
