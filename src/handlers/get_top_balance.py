from typing import List
from fastapi import APIRouter, HTTPException
from src.api.services import get_top_holders, get_top_holders_with_tx
from src.domain.entities import TopAddress, TopAddressWithTx

router = APIRouter(prefix="/top", tags=["Top Holders"])

@router.get("/", response_model=List[TopAddress])
async def get_top(n: int = 10):
    """Уровень C: Топ N держателей (заглушка)"""
    try:
        return get_top_holders(n)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))

@router.get("/with_tx", response_model=List[TopAddressWithTx])
async def get_top_with_tx(n: int = 10):
    """Уровень D: Топ с датой последней транзакции"""
    try:
        return get_top_holders_with_tx(n)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))