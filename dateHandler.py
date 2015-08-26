import json
import datetime
from time import mktime

dateTODAY = datetime.datetime.now()



def date_by_adding_business_days(from_date, add_days,holidays):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        if current_date in holidays:
            continue
        business_days_to_add -= 1
    return current_date

#demo:
Holidays =[
	datetime.datetime(2015,10,31),
	datetime.datetime(2015,12,24)
]


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)


# print date_by_adding_business_days(datetime.datetime(dateTODAY.year,dateTODAY.month,dateTODAY.day), 10,Holidays)