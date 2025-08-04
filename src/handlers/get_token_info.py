from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from src.api.services import get_token_info
from src.domain.entities import TokenInfoResponse

router = APIRouter(prefix="/token", tags=["Token"])

@router.get("/", response_model=TokenInfoResponse)
async def get_token_info_endpoint():
    """Уровень E: Информация о токене"""
    try:
        return get_token_info()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/last_tx")
async def get_last_tx(address: str):
    """Уровень E: Дата последней транзакции"""
    from infra.external.polygon import get_last_transaction_date
    date = get_last_transaction_date(address)
    return {"address": address, "lastTransactionDate": date}