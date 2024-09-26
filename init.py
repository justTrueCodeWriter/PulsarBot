import requests
import sys

contract_id = sys.argv[1] 

response =  requests.get(f"https://api.jup.ag/price/v2?ids={contract_id}")

data = response.json()
print(data["data"][contract_id]["price"])