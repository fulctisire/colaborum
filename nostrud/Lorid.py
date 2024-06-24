import datetime

def unix_date(unix):
    date_time = datetime.datetime.utcfromtimestamp(unix)
    formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date_time
