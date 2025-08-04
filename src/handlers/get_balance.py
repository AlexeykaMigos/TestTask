from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.api.services import get_balance, get_balances
from src.domain.entities import BalanceResponse, BalancesResponse

router = APIRouter(prefix="/balance", tags=["Balance"])

class AddressesRequest(BaseModel):
    addresses: List[str]

@router.get("/{address}", response_model=BalanceResponse)
async def get_balance_endpoint(address: str):
    """Уровень A: Получить баланс одного адреса"""
    try:
        return get_balance(address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/batch", response_model=BalancesResponse)
async def get_balance_batch(request: AddressesRequest):
    """Уровень B: Получить баланс нескольких адресов"""
    return get_balances(request.addresses)