import yfinance as yf

data = yf.download(
    "TCS.NS",
    start="2025-01-01",
    end="2026-01-01",
    auto_adjust=False
)

print(data.head())
