import json
import logging
from pathlib import Path

path=Path("data.json")

try:
    with path.open("r",encoding="utf-8") as file:
     message=json.load(file)
    print(message)
except json.JSONDecodeError:
    logging.warning(f"Failed to decode JSON from {path}")


class TokencountError(Exception):
   pass
def token_count(token):
    if token<0:
        raise TokencountError("Token count cannot be negative")

token_count(10)

from datetime import datetime,timezone

timenow=datetime.now(timezone.utc)
print(timenow)

from time import perf_counter

start_time=perf_counter()
path=Path("data.json")
data=path.read_text(encoding="utf-8")
end_time=perf_counter()

print(f"Time taken to read the file: {end_time-start_time:.6f} seconds")

# ////
from collections import Counter,defaultdict
import uuid

roles=["employee","manager","admin","employee","admin","admin"]
counter=Counter(roles)
print(counter)


default_dict=defaultdict(int)
for role in roles:
    default_dict[role]+=1
print(default_dict)

messages=[
    {"role": "employee", "text": "claim submitted"},
    {"role": "manager", "text": "claim approved"},
    {"role": "admin", "text": "claim processed"},
    {"role": "employee", "text": "claim submitted"},
    {"role": "manager", "text": "claim rejected"},
]
for message in messages:
    unique_id=uuid.uuid4()
    print(f"Role: {message['role']}, Text: {message['text']}, Unique ID: {unique_id}")
