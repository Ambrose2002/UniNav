from datetime import datetime


def get_current_time():
    """returns the current time as a datetime object"""
    time_now = datetime.now()
    return time_now


def get_today():
    """returns the current day of the week"""
    today = datetime.today().strftime("%A")
    return today


def get_dif(time_now, lecture_time):
    """returns the time difference in seconds between current time and lecture time"""
    hour = int(lecture_time[:2])
    minute = int(lecture_time[3:5])
    lecture_time = time_now.replace(hour = hour, minute = minute, second = 0)
    return lecture_time - time_now


def convert(string):
    """returns a string of time in 24 hour format"""
    pos = string.find(":")
    if len(string[:pos]) == 1:
        string = "0" + string
    if string[-2:] == "am" and string[:2] == "12":
        return "00" + string[2:-2]

    elif string[-2:] == "am":
        return string[:-2]

    elif string[-2:] == "pm" and string[:2] == "12":
        return string[:-2]
    
    else:
        return str(int(string[:2]) + 12) + string[2:8]


def time_to_seconds(time_dif):
    """converts time to seconds"""
    time_dif = str(time_dif)
    time = time_dif[-8:]
    h, m, s = map(int, time.split(':'))
    time =  h * 3600 + m * 60 + s
    return time
    
def get_time_str(start_diff, end_dif):
    """returns a string of time left before/until class"""
    hour = start_diff//3600
    if hour > 18:
        hour = 24 - hour
    s_left = start_diff%3600
    minute = s_left//60
    if start_diff <= 1800:
        if hour == 0:
            return f"Starts in {minute} minutes"
        elif minute == 0:
            return f"Starts in exactly {minute} minutes"
        return f"Starts in {hour} hours, {minute} minutes"
    else:
        hour = end_dif//3600
        if hour > 18:
            hour = 24 - hour
        s_left = end_dif%3600
        minute = s_left//60
        if hour == 0:
            return f"Ends in {minute} minutes"
        elif minute == 0:
            return f"Ends in exactly {hour} hours"
        return f"Ends in {hour} hours, {minute} minutes"



