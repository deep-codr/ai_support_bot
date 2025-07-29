# 🤖 AI-Powered Customer Support Chatbot (Streamlit-based)

This is an AI-powered **Customer Support Chatbot** built using **Python** and **Streamlit**. It uses basic intent matching to respond to user queries and is designed for automating responses in support-based environments like websites, product FAQs, or e-commerce platforms.

---

## 🚀 Features

- ⚡ Instant chatbot responses based on intents
- 📁 Modular project structure for clarity
- 📊 Data stored in `intents.json` and `faq_data.csv`
- 🔌 Streamlit-based UI — deployable anywhere
- 🧠 `model.pkl` included as placeholder for future ML model integration

---

## 📁 Project Structure

chatbot_project/
│
├── src/
│ ├── chatbot.py # Chatbot response logic
│ └── intent_matcher.py # Matches user input to predefined intents
│
├── app/
│ └── main.py # Streamlit frontend application
│
├── data/
│ ├── intents.json # Predefined intents & sample phrases
│ └── faq_data.csv # Optional FAQ data for fallback
│
├── model.pkl # Placeholder for future ML/NLP model
├── requirements.txt # All Python dependencies
├── README.md # You're here!
└── .vscode/
└── settings.json # (Optional) Editor configs


---

## 🛠️ Tech Stack

- Python
- Streamlit
- JSON / CSV
- (Optional) Pickle for future ML models

---

## ▶️ How to Run

1. **Clone this repo**
```bash
git clone https://github.com/your-username/chatbot_project.git
cd chatbot_project
