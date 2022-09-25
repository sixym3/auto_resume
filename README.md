# auto_resume

Account class:
- id: integer
- Person: Person object
- Experiences: list object
--------------------------------
- save: returns boolean
- add_experience(exp, experience): return boolean
- remove_experience(id integer): return boolean
- get_experiences(): return list object
- modify_experience(id integer, ):  return boolean


Person class:
- name: string
- email: string
- phone: string
- address: string
--------------------------------
- set_name: returns boolean
- set_email: returns boolean
- set_phone: returns boolean
- set_address: returns boolean
- (function to return json format of person)


Experience object:
- experience id: integer
- Start_date: Datetime object
- End_date: Datetime object
- Job_title: string
- Job_description: list of string
- Type: string ("work", "volunteer", "education", "training", "skill")
- (function to return json format of experience)


CLI object:
- 