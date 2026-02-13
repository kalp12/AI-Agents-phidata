# 🤖 AI-Agents (Phidata + Groq)

This project demonstrates how to build AI agents using the **Agno agent framework**, powered by **Groq LLMs**, with tools for:

- Financial data analysis
- Stock fundamentals & analyst recommendations
- Web search integration
- Multi-agent collaboration

---

## 🚀 Overview

This repository contains multiple AI agent examples:

1. Basic LLM agent
2. Finance agent with stock tools
3. Web search agent
4. Multi-agent team (finance + web)
5. Company comparison using real financial data

The agents use:
- Groq Llama models
- YFinance tools
- DuckDuckGo search
- Tool calling + structured outputs

---

## 📂 Project Structure

AI-Agents-phidata/
│
├── agents.py 
├── finance_agent.py
├── sample_test.py 
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Requirements

- Python 3.9+
- Groq API Key
- Agno framework
- python-dotenv

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Setup
Create a .env file:

GROQ_API_KEY=your_api_key_here

## 🧠 Agents Included
1️⃣ Basic Agent
Simple LLM prompt example:

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response(
    "Share a 2 sentence love story between dosa and samosa"
)
2️⃣ Finance Agent
Features:

Fetch stock price

Analyst recommendations

Company fundamentals

Symbol lookup helper

Tools used:

YFinanceTools

Custom get_company_symbol() function

3️⃣ Web Search Agent
Capabilities:

Searches the web using DuckDuckGo

Returns summarized results

Includes sources

Bullet-point answers

4️⃣ Multi-Agent Team
Combines:

🌐 Web Agent → company info & news

📈 Finance Agent → stock data

Team agent compares companies like:

Vedanta

LTIMindtree

TCS

Output includes:

Markdown tables

Analyst recommendations

Company fundamentals

Forecast insights

📊 Example Queries
Summarize and compare analyst recommendations and fundamentals for Vedanta and LTIMindtree.
Show in tables.
What do these companies do?
What is the stock forecast?
Get analyst recommendations for LTIMindtree
What do Vedanta and LTIMindtree do?
🛠 Tools Used
Groq LLM (llama-3.3-70b-versatile)

YFinanceTools

Stock price

Analyst recommendations

Company info

Fundamentals

DuckDuckGoTools

Web search

Source-backed summaries

🧩 Key Features
Tool-calling agents

Multi-agent collaboration

Financial data retrieval

Web-enhanced responses

Markdown table outputs

Debug mode support

## 📈 Use Cases
Stock research assistant

Financial comparison bot

Market analysis automation

AI-powered research agents

Multi-agent orchestration demos

## 🔮 Future Improvements
Add Streamlit UI

Add portfolio analysis agent

Add news sentiment analysis

Add crypto market agent
