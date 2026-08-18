import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Ensure parent directory is in sys.path for relative imports
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from api.market import router as market_router

app = FastAPI(
    title="Quant Trading System API",
    description="Backend service providing real-time market data, indicators, and strategy execution.",
    version="1.0.0"
)

# Enable CORS for frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Next.js / React / Vite defaults
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(market_router)

@app.get("/")
def root():
    return {"status": "online", "message": "Quant Trading Backend API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)