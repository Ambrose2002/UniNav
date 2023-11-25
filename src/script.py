import requests
from bs4 import BeautifulSoup
import json
from db import db, Lectures
from flask import Flask, request
from date_time import get_current_time, get_today, get_dif, convert, time_to_seconds, get_time_str


app = Flask(__name__)

db_filename = "lectures.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps(data), code


def failure_response(message, code=404):
    return json.dumps({"error": message}), code

url = "https://classes.cornell.edu/browse/roster/FA23"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
sGroup = soup.find_all("ul", {"class": "subject-group"})

codes = [subject.find("a").get_text() for subject in sGroup]

# for subject in sGroup:
#     print(subject.find("a").get_text())

url_prefix = "https://classes.cornell.edu"

course_sites = {}
for i in range(len(sGroup)):
    code = codes[i]
    course = sGroup[i]
    course_sites[code] = url_prefix + f"/browse/roster/FA23/subject/{code}"
            


def get_courses_data(course):
    """returns a list of all lectures under course"""
    course_url = course_sites.get(course)
    course_page = requests.get(course_url)
    soup = BeautifulSoup(course_page.text, "html.parser")
    lectures = soup.find_all("div", {"class": "enrlgrp"})
    lectures_lst = []
    for lect in lectures:
        lecture = lect.find_all(class_ = ["section active-tab-details section-last", "section active-tab-details"])
        for lec in lecture:
            class_dict = {}
            course = lect.parent.parent.select(".title-coursedescr")[0].get_text()
            class_dict["course"] = course
            class_code = lec.find("strong", {"class": "tooltip-iws"}).get_text()
            class_dict["code"] = class_code[1:]
            try:
                time = lec.select(".time")[0].get_text()
                class_dict["time_period"] = time
            except:
                class_dict["time_period"] = "N/A"
                
            try:
                location = lec.select(".facility-search")[0].get_text()
                class_dict["location"] = location
            except:
                class_dict["location"] = "N/A"
            days = []
            try:
                dOw = lec.select(".pattern-only")[0].get_text()
                for letter in dOw:
                    if letter == "R":
                        days.append("Thursday")
                    elif letter == "F":
                        days.append("Friday")
                    elif letter == "W":
                        days.append("Wednesday")
                    elif letter == "M":
                        days.append("Monday")
                    else:
                        days.append("Tuesday")
                if len(str(dOw)) == 0:
                    days.append("N/A")
            except:
                days.append("N/A")
            days = " ".join(days)
            class_dict["days"] = days
            lectures_lst.append(class_dict)
            
    return lectures_lst
   
# print(get_courses_data("AS"))

@app.route("/api/create/", methods = ["GET"]) 
def create_table():
    """endpoint for creating lectures table and 
    inserting into lectures table
    """
    for course in course_sites:
        data = get_courses_data(course)
        for body in data:
            lecture = Lectures(
                course = body.get("course"),
                code = body.get("code"),
                time_period = body.get("time_period"),
                location = body.get("location"),
                days = body.get("days")
            )
            db.session.add(lecture)
            db.session.commit()
    return success_response("Successfully created")

@app.route("/api/<string:building>/", methods = ["GET"])
def get_busy_rooms(building):
    """endpoint for getting busy rooms in a lecture building"""
    building = building.capitalize()
    lectures = Lectures.query.filter(Lectures.location.like(f'%{building}%')).all()
    lectures = [lecture.serialize() for lecture in lectures]
    # today = get_today()
    today = "Monday"
    current_time = get_current_time()
    lectures_today = [lecture for lecture in lectures if today in lecture["days"]]
    lectures = []
    for lecture in lectures_today:
        time_period = lecture["time_period"]
        pos1 = time_period.find(" ")
        pos2 = pos1 + 2
        lecture_start_time = time_period[:pos1]
        lecture_start_time = convert(lecture_start_time)
        start_dif = get_dif(current_time, lecture_start_time)
        start_dif = time_to_seconds(start_dif)
        if start_dif >= 83400 or start_dif <= 1800:
            lecture_end_time = time_period[pos2:]
            lecture_end_time = convert(lecture_end_time)
            end_dif = get_dif(current_time, lecture_end_time)
            end_dif = time_to_seconds(end_dif)
            lecture["status"] = get_time_str(start_dif, end_dif)
            lectures.append(lecture)
            
    return lectures
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    
    
    

    
        




