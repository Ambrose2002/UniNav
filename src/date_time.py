from datetime import datetime


def get_time():
    time_now = datetime.now()
    time_now = time_now.strftime('%I:%M:%S %p')
    suffix = (time_now[-2:]).lower()
    time_now = time_now[:-6]
    if time_now[0] == "0":
        time_now = time_now[1:]
    time_now += suffix
    return time_now

def get_today():
    today = datetime.today().strftime("%A")
    return today
