from fastapi import FastAPI
from src.handlers import get_balance, get_token_info, get_top_balance

app = FastAPI(
    title="polygon test",
    description="polygon test"
)

# Подключение роутеров
app.include_router(get_balance.router)
app.include_router(get_token_info.router)
app.include_router(get_top_balance.router)

@app.get("/")
def root():
    return {"message": "тестовое"}