from experience import experience
from person import person
from account import account
import json

if __name__ == '__main__':
    # json_v = experience("work", "Software Engineer").to_json()
    # exp = experience.from_json(json.loads(json_v))
    # print(repr(exp), exp.to_json())
    pr = person("Eric", "eric@gmail.com", "passwords", "home")
    acc = account(pr)
    for x in ["software engineer", "developer", "student"]:
        acc.add_experience(experience("Work", x))

    acc.save()