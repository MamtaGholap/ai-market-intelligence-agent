# AI Market Intelligence Agent

An AI-powered financial analysis tool built with Python that automatically generates professional stock market reports.

# What it does
- Takes any stock ticker symbol as input 
- Fetches live stock price data from Alpha Vantage API
- Sends data to Google Gemini AI for professional financial analysis
- Automatically saves a formatted report to disk

# Technologies Used
- Python 3.11
- Google Gemini AI API
- Alpha Vantage Financial API
- python-dotenv (To secure API key management)
- Git & GitHub

# How to Run
1. Clone the repository
2. Install dependencies: `pip install google-genai requests python-dotenv`
3. Create a `.env` file with your API keys
4. Run: `python3 market_intelligence.py`

# Project Structure
- `market_intelligence.py` — Main tool
- `agent.py` — Agentic AI version with tool calling
- `.env` — API keys (not included for security reasons)

## Author ##
Mamta Gholap — AI/Automation Engineer (Student)
Python | APIs | AI Integration | Finance Domain Knowledge