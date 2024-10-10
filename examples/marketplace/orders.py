import os

from dotenv import load_dotenv

from wb_api import WBApi
from wb_api.schemas.marketplace import Order, OrderNew, Orders, OrdersNew

load_dotenv()
test_mode = False
#Используемый токен не применим к данным методам
if test_mode == True :
    print(os.getenv("API_TOKEN_TEST"))
    api = WBApi(api_key=os.getenv("API_TOKEN_TEST"), test_mode=False)
else:
    api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=False)
print(f"Test mode: {api.test_mode}")

marketplace = api.marketplace
# orders = marketplace.get_orders(date_from="2024-06-01", date_to="2024-10-10", limit=1, next="0")
orders = marketplace.get_orders_new(date_from="2024-06-01")

for order in orders:
     #  print(order)
    print(f'{order.created_at.date()} {order.created_at.time()}')

#pager = marketplace.get_orders_pager(date_from="2024-08-31", date_to="2024-09-30", limit="1000", next="0") 