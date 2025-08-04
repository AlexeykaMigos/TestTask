from typing import List, Optional
from pydantic import BaseModel

class TokenInfoResponse(BaseModel):
    name: str
    symbol: str
    decimals: int
    totalSupply: str
    formattedTotalSupply: str

class BalanceResponse(BaseModel):
    balance: str
    formattedBalance: str

class BalancesResponse(BaseModel):
    balances: List[str]
    formattedBalances: List[str]

class TopAddress(BaseModel):
    address: str
    balance: str
    formattedBalance: str

class TopAddressWithTx(TopAddress):
    lastTransactionDate: Optional[str] = None