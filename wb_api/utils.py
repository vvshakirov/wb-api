import datetime
import time
from datetime import datetime as dt


def validate_date(date: str):
    try:
        dt.fromisoformat(date)
    except ValueError:
        raise ValueError(
            "Дата должна быть в формате: 2019-06-20 | 2019-06-20T23:59:59 | 2019-06-20T00:00:00.12345 | 2017-03-25T00:00:00"
        )

def get_unix_date(date: str):
    validate_date(date)
    date_time = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    unix_date = int(time.mktime(date_time.timetuple()))
    return unix_date

def snake_to_camel_case(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.capitalize() for x in components[1:])
