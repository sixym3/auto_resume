import os
import itertools
import math
from person import person
from experience import experience
import json

class account(object):
    metadata = "account_metadata.json"
    iter_id = itertools.count() # TODO: Remember list of id

    def __init__(self, person, username, password):
        self.id = next(account.iter_id)
        self.person = person
        self.experiences = []
        self.username = username
        self.password = password # TODO: Hash the password
        self.filename = "users/" + str(self.id) + ".json"

    @staticmethod
    def load_metadata():
        if os.path.exists(account.metadata):
            with open(account.metadata, "r") as m:
                data = json.load(m)
                account.iter_id = itertools.count(data["iter_id"])
        account.save_metadata()

    @staticmethod
    def save_metadata():
        with open(account.metadata, "w") as m:
            id = next(account.iter_id)-1
            if id < 0:
                id = 0
            m.write(json.dumps({"iter_id": id }))

    def get_experiences(self, num_per_row):
        result = []
        for i in range(math.ceil(len(self.experiences)/num_per_row)):
            result.append([])
            for j in range(num_per_row):
                if (i * num_per_row + j) < len(self.experiences):
                    index = i * num_per_row + j
                else:
                    index = len(self.experiences) - 1
                result[i][j] = self.experiences[index]
        return result

    def get_email(self):
        return self.person.get_email()

    def update_email(self, email):
        # TODO: Add a check for whether the email is valid 
        self.person.update_email(email)

    def get_address(self):
        return self.person.get_address()

    def update_address(self, address):
        self.person.update_address(address)

    def add_experience(self, ex):
        if isinstance(ex, experience):
            self.experiences.append(ex)
            return True
        return False

    @staticmethod
    def authenticate(username, password):
        return True # TODO: Check if user is created already

    def to_json(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.save()))

    def save(self):
        # try:
        #     if len(self.experiences) > 0:
        #         x = [exp.save() for exp in self.experiences]
        #     else:
        #         x = []
        # except Exception:
        #     print(Exception)
        x = [exp.save() for exp in self.experiences]
        return {"id": self.id, "person": self.person.save(), "experiences": x, "username": self.username, "password": self.password}
    
