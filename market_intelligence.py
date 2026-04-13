from google import genai
import requests

from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
ALPHA_KEY = os.getenv("ALPHA_KEY")

# Clients
client = genai.Client(api_key=GEMINI_KEY)

print("Market Intelligence Tool")
print("------------------------")

symbol = input("Enter stock symbol (e.g. AAPL, TSLA, IBM): ").upper()
print(f"\nFetching data for {symbol}...")
response = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=" + ALPHA_KEY)
data = response.json()
quote = data["Global Quote"]
print(f"Symbol: {quote['01. symbol']}")
print(f"Price: ${quote['05. price']}")
print(f"Change: {quote['10. change percent']}")
print(f"Last Trading Day: {quote['07. latest trading day']}")
print("\nAsking AI for analysis...")

prompt = f"""
You are a financial analyst. Analyse this stock data and give a brief professional summary:

Company: {symbol}
Current Price: ${quote['05. price']}
Change Today: {quote['10. change percent']}
Last Trading Day: {quote['07. latest trading day']}

Provide:
1. A 2-sentence market summary
2. What this price movement might indicate
3. One risk and one opportunity for investors
"""

try:
    response_ai = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    analysis = response_ai.text
    print("\n--- AI Analysis ---")
    print(analysis)

except Exception as e:
    print("AI Error:", str(e))

# Save report
filename = f"{symbol}_report.txt"
with open(filename, "w") as file:
    file.write(f"MARKET INTELLIGENCE REPORT\n")
    file.write(f"==========================\n")
    file.write(f"Symbol: {symbol}\n")
    file.write(f"Price: ${quote['05. price']}\n")
    file.write(f"Change: {quote['10. change percent']}\n")
    file.write(f"Date: {quote['07. latest trading day']}\n")
    file.write(f"\n--- AI Analysis ---\n")
    file.write(analysis)

print(f"\nReport saved as {filename}")