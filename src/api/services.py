from web3.exceptions import ContractLogicError
from src.infra.web import contract
from src.infra.web.web_client import w3
from src.domain.entities import BalanceResponse, BalancesResponse, TokenInfoResponse, TopAddress, TopAddressWithTx
from src.infra.external.polygon import get_last_transaction_date
from typing import List

def format_balance(raw_balance: int, decimals: int) -> str:
    return f"{raw_balance / (10 ** decimals):.18f}".rstrip('0').rstrip('.')

def get_token_decimals() -> int:
    try:
        return contract.functions.decimals().call()
    except ContractLogicError:
        return 18

def get_balance(address: str) -> BalanceResponse:
    try:
        checksum = w3.to_checksum_address(address)
        balance = contract.functions.balanceOf(checksum).call()
        decimals = get_token_decimals()
        return BalanceResponse(
            balance=str(balance),
            formattedBalance=format_balance(balance, decimals)
        )
    except Exception as e:
        raise ValueError(f"Ошибка при получении баланса: {str(e)}")

def get_balances(addresses: List[str]) -> BalancesResponse:
    balances = []
    formatted = []
    decimals = get_token_decimals()
    for addr in addresses:
        try:
            checksum = w3.to_checksum_address(addr)
            balance = contract.functions.balanceOf(checksum).call()
            balances.append(str(balance))
            formatted.append(format_balance(balance, decimals))
        except Exception:
            balances.append("0")
            formatted.append("0")
    return BalancesResponse(balances=balances, formattedBalances=formatted)

def get_token_info() -> TokenInfoResponse:
    try:
        name = contract.functions.name().call()
        symbol = contract.functions.symbol().call()
        decimals = contract.functions.decimals().call()
        total_supply = contract.functions.totalSupply().call()
        formatted_supply = format_balance(total_supply, decimals)
        return TokenInfoResponse(
            name=name,
            symbol=symbol,
            decimals=decimals,
            totalSupply=str(total_supply),
            formattedTotalSupply=formatted_supply
        )
    except Exception as e:
        raise ValueError(f"Ошибка при получении информации о токене: {str(e)}")

def get_top_holders(n: int = 10) -> List[TopAddress]:
    raise NotImplementedError(
        "Невозможно получить все адреса напрямую из контракта"
    )

def get_top_holders_with_tx(n: int = 10) -> List[TopAddressWithTx]:
    raise NotImplementedError(
        "Требуется индексация"
    )