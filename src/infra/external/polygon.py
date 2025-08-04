import requests
import os
from datetime import datetime

POLYGONSCAN_API = "https://api.polygonscan.com/api"
POLYGONSCAN_API_KEY = os.getenv("POLYGONSCAN_API_KEY", "DGB3J9HZHGSWZB25PJH5XDB4NPJU3Q8RBP")
TOKEN_ADDRESS = "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0"

def get_last_transaction_date(address: str) -> str | None:
    try:
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": TOKEN_ADDRESS,
            "address": address,
            "sort": "desc",
            "apikey": POLYGONSCAN_API_KEY,
            "page": 1,
            "offset": 1
        }
        response = requests.get(POLYGONSCAN_API, params=params)
        data = response.json()

        if data["status"] == "1" and len(data["result"]) > 0:
            timestamp = int(data["result"][0]["timeStamp"])
            return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return None
    except Exception:
        return None