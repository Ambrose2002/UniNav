from datetime import datetime


def get_current_time():
    time_now = datetime.now()
    return time_now


def get_today():
    today = datetime.today().strftime("%A")
    return today


def get_dif(time_now, lecture_time):
    hour = int(lecture_time[:2])
    minute = int(lecture_time[3:5])
    lecture_time = time_now.replace(hour = hour, minute = minute, second = 0)
    return lecture_time - time_now


def convert(string):
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
    time_dif = str(time_dif)
    time = time_dif[-8:]
    h, m, s = map(int, time.split(':'))
    time =  h * 3600 + m * 60 + s
    return time
    
    
    
# print(get_dif(get_current_time(), convert("8:47pm")))
# time_to_seconds(get_dif(get_current_time(), convert("8:47pm")))


