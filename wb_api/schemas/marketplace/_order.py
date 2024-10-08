from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Order(BaseModel):
    """

        Attributes:
        createdAt (datetime): Дата и время заказа. Это поле соответствует параметру dateFrom в запросе, если параметр flag=1.
                         Если часовой пояс не указан, то берется Московское время (UTC+3)

    Order:
        type: object
        properties:
            address:
                type: object
                nullable: true
                description: Детализованный адрес покупателя для доставки (если применимо).
                    Некоторые из полей могут прийти пустыми из-за специфики адреса
                properties:
                    fullAddress:
                        description: Адрес доставки.
                        type: string
                        example: Челябинская область, г. Челябинск, 51-я улица Арабкира, д.
                            10А, кв. 42
                    province:
                        type: string
                        nullable: false
                        description: Область
                        example: Челябинская область
                        deprecated: true
                    area:
                        type: string
                        nullable: false
                        description: Район
                        example: Челябинск
                        deprecated: true
                    city:
                        type: string
                        nullable: false
                        description: Город
                        example: Город
                        deprecated: true
                    street:
                        type: string
                        nullable: false
                        description: Улица
                        example: 51-я улица Арабкира
                        deprecated: true
                    home:
                        type: string
                        nullable: false
                        description: Номер дома
                        example: 10А
                        deprecated: true
                    flat:
                        type: string
                        nullable: false
                        description: Номер квартиры
                        example: '42'
                        deprecated: true
                    entrance:
                        type: string
                        nullable: false
                        description: Подъезд
                        example: '3'
                        deprecated: true
                    longitude:
                        type: number
                        format: float64
                        nullable: false
                        description: Координата долготы
                        example: 44.519068
                    latitude:
                        type: number
                        format: float64
                        nullable: false
                        description: Координаты широты
                        example: 40.20192
            scanPrice:
                type: number
                format: uint32
                description: Цена приёмки в копейках. Появляется после фактической приёмки заказа
                example: 1500
            deliveryType:
                type: string
                nullable: false
                description: '<dl>
                    <dt>Тип доставки:</dt>
                    <dd>fbs - доставка на склад Wildberries</dd>
                    <dd>dbs - доставка силами продавца</dd>
                    <dd>wbgo - доставка курьером WB</dd>
                    <dd>edbs - экспресс-доставка силами продавца</dd>
                    </dl>
                    '
                enum:
                    - dbs
                    - edbs
                    - fbs
                    - wbgo
            supplyId:
                type: string
                description: Идентификатор поставки. Возвращается, если заказ закреплён
                    за поставкой
                example: WB-GI-92937123
                orderUid:
                type: string
                description: Идентификатор транзакции для группировки сборочных заданий.
                    Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID
                example: 165918930_629fbc924b984618a44354475ca58675
            article:
                type: string
                nullable: false
                description: Артикул продавца
                example: one-ring-7548
            colorCode:
                type: string
                nullable: false
                description: Код цвета (только для колеруемых товаров)
                example: RAL 3017
            rid:
                type: string
                nullable: false
                description: Идентификатор сборочного задания в системе Wildberries
                example: f884001e44e511edb8780242ac120002
            createdAt:
                type: string
                format: date-time
                nullable: false
                description: Дата создания сборочного задания (RFC3339)
                example: '2022-05-04T07:56:29Z'
            offices:
                type: array
                nullable: true
                description: Список офисов, куда следует привезти товар
            items:
                type: string
                example: Калуга
            skus:
                type: array
                nullable: false
                description: Массив баркодов товара
                items:
                    type: string
                    example: '6665956397512'
            id:
                type: integer
                format: int64
                nullable: false
                description: Идентификатор сборочного задания в Маркетплейсе
                example: 13833711
            warehouseId:
                type: integer
                nullable: false
                description: Идентификатор склада продавца, на который поступило сборочное
                    задание
                example: 658434
            nmId:
                type: integer
                nullable: false
                description: Артикул WB
                example: 12345678
            chrtId:
            type: integer
                nullable: false
                description: Идентификатор размера товара в системе Wildberries
                example: 987654321
            price:
                type: integer
                nullable: false
                description: Цена в валюте продажи с учетом всех скидок, умноженная на 100.
                    Код валюты продажи в поле currencyCode.
                example: 1014
            convertedPrice:
                type: integer
                nullable: false
                description: Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.
                example: 28322
            currencyCode:
                type: integer
                nullable: false
                description: Код валюты продажи (ISO 4217)
                example: 933
            convertedCurrencyCode:
                type: integer
                nullable: false
                description: Код валюты страны продавца (ISO 4217)
                example: 643
            cargoType:
                type: integer
                nullable: false
                description: '<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ
                    (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не
                    используется на данный момент.</dd> </dl>

                    '
                enum:
                    - 1
                    - 2
                    - 3
            isZeroOrder:
                description: Признак заказа, сделанного на нулевой остаток товара. (<code>false</code> - заказ сделан на товар с ненулевым остатком, <code>true</code> - заказ сделан на товар с остатком равным нулю. Такой заказ можно отменить без штрафа за отмену)
                example: false
    """
    address: Any
    scan_price: int = Field(..., alias='scanPrice')
    comment: str
    delivery_type: str = Field(..., alias='deliveryType')
    supply_id: str = Field(..., alias='supplyId')
    order_uid: str = Field(..., alias='orderUid')
    article: str
    color_code: str = Field(..., alias='colorCode')
    rid: str
    created_at: datetime = Field(..., alias='createdAt')
    offices: List[str]
    skus: List[str]
    id: int
    warehouse_id: int = Field(..., alias='warehouseId', description="ID склада отгрузки")
    nm_id: int = Field(..., alias='nmId')
    chrt_id: int = Field(..., alias='chrtId')
    price: int
    converted_price: int = Field(..., alias='convertedPrice')
    currency_code: int = Field(..., alias='currencyCode')
    converted_currency_code: int = Field(..., alias='convertedCurrencyCode')
    cargo_type: int = Field(..., alias='cargoType')
    is_zero_order: bool = Field(..., alias='isZeroOrder')


    class Config:
        populate_by_name = True

class OrderNew(BaseModel):
    """
    OrderNew:
    type: object
    properties:       
    address:
        type: object
        nullable: true
        description: Детализованный адрес покупателя для доставки (если применимо).
        Некоторые из полей могут прийти пустыми из-за специфики адреса
        properties:
        fullAddress:
            description: Адрес доставки.
            type: string
            example: Челябинская область, г. Челябинск, 51-я улица Арабкира, д.
            10А, кв. 42
        province:
            type: string
            nullable: false
            description: Область
            example: ""
            deprecated: true
        area:
            type: string
            nullable: false
            description: Район
            example: ""
            deprecated: true
        city:
            type: string
            nullable: false
            description: Город
            example: ""
            deprecated: true
        street:
            type: string
            nullable: false
            description: Улица
            example: ""
            deprecated: true
        home:
            type: string
            nullable: false
            description: Номер дома
            example: ""
            deprecated: true
        flat:
            type: string
            nullable: false
            description: Номер квартиры
            example: ""
            deprecated: true
        entrance:
            type: string
            nullable: false
            description: Подъезд
            example: ""
            deprecated: true
        longitude:
            type: number
            format: float64
            nullable: false
            description: Координата долготы
            example: 44.519068
        latitude:
            type: number
            format: float64
            nullable: false
            description: Координаты широты
            example: 40.20192
    ddate:
        type: string
        description: |
        Планируемая дата доставки.<br> 
        Поле отображается для схем: <br> 
        dbs — доставка силами продавца <br> 
        edbs — экспресс-доставка силами продавца <br> 
        wbgo — доставка курьером WB <br> 
        СГТ — заказы сверхгабаритных товаров (<code>cargoType: 2</code>) для схем fbs — доставка на склад Wildberries — и dbs.
        nullable: false
        example: 17.05.2024
    dTimeFrom:
        type: string
        description: Время доставки "с".<br> Поле отображается только для edbs (экспресс-доставка силами продавца)
        example: 15:00
    dTimeTo:
        type: string
        description: Время доставки "до".<br> Поле отображается только для edbs (экспресс-доставка силами продавца)
        example: 16:00
    requiredMeta:
        description: "Перечень метаданных, которые необходимо добавить в сборочное
        задание.  <br> На данный момент обязательным к добавлению является только
        UIN, при его наличии в перечне.             \n"
        type: array
        items:
        type: string
        example:
        - uin
    deliveryType:
        type: string
        nullable: false
        description: '<dl>

        <dt>Тип доставки:</dt>

        <dd>fbs - доставка на склад Wildberries</dd>

        <dd>dbs - доставка силами продавца</dd>

        <dd>edbs - экспресс-доставка силами продавца</dd>

        <dd>wbgo - доставка курьером WB</dd>

        </dl>

        '
        enum:
        - dbs
        - fbs
        - edbs
        - wbgo
    scanPrice:
        description: Цена приёмки в копейках. Появляется после фактической приёмки заказа. Для данного метода всегда будет возвращаться null
        type: number
        format: uint32
        nullable: true
        example: null
    orderUid:
        type: string
        description: Идентификатор транзакции для группировки сборочных заданий.
        Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID
        example: 165918930_629fbc924b984618a44354475ca58675
    article:
        type: string
        nullable: false
        description: Артикул продавца
        example: one-ring-7548
    colorCode:
        description: Код цвета (только для колеруемых товаров)
        type: string
        nullable: false
        example: RAL 3017
    rid:
        type: string
        nullable: false
        description: Идентификатор сборочного задания в системе Wildberries
        example: f884001e44e511edb8780242ac120002
    createdAt:
        type: string
        format: date-time
        nullable: false
        description: Дата создания сборочного задания (RFC3339)
        example: '2022-05-04T07:56:29Z'
    offices:
        type: array
        nullable: true
        description: Список офисов, куда следует привезти товар
        items:
        type: string
        example: Калуга
    skus:
        type: array
        nullable: false
        description: Массив баркодов товара
        items:
        type: string
        example: '6665956397512'
    id:
        type: integer
        format: int64
        nullable: false
        description: Идентификатор сборочного задания в Маркетплейсе
        example: 13833711
    warehouseId:
        type: integer
        nullable: false
        description: Идентификатор склада продавца, на который поступило сборочное
        задание
        example: 658434
    nmId:
        type: integer
        nullable: false
        description: Артикул WB
        example: 123456789
    chrtId:
        type: integer
        nullable: false
        description: Идентификатор размера товара в системе Wildberries
        example: 987654321
    price:
        type: integer
        nullable: false
        description: Цена в валюте продажи с учетом всех скидок, умноженная на 100.
        Код валюты продажи в поле currencyCode.
        example: 1014
    convertedPrice:
        type: integer
        nullable: false
        description: Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.
        example: 28322
    currencyCode:
        type: integer
        nullable: false
        description: Код валюты продажи (ISO 4217)
        example: 933
    convertedCurrencyCode:
        type: integer
        nullable: false
        description: Код валюты страны продавца (ISO 4217)
        example: 643
    cargoType:
        type: integer
        nullable: false
        description: '<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ
        (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не
        используется на данный момент.</dd> </dl>

        '
        enum:
        - 1
        - 2
        - 3
    isZeroOrder:
        description: Признак заказа, сделанного на нулевой остаток товара. (<code>false</code> - заказ сделан на товар с ненулевым остатком, <code>true</code> - заказ сделан на товар с остатком равным нулю. Такой заказ можно отменить без штрафа за отмену)
        example: false
    """

class Orders(BaseModel):
    orders: List[Order]
    #orders: List[Order] 
    # orders: List[Order] = Field(
    #     ...,
    #     alias="orders",
    #     description="Заказы",
    # ) 
    #next: int = Field(..., alias="next", description="Пайджер")

class OrdersPager(BaseModel):
    orders: List[Order]
    next: int


class OrdersNew(BaseModel):
    orders: List[OrderNew]