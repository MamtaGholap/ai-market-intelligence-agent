from google import genai
import requests

from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
ALPHA_KEY = os.getenv("ALPHA_KEY")

client = genai.Client(api_key=GEMINI_KEY)

# Tool 1 — Get stock price
def get_stock_price(symbol: str) -> str:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_KEY}"
    response = requests.get(url)
    data = response.json()
    quote = data["Global Quote"]
    return f"Symbol: {quote['01. symbol']}, Price: ${quote['05. price']}, Change: {quote['10. change percent']}"

# Tool 2 — Save report
def save_report(content: str) -> str:
    with open("agent_report.txt", "w") as file:
        file.write(content)
    return "Report saved as agent_report.txt"

print("Testing tools...")
print(get_stock_price("AAPL"))

# Define tools for the agent
tools = [get_stock_price, save_report]

# Agent loop
print("\nAI Market Agent Ready.")
user_request = input("What would you like to analyse? ")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=user_request,
    config=genai.types.GenerateContentConfig(
        tools=tools,
        system_instruction="You are a financial analyst agent. When asked about a stock, use get_stock_price to fetch data, analyse it professionally, then use save_report to save your analysis."
    )
)

print("\nAgent Response:")
print(response.text)