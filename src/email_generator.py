# data = [
#     {"code": 2424, "course": "Design Your Dyson", "days": "Monday Wednesday", "location": "Malott Hall 228-Bache Aud", "status": "Ends in 46 minutes", "time_period": "1:25pm - 2:40pm"},
#     {"code": 2358, "course": "Laboratory in Genetics and Genomics", "days": "Monday", "location": "Malott Hall 253", "status": "Ends in 21 minutes", "time_period": "1:25pm - 2:15pm"},
#     {"code": 2372, "course": "Intergroup Dialogue", "days": "Monday", "location": "Malott Hall 203", "status": "Ends in 2 hours, 31 minutes", "time_period": "1:25pm - 4:25pm"},
#     {"code": 2392, "course": "Intergroup Dialogue", "days": "Monday", "location": "Malott Hall 224", "status": "Ends in 2 hours, 31 minutes", "time_period": "1:25pm - 4:25pm"},
#     {"code": 8530, "course": "Fashion Product Management", "days": "Monday Wednesday", "location": "Malott Hall 406", "status": "Ends in 46 minutes", "time_period": "1:25pm - 2:40pm"},
#     {"code": 1445, "course": "Intergroup Dialogue", "days": "Monday", "location": "Malott Hall 203", "status": "Ends in 2 hours, 31 minutes", "time_period": "1:25pm - 4:25pm"},
#     {"code": 1448, "course": "Intergroup Dialogue", "days": "Monday", "location": "Malott Hall 224", "status": "Ends in 2 hours, 31 minutes", "time_period": "1:25pm - 4:25pm"},
#     {"code": 8774, "course": "Calculus I", "days": "Monday", "location": "Malott Hall 251", "status": "Ends in 21 minutes", "time_period": "1:25pm - 2:15pm"},
#     {"code": 9928, "course": "Abstract Algebra", "days": "Monday Wednesday", "location": "Malott Hall 207", "status": "Ends in 46 minutes", "time_period": "1:25pm - 2:40pm"},
#     {"code": 3499, "course": "Algebra", "days": "Monday Wednesday", "location": "Malott Hall 205", "status": "Ends in 46 minutes", "time_period": "1:25pm - 2:40pm"}
# ]

def generate_email(lecture_data, building):
    email_content = f"""
    
Dear Ambrose,

Here is the current schedule of lectures taking place today in {building}:

"""
    for lecture in lecture_data:
        email_content += f"""
{lecture["course"]} (Code: {lecture["code"]})
   - Status: {lecture["status"]}
   - Location: {lecture["location"]}
   - Time Period: {lecture["time_period"]}

"""
    email_content += """
This is an automatically generated email. Please do not reply.
Designed with love by Ambrose Blay
"""
    return email_content

# print(generate_email(data, "Klarman"))