import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
vats = content.get_vat()  # or `content.get_nds()`

for vat in vats:
    print(vat)