import json

class person(object):
    def __init__(self, email=None, address=None):
        self.email = email
        self.address = address
    
    def get_email(self):
        return self.email

    def update_email(self, email):
        self.email = email

    def get_address(self):
        return self.address

    def update_address(self, address):
        self.address = address

    def save(self):
        return {"email": self.email, "address": self.address}