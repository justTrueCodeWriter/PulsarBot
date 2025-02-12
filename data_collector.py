import requests
from dataclasses import dataclass

@dataclass
class DataCollector:
    chain_id: str
    dex_id: str
    descreener_url: str
    open_graph_url: str
    token_address: str
    token_name: str
    token_symbol: str
    price_usd: str


def collect_data(chainId: str, tokenAddress: str) -> DataCollector:
    response = requests.get(
    f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}",
    headers={},
    )
    data = response.json()

    data_collector = DataCollector(
        chain_id = data[0]["chainId"],
        dex_id = data[0]["dexId"],
        descreener_url = data[0]["url"],
        open_graph_url = data[0]["info"]["openGraph"],
        token_address = data[0]["baseToken"]["address"],
        token_name = data[0]["baseToken"]["name"],
        token_symbol = data[0]["baseToken"]["symbol"],
        price_usd = data[0]["priceUsd"],
    )
    
    return data_collector
