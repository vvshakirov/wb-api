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


test_order = {
            "address": "null",
            "scanPrice": "null",
            "comment": "",
            "deliveryType": "fbs",
            "supplyId": "WB-GI-102905838",
            "orderUid": "23728742_8071471667969622833",
            "article": "AMDRyzen9/7950X3D",
            "colorCode": "",
            "rid": "8071471667969622833.0.0",
            "createdAt": "2024-08-20T18:10:06Z",
            "offices": [
                "Москва_Запад-Юг"
            ],
            "skus": [
                "2040414667220"
            ],
            "id": 2046647934,
            "warehouseId": 842562,
            "nmId": 238009160,
            "chrtId": 374533653,
            "price": 5789500,
            "convertedPrice": 5789500,
            "currencyCode": 643,
            "convertedCurrencyCode": 643,
            "cargoType": 1,
            "isZeroOrder":  "false"
        }

assert Order.model_validate(test_order)


marketplace = api.marketplace
# orders = marketplace.get_orders(date_from="2024-06-01", date_to="2024-10-10", limit=1000, next="0")
marketplace.get_sticker(order_id = 1831710692, type='png', width='58', height='40')
# orders = marketplace.get_orders_new(date_from="2024-06-01")

# for order in orders:
     #  print(order)
    # print(f'{order}')

#pager = marketplace.get_orders_pager(date_from="2024-08-31", date_to="2024-09-30", limit="1000", next="0") 