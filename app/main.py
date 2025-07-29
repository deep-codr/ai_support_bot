import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Chatbot import find_best_match
import json
import streamlit as st

# Load intents data
with open('data/intents.json', 'r') as file:
    intents_data = json.load(file)

# --- PAGE CONFIG ---
st.set_page_config(page_title="🤖 AI Support ChatBot", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            background-color: #f0f2f6;
            color: #000000;
        }
        .stTextInput > label {
            font-weight: bold;
        }
        .stSuccess {
            background-color: #dff0d8;
            color: #155724;
            padding: 12px;
            border-radius: 10px;
            font-weight: 500;
        }
        .stError {
            background-color: #f8d7da;
            color: #721c24;
            padding: 12px;
            border-radius: 10px;
            font-weight: 500;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- TITLE & HEADER ---
st.title("💬 AI Customer Support")
st.subheader("Ask me anything related to our services!")
st.markdown("---")

# --- INPUT BOX ---
query = st.text_input("🔎 Type Your Question below:")

# --- RESPONSE ---
if query:
    result = find_best_match(query, intents_data)

    if result:
        st.success(f"**Answer:** {result}")
    else:
        st.error("❌ Sorry! I couldn't understand your question. Please try rephrasing.")




# 🔘 QUICK BUTTONS block
st.markdown("#### 🔍 Quick Questions:")
col1, col2 = st.columns(2)

with col1:
    if st.button("📦 Order Status"):
        st.success(find_best_match("order status", intents_data))

    if st.button("💰 Refund Policy"):
        st.success(find_best_match("refund", intents_data))

with col2:
    if st.button("📞 Contact Support"):
        st.success(find_best_match("contact", intents_data))

    if st.button("🔧 Service Request"):
        st.success(find_best_match("service", intents_data))


# 🧹 Clear Button (optional)
if st.button("🧹 Clear Chat"):
    st.experimental_rerun()

if st.button("👍 Helpful"):
    st.toast("Glad I could help! 😊", icon="✅")

if st.button("👎 Not Helpful"):
    st.toast("Sorry about that! Try rephrasing your question.", icon="😢")



# 🎨 FOOTER
st.markdown("---")
st.markdown("<center>© 2025 DeepCodr Support AI | Built with ❤️ by Varun</center>", unsafe_allow_html=True)
st.markdown("<center>Follow us: [Instagram](https://www.instagram.com/deepcodr?igsh=bzUwZDcyYmVvZjR6)</center>", unsafe_allow_html=True)
