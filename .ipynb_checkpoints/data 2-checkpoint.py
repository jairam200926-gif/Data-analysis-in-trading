import yfinance as yf

stock = "INFY.NS"

data = yf.download(
    stock,
    start="2025-01-01",
    end="2026-01-01",
    auto_adjust=False
)

print(data.head())