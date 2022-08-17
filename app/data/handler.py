import json
from typing import List, Dict
from app.data.model import UserSchema, UserLoginSchema

"""
{
  "users": [
    {
      "user": "test",
      "email": "test",
      "password": "test"
    },
    {
      "user": "test2",
      "email": "test2",
      "password": "test2"
    }
  ]
}
"""

def get_all_users() -> List:
    with open('app/data/db.json') as out_file:
        data = json.load(out_file)
        return data['users']

def get_user(email: str = None) -> UserSchema:
    if email:
        with open('app/data/db.json') as out_file:
            data = json.load(out_file)
            for user in data['users']:
                if user['email'] == email:
                    return user

def write_user(user: UserSchema):
    with open('app/data/db.json', 'r') as file:
        data = json.load(file)
        file.close()
    if data.get('users'):
        data['users'].append(user.dict())
    with open('app/data/db.json', 'w') as f2:
        f2.write(json.dumps(data, indent=4))

def check_user(data: UserLoginSchema):
    for user in get_all_users():
        obj = UserSchema(**user)
        if obj.email == data.email and obj.password == data.password:
            return True
    return False


# user = UserSchema(fullname='modfsfdo', email='moo.hughes@email.com', password='bah')
# write_user(user)