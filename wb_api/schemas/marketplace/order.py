# generated by datamodel-codegen:
#   filename:  wb.yaml
#   timestamp: 2024-10-08T05:01:46+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Dict, List, Optional, TypeAlias

from pydantic import BaseModel, BeforeValidator, Field, constr, field_validator


def _null_str_to_none(v: str | None) -> None:
    if v is None:
        return None
    if v == 'null' or v == '':
        return None
    raise ValueError('Value is not empty') # Not str or None, Fall to next type. e.g. Decimal, or a non-empty str

NullStrToNone = Annotated[None, BeforeValidator(_null_str_to_none)]

class Error(BaseModel):
    code: Optional[str] = Field(None, description='Код ошибки')
    message: Optional[str] = Field(None, description='Описание ошибки')
    data: Optional[Dict[str, Any]] = Field(
        None, description='Дополнительные данные, обогощающие ошибку'
    )


class CrossborderTurkeyClientInfo(BaseModel):
    firstName: Optional[str] = Field(None, description='Имя клиента', example='Иван')
    fullName: Optional[str] = Field(
        None, description='Фамилия, Имя, Отчество', example='Андреев Иван Васильевич'
    )
    lastName: Optional[str] = Field(
        None, description='Фамилия клиента', example='Андреев'
    )
    middleName: Optional[str] = Field(
        None, description='Отчество клиента', example='Васильевич'
    )
    orderID: Optional[int] = Field(None, description='Номер заказа', example=134567)
    phone: Optional[str] = Field(
        None, description='Телефон для связи с клиентом', example=79871234567
    )
    phoneCode: Optional[str] = Field(None, description='Не используется', example=0)


class DbsClientInfo(BaseModel):
    firstName: Optional[str] = Field(None, description='Имя клиента')
    fullName: Optional[str] = Field(
        None,
        description='Полное имя, используется для оформления документов. Например, документы для автомобиля.',
        example='Иван Иван Иванович',
    )
    orderID: Optional[int] = Field(None, description='Номер заказа', example=134567)
    phone: Optional[str] = Field(
        None,
        description='Телефон для связи с клиентом. <br> Чтобы связаться с клиентом наберите этот номер и введите добавочный код. <br> Даный номер не является прямым номером клиента.',
        example=79871234567,
    )
    phoneCode: Optional[str] = Field(
        None, description='Добавочный код', example=1234567
    )


class CrossborderTurkeyClientInfoResp(BaseModel):
    orders: Optional[List[CrossborderTurkeyClientInfo]] = Field(
        None, description='Информация по клиенту для кроссбордер-заказа из Турции'
    )


class DbsClientInfoResp(BaseModel):
    orders: Optional[List[DbsClientInfo]] = Field(
        None,
        description='Информация по клиенту для dbs-заказа (доставка силами продавца)',
    )


class OrdersRequestAPI(BaseModel):
    orders: Optional[List[int]] = Field(None, description='Список заказов')


class Code(BaseModel):
    code: Optional[str] = Field(None, description='Код клиентской доставки')


class PassOffice(BaseModel):
    name: Optional[str] = Field(None, description='Название', example='Коледино')
    address: Optional[str] = Field(
        None, description='Адрес', example='г. Подольск, д. Коледино, ул. Троицкая'
    )
    id: Optional[int] = Field(None, description='ID', example=1)


class CargoType(Enum):
    integer_0 = 0
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class Supply(BaseModel):
    id: Optional[str] = Field(
        None, description='Идентификатор поставки', example='WB-GI-1234567'
    )
    done: Optional[bool] = Field(None, description='Флаг закрытия поставки')
    createdAt: Optional[datetime] = Field(
        None,
        description='Дата создания поставки (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    closedAt: Optional[datetime] = Field(
        None,
        description='Дата закрытия поставки (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    scanDt: Optional[datetime] = Field(
        None,
        description='Дата скана поставки (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    name: Optional[str] = Field(
        None, description='Наименование поставки', example='Тестовая поставка'
    )
    cargoType: Optional[CargoType] = Field(
        None,
        description='<dl> <dt>Тип поставки:</dt> <dd>0 - признак отсутствует</dd> <dd>1 - обычная</dd> <dd>2 - СГТ (Содержит сверхгабаритные товары)</dd> <dd>3 - КГТ (Содержит крупногабаритные товары). Не используется на данный момент.</dd> </dl>\n',
    )


class Next(BaseModel):
    root: int = Field(
        ...,
        description='Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения следующего пакета данных',
        example=13833711,
    )


class Address(BaseModel):
    fullAddress: Optional[str] = Field(
        None,
        description='Адрес доставки.',
        example='Челябинская область, г. Челябинск, 51-я улица Арабкира, д. 10А, кв. 42',
    )
    province: Optional[str] = Field(
        None, description='Область', example='Челябинская область'
    )
    area: Optional[str] = Field(None, description='Район', example='Челябинск')
    city: Optional[str] = Field(None, description='Город', example='Город')
    street: Optional[str] = Field(
        None, description='Улица', example='51-я улица Арабкира'
    )
    home: Optional[str] = Field(None, description='Номер дома', example='10А')
    flat: Optional[str] = Field(None, description='Номер квартиры', example='42')
    entrance: Optional[str] = Field(None, description='Подъезд', example='3')
    longitude: Optional[float] = Field(
        None, description='Координата долготы', example=44.519068
    )
    latitude: Optional[float] = Field(
        None, description='Координаты широты', example=40.20192
    )


class DeliveryType(Enum):
    dbs = 'dbs'
    edbs = 'edbs'
    fbs = 'fbs'
    wbgo = 'wbgo'


class CargoType1(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class Order(BaseModel):
    

    address: Optional[Address | NullStrToNone] = Field(
        None,
        description='Детализованный адрес покупателя для доставки (если применимо). Некоторые из полей могут прийти пустыми из-за специфики адреса',
    )
    scanPrice: Optional[int | NullStrToNone]  = Field(
        None,
        description='Цена приёмки в копейках. Появляется после фактической приёмки заказа',
        example=1500,
    )
    deliveryType: Optional[DeliveryType] = Field(
        None,
        description='<dl>\n<dt>Тип доставки:</dt>\n<dd>fbs - доставка на склад Wildberries</dd>\n<dd>dbs - доставка силами продавца</dd>\n<dd>wbgo - доставка курьером WB</dd>\n<dd>edbs - экспресс-доставка силами продавца</dd>\n</dl>\n',
    )
    supplyId: Optional[str] = Field(
        None,
        description='Идентификатор поставки. Возвращается, если заказ закреплён за поставкой',
        example='WB-GI-92937123',
    )
    orderUid: Optional[str] = Field(
        None,
        description='Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID',
        example='165918930_629fbc924b984618a44354475ca58675',
    )
    article: Optional[str] = Field(
        None, description='Артикул продавца', example='one-ring-7548'
    )
    colorCode: Optional[str] = Field(
        None,
        description='Код цвета (только для колеруемых товаров)',
        example='RAL 3017',
    )
    rid: Optional[str] = Field(
        None,
        description='Идентификатор сборочного задания в системе Wildberries',
        example='f884001e44e511edb8780242ac120002',
    )
    createdAt: Optional[datetime] = Field(
        None,
        description='Дата создания сборочного задания (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    offices: Optional[List[str]] = Field(
        None, description='Список офисов, куда следует привезти товар'
    )
    skus: Optional[List[str]] = Field(None, description='Массив баркодов товара')
    id: Optional[int] = Field(
        None,
        description='Идентификатор сборочного задания в Маркетплейсе',
        example=13833711,
    )
    warehouseId: Optional[int] = Field(
        None,
        description='Идентификатор склада продавца, на который поступило сборочное задание',
        example=658434,
    )
    nmId: Optional[int] = Field(None, description='Артикул WB', example=12345678)
    chrtId: Optional[int] = Field(
        None,
        description='Идентификатор размера товара в системе Wildberries',
        example=987654321,
    )
    price: Optional[int] = Field(
        None,
        description='Цена в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи в поле currencyCode.',
        example=1014,
    )
    convertedPrice: Optional[int] = Field(
        None,
        description='Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.',
        example=28322,
    )
    currencyCode: Optional[int] = Field(
        None, description='Код валюты продажи (ISO 4217)', example=933
    )
    convertedCurrencyCode: Optional[int] = Field(
        None, description='Код валюты страны продавца (ISO 4217)', example=643
    )
    cargoType: Optional[CargoType1] = Field(
        None,
        description='<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl>\n',
    )
    isZeroOrder: Optional[Any] = Field(
        None,
        description='Признак заказа, сделанного на нулевой остаток товара. (<code>false</code> - заказ сделан на товар с ненулевым остатком, <code>true</code> - заказ сделан на товар с остатком равным нулю. Такой заказ можно отменить без штрафа за отмену)',
        example=False,
    )
    class Config:
        populate_by_name = True

class Address1(BaseModel):
    fullAddress: Optional[str] = Field(
        None,
        description='Адрес доставки.',
        example='Челябинская область, г. Челябинск, 51-я улица Арабкира, д. 10А, кв. 42',
    )
    province: Optional[str] = Field(None, description='Область', example='')
    area: Optional[str] = Field(None, description='Район', example='')
    city: Optional[str] = Field(None, description='Город', example='')
    street: Optional[str] = Field(None, description='Улица', example='')
    home: Optional[str] = Field(None, description='Номер дома', example='')
    flat: Optional[str] = Field(None, description='Номер квартиры', example='')
    entrance: Optional[str] = Field(None, description='Подъезд', example='')
    longitude: Optional[float] = Field(
        None, description='Координата долготы', example=44.519068
    )
    latitude: Optional[float] = Field(
        None, description='Координаты широты', example=40.20192
    )


class DeliveryType1(Enum):
    dbs = 'dbs'
    fbs = 'fbs'
    edbs = 'edbs'
    wbgo = 'wbgo'


class OrderNew(BaseModel):
    address: Optional[Address1 | NullStrToNone] = Field(
        None,
        description='Детализованный адрес покупателя для доставки (если применимо). Некоторые из полей могут прийти пустыми из-за специфики адреса',
    )
    ddate: Optional[str] = Field(
        None,
        description='Планируемая дата доставки.<br> \nПоле отображается для схем: <br> \ndbs — доставка силами продавца <br> \nedbs — экспресс-доставка силами продавца <br> \nwbgo — доставка курьером WB <br> \nСГТ — заказы сверхгабаритных товаров (<code>cargoType: 2</code>) для схем fbs — доставка на склад Wildberries — и dbs.\n',
        example='17.05.2024',
    )
    dTimeFrom: Optional[str] = Field(
        None,
        description='Время доставки "с".<br> Поле отображается только для edbs (экспресс-доставка силами продавца)',
        example=900,
    )
    dTimeTo: Optional[str] = Field(
        None,
        description='Время доставки "до".<br> Поле отображается только для edbs (экспресс-доставка силами продавца)',
        example=960,
    )
    requiredMeta: Optional[List[str]] = Field(
        None,
        description='Перечень метаданных, которые необходимо добавить в сборочное задание.  <br> На данный момент обязательным к добавлению является только UIN, при его наличии в перечне.             \n',
        example=['uin'],
    )
    deliveryType: Optional[DeliveryType1] = Field(
        None,
        description='<dl>\n<dt>Тип доставки:</dt>\n<dd>fbs - доставка на склад Wildberries</dd>\n<dd>dbs - доставка силами продавца</dd>\n<dd>edbs - экспресс-доставка силами продавца</dd>\n<dd>wbgo - доставка курьером WB</dd>\n</dl>\n',
    )
    scanPrice: Optional[int | NullStrToNone] = Field(
        None,
        description='Цена приёмки в копейках. Появляется после фактической приёмки заказа. Для данного метода всегда будет возвращаться null',
    )
    orderUid: Optional[str] = Field(
        None,
        description='Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID',
        example='165918930_629fbc924b984618a44354475ca58675',
    )
    article: Optional[str] = Field(
        None, description='Артикул продавца', example='one-ring-7548'
    )
    colorCode: Optional[str] = Field(
        None,
        description='Код цвета (только для колеруемых товаров)',
        example='RAL 3017',
    )
    rid: Optional[str] = Field(
        None,
        description='Идентификатор сборочного задания в системе Wildberries',
        example='f884001e44e511edb8780242ac120002',
    )
    createdAt: Optional[datetime] = Field(
        None,
        description='Дата создания сборочного задания (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    offices: Optional[List[str]] = Field(
        None, description='Список офисов, куда следует привезти товар'
    )
    skus: Optional[List[str]] = Field(None, description='Массив баркодов товара')
    id: Optional[int] = Field(
        None,
        description='Идентификатор сборочного задания в Маркетплейсе',
        example=13833711,
    )
    warehouseId: Optional[int] = Field(
        None,
        description='Идентификатор склада продавца, на который поступило сборочное задание',
        example=658434,
    )
    nmId: Optional[int] = Field(None, description='Артикул WB', example=123456789)
    chrtId: Optional[int] = Field(
        None,
        description='Идентификатор размера товара в системе Wildberries',
        example=987654321,
    )
    price: Optional[int] = Field(
        None,
        description='Цена в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи в поле currencyCode.',
        example=1014,
    )
    convertedPrice: Optional[int] = Field(
        None,
        description='Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.',
        example=28322,
    )
    currencyCode: Optional[int] = Field(
        None, description='Код валюты продажи (ISO 4217)', example=933
    )
    convertedCurrencyCode: Optional[int] = Field(
        None, description='Код валюты страны продавца (ISO 4217)', example=643
    )
    cargoType: Optional[CargoType1] = Field(
        None,
        description='<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl>\n',
    )
    isZeroOrder: Optional[Any] = Field(
        None,
        description='Признак заказа, сделанного на нулевой остаток товара. (<code>false</code> - заказ сделан на товар с ненулевым остатком, <code>true</code> - заказ сделан на товар с остатком равным нулю. Такой заказ можно отменить без штрафа за отмену)',
        example=False,
    )
    class Config:
        populate_by_name = True


class SupplyOrder(BaseModel):
    scanPrice: Optional[float] = Field(
        None,
        description='Цена приёмки в копейках. Появляется после фактической приёмки заказа. Для данного метода всегда будет возвращаться null',
    )
    orderUid: Optional[str] = Field(
        None,
        description='Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID',
        example='165918930_629fbc924b984618a44354475ca58675',
    )
    article: Optional[str] = Field(
        None, description='Артикул продавца', example='one-ring-7548'
    )
    colorCode: Optional[str] = Field(
        None,
        description='Код цвета (только для колеруемых товаров)',
        example='RAL 3017',
    )
    rid: Optional[str] = Field(
        None,
        description='Идентификатор сборочного задания в системе Wildberries',
        example='f884001e44e511edb8780242ac120002',
    )
    createdAt: Optional[datetime] = Field(
        None,
        description='Дата создания сборочного задания (RFC3339)',
        example='2022-05-04T07:56:29Z',
    )
    offices: Optional[List[str]] = Field(
        None, description='Список офисов, куда следует привезти товар'
    )
    skus: Optional[List[str]] = Field(None, description='Массив баркодов товара')
    id: Optional[int] = Field(
        None,
        description='Идентификатор сборочного задания в Маркетплейсе',
        example=13833711,
    )
    warehouseId: Optional[int] = Field(
        None,
        description='Идентификатор склада продавца, на который поступило сборочное задание',
        example=658434,
    )
    nmId: Optional[int] = Field(None, description='Артикул WB', example=123456789)
    chrtId: Optional[int] = Field(
        None,
        description='Идентификатор размера товара в системе Wildberries',
        example=987654321,
    )
    price: Optional[int] = Field(
        None,
        description='Цена в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи в поле currencyCode.',
        example=1014,
    )
    convertedPrice: Optional[int] = Field(
        None,
        description='Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.',
        example=28322,
    )
    currencyCode: Optional[int] = Field(
        None, description='Код валюты продажи (ISO 4217)', example=933
    )
    convertedCurrencyCode: Optional[int] = Field(
        None, description='Код валюты страны продавца (ISO 4217)', example=643
    )
    cargoType: Optional[CargoType1] = Field(
        None,
        description='<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl>\n',
    )
    isZeroOrder: Optional[Any] = Field(
        None,
        description='Признак заказа, сделанного на нулевой остаток товара. (<code>false</code> - заказ сделан на товар с ненулевым остатком, <code>true</code> - заказ сделан на товар с остатком равным нулю. Такой заказ можно отменить без штрафа за отмену)',
        example=False,
    )


class SupplyTrbx(BaseModel):
    id: Optional[str] = Field(None, description='ID короба.', example='WB-TRBX-1234567')
    orders: Optional[List[int]] = Field(
        None, description='Массив идентификаторов заказа.'
    )


class TrbxStickers(BaseModel):
    barcode: Optional[constr(min_length=1)] = Field(
        None,
        description='Закодированное значение этикетки.',
        example='$WBMP:1:123:1234567',
    )
    file: Optional[str] = Field(
        None,
        description='Полное представление этикетки в заданном формате. (кодировка base64)',
        example='U3dhZ2dlciByb2Nrcw==',
    )

class Sticker(BaseModel):
    partA: Optional[constr(min_length=7)] = Field(
        None,
        description='Первая часть номера 7 цифр',
        example='2180097',
    )

    partB: Optional[constr(min_length=4)] = Field(
        None,
        description='Вторая часть номера 4 цифры',
        example='4565',
    )
    
    barcode: Optional[constr(min_length=1)] = Field(
        None,
        description='Закодированное значение этикетки.',
        example='$WBMP:1:123:1234567',
    )
    file: Optional[str] = Field(
        None,
        description='Полное представление этикетки в заданном формате. (кодировка base64)',
        example='U3dhZ2dlciByb2Nrcw==',
    )


class DeliveryType2(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class Office(BaseModel):
    address: Optional[str] = Field(
        None, description='Адрес', example='ул. Троицкая, Подольск, Московская обл.'
    )
    name: Optional[str] = Field(
        None, description='Название', example='Москва (Коледино)'
    )
    city: Optional[str] = Field(None, description='Город', example='Москва')
    id: Optional[int] = Field(None, description='ID', example=15)
    longitude: Optional[float] = Field(None, description='Долгота', example=55.386871)
    latitude: Optional[float] = Field(None, description='Широта', example=37.588898)
    cargoType: Optional[CargoType1] = Field(
        None,
        description='<dl> <dt>Тип товара, который принимает склад:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl>\n',
        example=1,
    )
    deliveryType: Optional[DeliveryType2] = Field(
        None,
        description='<dl>\n<dt>Тип доставки, который принимает склад:</dt>\n<dd>1 - доставка на склад Wildberries</dd>\n<dd>2 - доставка силами продавца</dd>\n<dd>3 - доставка курьером WB</dd>\n</dl>\n',
        example=1,
    )
    selected: Optional[bool] = Field(
        None, description='Признак того, что склад уже выбран продавцом'
    )


class Warehouse(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Название склада продавца',
        example='ул. Троицкая, Подольск, Московская обл.',
    )
    officeId: Optional[int] = Field(None, description='ID склада WB', example=15)
    id: Optional[int] = Field(None, description='ID склада продавца', example=1)
    cargoType: Optional[CargoType1] = Field(
        None,
        description='<dl> <dt>Тип товара, который принимает склад:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl>\n',
        example=1,
    )
    deliveryType: Optional[DeliveryType2] = Field(
        None,
        description='<dl>\n<dt>Тип доставки, который принимает склад:</dt>\n<dd>1 - доставка на склад Wildberries</dd>\n<dd>2 - доставка силами продавца</dd>\n<dd>3 - доставка курьером WB</dd>\n</dl>\n',
        example=1,
    )


class Meta(BaseModel):
    imei: Optional[str] = Field(None, description='IMEI', example=123456789012345)
    uin: Optional[str] = Field(None, description='УИН', example=1234567890123456)
    gtin: Optional[str] = Field(None, description='GTIN', example=1234567890123)
    sgtin: Optional[str] = Field(
        None, description='КиЗ (Маркировка честного знака)', example=1234567890123456
    )


class Pass(BaseModel):
    firstName: Optional[str] = Field(
        None, description='Имя водителя', example='Александр'
    )
    dateEnd: Optional[str] = Field(
        None,
        description='Дата окончания действия пропуска',
        example='2022-07-31 17:53:13+00:00',
    )
    lastName: Optional[str] = Field(
        None, description='Фамилия водителя', example='Петров'
    )
    carModel: Optional[str] = Field(
        None, description='Марка машины', example='Lamborghini'
    )
    carNumber: Optional[str] = Field(
        None, description='Номер машины', example='A456BC123'
    )
    officeName: Optional[str] = Field(
        None, description='Название склада', example='Коледино'
    )
    officeAddress: Optional[str] = Field(
        None,
        description='Адрес склада',
        example='г. Подольск, д. Коледино, ул. Троицкая',
    )
    officeId: Optional[int] = Field(None, description='ID склада', example=15)
    id: Optional[int] = Field(None, description='ID пропуска', example=1)

class Orders(BaseModel):
    orders: List[Order]

class OrdersNew(BaseModel):
    orders: List[OrderNew]