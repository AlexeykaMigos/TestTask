from web3 import Web3
import os

POLYGON_RPC = os.getenv("POLYGON_RPC", "https://polygon-rpc.com")

w3 = Web3(Web3.HTTPProvider(POLYGON_RPC, request_kwargs={"timeout": 10}))

if not w3.is_connected():
    raise Exception("Не удалось подклюычиться к polygonRPC")