import datetime
import json

class experience(object):

    def __init__(self, type, title, description=None, start_date=None, end_date=None):
        self.type = type
        self.title = title
        self.id = id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def from_json(json):
        return experience(json["type"], json["title"], json["description"], json["start_date"], json["end_date"])

    def set_description(self, description):
        self.description = description

    def get_description(self):
        if self.description:
            return self.description
        else:
            return ""
    
    def get_titles(self):
        return self.title

    def save(self):
        return {"type": self.type, "title": self.title, "description": self.description, "start_date": self.start_date, "end_date": self.end_date}
    