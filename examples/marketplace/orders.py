import os

from dotenv import load_dotenv

from wb_api import WBApi
from wb_api.schemas.marketplace import Order, OrderNew, Orders, OrdersNew

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=False)

marketplace = api.marketplace
orders = marketplace.get_orders(date_from="2024-08-31", date_to="2024-09-30", limit="1000", next="0")

for order in orders:
    #  print(order)
     print(f'{order.created_at.date()} {order.created_at.time()}')

#pager = marketplace.get_orders_pager(date_from="2024-08-31", date_to="2024-09-30", limit="1000", next="0")