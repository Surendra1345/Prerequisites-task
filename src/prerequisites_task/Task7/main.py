from fastapi import FastAPI
from pydantic import BaseModel,ValidationError

class Message(BaseModel):
    role:str
    text:str
    token_count:int


messages=Message(
    role="user",
    text="Hello, how are you?",
    token_count=5,
)
print(messages)

class Medication(BaseModel):
    name: str
    dose: str | None = None

medication=Medication(
    name="Aspirin",
    dose="None"
)
print(medication)


import json

with open("data.json", "r") as file:
    data=json.load(file)

class Message(BaseModel):
    role:str
    text:str
    token_count:int

try:
    message=[Message(**item) for item in data]
    for msg in message:
        print(msg)
except ValidationError as e:
    print("Validation error:", e)


import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)