import datetime
import time
from datetime import datetime as dt
from datetime import timedelta

def validate_date(date: str):
    try:
        dt.fromisoformat(date)
    except ValueError:
        raise ValueError(
            "Дата должна быть в формате: 2019-06-20 | 2019-06-20T23:59:59 | 2019-06-20T00:00:00.12345 | 2017-03-25T00:00:00"
        )

def date_iso(date: str):
    try:
        isodate = dt.fromisoformat(date)
    except ValueError:
        raise ValueError(
            "Дата должна быть в формате: 2019-06-20 | 2019-06-20T23:59:59 | 2019-06-20T00:00:00.12345 | 2017-03-25T00:00:00"
        )
    return isodate

def get_unix_date(date_time):
    # validate_date(date)
    # date_time = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    unix_date = int(time.mktime(date_time.timetuple()))
    return unix_date

#возвращает массим переодов дат
def get_periods_by_month_unix(startDate, endDate, days=30):
    periods = []
    # timeDelta = 
    periodDate = endDate - startDate
    print (f"{periodDate.days}, {days}")
    if periodDate.days <= days:
        periods.append({"startDate": int(time.mktime(startDate.date().timetuple())), "endDate": endDate.date()})
        return periods
    else:
        periodStart = startDate
        periodEnd = startDate + timedelta(days=days)
        while periodEnd <= endDate:
            periods.append({"startDate": int(time.mktime(periodStart.date().timetuple())), "endDate": int(time.mktime(periodEnd.date().timetuple()))})
            periodStart = periodEnd + timedelta(days=1)
            periodEnd = periodStart + timedelta(days=days)
        periods.append({"startDate": int(time.mktime(periodStart.date().timetuple())), "endDate": int(time.mktime(periodEnd.date().timetuple()))})
        return periods 

#возвращает массим переодов дат
def get_periods_by_month(start_date, end_date, days=30):
    validate_date(start_date)
    validate_date(end_date)
    start_date = dt.fromisoformat(start_date)
    end_date = dt.fromisoformat(end_date)
    
    periods = []
    # timeDelta = 
    period_date = end_date - start_date
    # print (f"{period_date.days}, {days}")
    if period_date.days <= days:
        periods.append({"startDate": start_date.date(), "endDate": end_date.date()})
        return periods
    else:
        period_start = start_date
        period_end = start_date + timedelta(days=days)
        while period_end <= end_date:
            periods.append({"startDate": period_start.date(), "endDate": period_end.date()})
            period_start = period_end + timedelta(days=1)
            period_end = period_start + timedelta(days=days)
        periods.append({"startDate": period_start.date(), "endDate": period_end.date()})
        return periods     
    
def snake_to_camel_case(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.capitalize() for x in components[1:])
