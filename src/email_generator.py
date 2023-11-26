def generate_email(lecture_data, building):
    """Returns the body of the email"""
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

