from enum import Enum

class Model(Enum):
    User="user"
    Assistant="assistant"

role=Model.User
print(role.value)
role=Model.Assistant
print(role.value)
