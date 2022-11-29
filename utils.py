from datetime import datetime
from pytz import timezone


# hello_world to helloWorld
def to_camel_case(snake_string):
    title = snake_string.title()
    title = title[0].lower() + title[1:]
    return title.replace("_", "")


# convert zulu time to local time and change datetime format
def format_datetime(time_attr):
    utc = timezone('UTC')
    local_time = timezone("Europe/London")
    if 'Z' in time_attr:
        datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        try:
            datetime.strptime(time_attr, datetime_format)
        except ValueError:
            datetime_format = "%Y-%m-%dT%H:%M:%SZ"
    else:
        datetime_format = "%Y-%m-%d %H:%M:%S.%f"
    utc_dt = utc.localize(datetime.strptime(time_attr, datetime_format))
    local_dt = utc_dt.astimezone(local_time).strftime("%Y-%m-%d %H:%M:%S.%f")
    return local_dt

