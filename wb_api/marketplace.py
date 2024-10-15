
from typing import Any, List, Optional
import json
from wb_api.base_api import BaseAPI
from wb_api.schemas.marketplace import (Order, OrderNew, Orders, OrdersNew)
from wb_api.utils import get_unix_date, validate_date, get_periods_by_month, date_iso


class Marketplace(BaseAPI):

    def __init__(self, wb_api) -> None:
        base_url: str = (
            "https://marketplace-api.wildberries.ru/api/{api_vers}"
        )
        super().__init__(api_client=wb_api, base_url=base_url)
    
    def get_orders_new(self, date_from: str, flag: Optional[int] = 0) -> List[Order]:
        """
        /api/v3/orders/new:
    servers:
      - url: https://marketplace-api.wildberries.ru
      - url: https://suppliers-api.wildberries.ru
        description: "**Deprecated URL**"
    get:
      security:
        - HeaderApiKey: [ ]
      tags:
        - Сборочные задания
      summary: Получить список новых сборочных заданий
      description: >
        Возвращает список всех новых сборочных заданий у продавца на данный момент.
      responses:
        200:
          description: Список сборочных заданий
          content:
            application/json:
              schema:
                type: object
                nullable: false
                properties:
                  orders:
                    type: array
                    nullable: false
                    description: Список новых сборочных заданий
                    items:
                      $ref: "#/components/schemas/OrderNew"
        401:
          $ref: "../../../../openapi/ru/responses/401.yaml"
        403:
          $ref: "#/components/responses/AccessDenied"
        429:
          $ref: "../../../../openapi/ru/responses/429.yaml"
        500:
          $ref: "#/components/responses/InternalServerError"
        """
        validate_date(date_from)

        data = self.get_data(
            endpoint="orders/new",
            # date_from=date_from,
            flag=flag,
            api_vers="v3"
        )
        print(json.dumps(data, indent=4, ensure_ascii=False))
        return OrdersNew(orders=data["orders"]).orders
    
    def get_orders(self, date_from: str, date_to: str, limit: int, next: int, flag: Optional[int] = 0) -> List[Order]:
        """
        /api/v3/orders:
    servers:
      - url: https://marketplace-api.wildberries.ru
      - url: https://suppliers-api.wildberries.ru
        description: "**Deprecated URL**"
    get:
      security:
        - HeaderApiKey: [ ]
      tags:
        - Сборочные задания
      summary: Получить информацию по сборочным заданиям
      description: >
        Возвращает информацию по сборочным заданиям без их актуального статуса.
        <br>Можно выгрузить данные за конкретный период, максимум 30 календарных дней
      parameters:
        - $ref: "#/components/parameters/Limit"
        - $ref: "#/components/parameters/Next"
        - name: dateFrom
          in: query
          schema:
            type: integer
          description: >
            Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до запроса
        - name: dateTo
          in: query
          schema:
            type: integer
          description: Дата конца периода в формате Unix timestamp
      responses:
        200:
          description: Список сборочных заданий
          content:
            application/json:
              schema:
                type: object
                nullable: false
                properties:
                  next:
                    $ref: "#/components/schemas/Next"
                  orders:
                    type: array
                    nullable: false
                    items:
                      $ref: "#/components/schemas/Order"
        400:
          description: Запрос содержит некорректные данные. Проверьте его на соответствие документации.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              examples:
                IncorrectParameter:
                  $ref: "#/components/examples/IncorrectParameter"
        401:
          $ref: "../../../../openapi/ru/responses/401.yaml"
        403:
          $ref: "#/components/responses/AccessDenied"
        429:
          $ref: "../../../../openapi/ru/responses/429.yaml"
        500:
          $ref: "#/components/responses/InternalServerError"
        """
        validate_date(date_from)
        validate_date(date_to)
        periods = get_periods_by_month(date_from, date_to)
        orders = []
        for period in periods:
            date_from = period["startDate"]
            date_to = period["endDate"]
            orders = orders + self.get_orders_pager(date_from=date_from, date_to=date_to, limit=1000)
        return orders
    

    def __get_orders_raw(self, date_from, date_to, limit: int = 1000, next: int = 0, flag: Optional[int] = 0) -> List[Order]:
        data = self.get_data(
            endpoint="orders",
            date_from=get_unix_date(date_from),
            date_to=get_unix_date(date_to),
            flag=flag,
            limit=limit,
            next=next,
            api_vers="v3"
        )
        print(json.dumps(data, indent=4, ensure_ascii=False))
        return data    

    def get_orders_pager(self, date_from: str, date_to: str, limit: int = 1000, next: int = 0, flag: Optional[int] = 0) -> List[Order]:
        data = self.__get_orders_raw(date_from=date_from, date_to=date_to, limit=limit, next=next, flag=flag)
        orders = data["orders"]
        if "next" in data:
             next = data["next"]
             while next != 0:
                data_add = self.__get_orders_raw(date_from=date_from, date_to=date_to, limit=limit, next=next, flag=flag)    
                orders = orders + data_add["orders"]
                next = data_add["next"]
        return Orders(orders=orders).orders
