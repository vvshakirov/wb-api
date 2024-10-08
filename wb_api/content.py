from typing import List, Optional


from wb_api.base_api import BaseAPI
from wb_api.enum import Locale
from wb_api.schemas.content.charc import Charc, Charcs
from wb_api.schemas.content.color import Color, Colors
from wb_api.schemas.content.country import Countries, Country
from wb_api.schemas.content.subject import Subject, Subjects
from wb_api.schemas.content.tnved import TNVED, TNVEDs
from wb_api.schemas.content import Parent, Parents


class Content(BaseAPI):
    def __init__(self, wb_api) -> None:
        base_url: str = "https://content-api{sandbox}.wildberries.ru/content/{api_vers}"
        super().__init__(api_client=wb_api, base_url=base_url)

    def get_all_parents(self, locale: Locale = Locale.RU) -> List[Parent]:
        """
        С помощью данного метода можно получить список всех родительских категорий товаров.

        Args:
            locale (Locale, optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений поля name. Не используется в песочнице
        """
        data = self.get_data(endpoint="object/parent/all", locale=locale)
        if not data["error"]:
            return Parents(parents=data["data"]).parents

    def get_all_subjects(
        self,
        name: Optional[str] = None,
        limit: Optional[int] = None,
        locale: Optional[Locale] = Locale.RU,
        offset: Optional[int] = None,
        parent_id: Optional[int] = None,
    ) -> List[Subject]:
        """
        С помощью данного метода можно получить список всех доступных предметов, родительских категорий предметов, и их идентификаторов.

        Args:
            name (Optional[str], optional):
                Поиск по наименованию предмета (Носки), поиск работает по подстроке, искать можно на любом из поддерживаемых языков.

            limit (Optional[int], optional):
                Количество подкатегорий (предметов), максимум 1 000

            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Язык полей ответа ("ru", "en", "zh"). Не используется в песочнице

            offset (Optional[int], optional):
                Номер позиции, с которой необходимо получить ответ

            parent_id (Optional[int], optional):
                Номер позиции, с которой необходимо получить ответ
        """
        data = self.get_data(
            endpoint="object/all",
            name=name,
            limit=limit,
            locale=locale,
            offset=offset,
            parent_id=parent_id,
        )
        if not data["error"]:
            return Subjects(subjects=data["data"]).subjects

    def get_charcs(
        self,
        subject_id: int,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[Charc]:
        """
        Получение списка характеристик предмета по его ID.

        Args:
            subject_id (int):
                Идентификатор предмета
            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint=f"object/charcs/{subject_id}",
            locale=locale,
        )
        if not data["error"]:
            return Charcs(charcs=data["data"]).charcs

    def get_colors(
        self,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[Color]:
        """
        Получение значения характеристики цвет.

        Args:
            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/colors",
            locale=locale,
        )
        if not data["error"]:
            return Colors(colors=data["data"]).colors

    def get_kinds(
        self,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[str]:
        """
        Получение значения характеристики пол.

        Args:
            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/kinds",
            locale=locale,
        )
        if not data["error"]:
            return data["data"]

    def get_countries(
        self,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[Country]:
        """
        Получение значения характеристики Страна Производства.

        Args:
            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/countries",
            locale=locale,
        )
        if not data["error"]:
            return Countries(countries=data["data"]).countries

    def get_seasons(
        self,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[str]:
        """
        Получение значения характеристики Сезон.

        Args:
            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/seasons",
            locale=locale,
        )
        if not data["error"]:
            return data["data"]

    def get_tnved(
        self,
        subject_ID: int,
        search: Optional[int] = None,
        locale: Optional[Locale] = Locale.RU,
    ) -> List[TNVED]:
        """
        С помощью данного метода можно получить список ТНВЭД кодов по ID предмета и фильтру по ТНВЭД коду.

        Args:
            subject_ID (int):
                Идентификатор предмета

            search (int):
                Поиск по ТНВЭД-коду. Работает только в паре с subjectID

            locale (Optional[Locale], optional): Defaults to `Locale.RU`.

                Параметр выбора языка ("ru", "en", "zh") значений полей `subjectName`, `name`. Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/tnved",
            subject_ID=subject_ID,
            search=search,
            locale=locale,
        )
        if not data["error"]:
            return TNVEDs(tnveds=data["data"]).tnveds

    def get_nds(
        self,
        locale: Locale = Locale.RU,
    ) -> List[str]:
        """
        Алиас для метода `get_vat` (список значений Ставка НДС)

        Args:
            locale (Locale, optional): Defaults to Locale.RU.
                Язык значения элементов data ("ru", "en", "zh"). Не используется в песочнице
        """
        return self.get_vat(locale=locale)

    def get_vat(
        self,
        locale: Locale = Locale.RU,
    ) -> List[str]:
        """
        С помощью данного метода можно получить список значений для характеристики Ставка НДС.

        Args:
            locale (Locale, optional): Defaults to Locale.RU.
                Язык значения элементов data ("ru", "en", "zh"). Не используется в песочнице
        """
        data = self.get_data(
            endpoint="directory/vat",
            locale=locale,
        )
        if not data["error"]:
            return data["data"]
