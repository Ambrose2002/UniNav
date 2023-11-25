from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lectures(db.Model):
    """Class for creating lecture objects"""
    __tablename__ = "lectures"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Integer, nullable = True)
    code = db.Column(db.Integer, nullable = False)
    time_period = db.Column(db.String, nullable = True)
    location = db.Column(db.String, nullable = True)
    days = db.Column(db.String, nullable = True)
    
    
    def __init__(self, **kwargs):
        """Initializes a lecture object"""
        self.course = kwargs.get("course")
        self.code = kwargs.get("code")
        self.time_period = kwargs.get("time_period")
        self.location = kwargs.get("location")
        self.days = kwargs.get("days")
        
    
    def serialize(self):
        return {
            "course": self.course,
            "code": self.code,
            "time_period":self.time_period,
            "location": self.location,
            "days": self.days
        }
    
    