from pydantic import BaseModel, ValidationError
import json
import logging
from decimal import Decimal
import re
import uuid
from time import perf_counter
from datetime import datetime, timezone
from pathlib import Path
import os
from dotenv import load_dotenv

class Message(BaseModel):
    role: str
    content: str
    token_count: int

def main():
    start_time = perf_counter()

    data_path = Path(__file__).parent / "data.json"
    with data_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

# pydantic validation
    messages = []

    for item in data:
        try:
          message = Message(**item)
          messages.append(message)
          print(f"Valid record: {message}")

        except ValidationError as e:
          logging.warning(f"Invalid record skipped: {e}")

# Regular expression


    message=[]

    for item in data:
      try:
        item=re.findall(r"\d{10}",item["content"])
        message.append(item)
        print(f"Valid record: {item}")
      except KeyError as e:
        logging.warning(f"KeyError: {e} in item: {item}")


# token cost calculation
    total_token_count = 0
    token_cost = Decimal("0.00025")

    for item in data:
      try:
        message = Message(**item)
        total_token_count += message.token_count
        print(f"Valid record: {message.token_count}")
      except ValidationError as e:
        logging.warning(f"Invalid record skipped: {e}")

    print(f"Total tokens: {total_token_count}")
    total_cost = Decimal(total_token_count) * token_cost
    print(f"Total token cost: ${total_cost:.4f}")

# uuid generation

    messages = []
    for item in data:
      try:
        message=Message(**item)
        unique_id=uuid.uuid4()
        date_time=datetime.now(timezone.utc)
        messages.append((message, unique_id))
      except ValidationError as e:
        logging.warning(f"Invalid record skipped: {e}")
    print("Messages with UUIDs:")
    for message, unique_id in messages:
      print(f"Role: {message.role}, Content: {message.content}, Token Count: {message.token_count}, UUID: {unique_id}, DateTime: {date_time}")

    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time:.4f} seconds")

# 
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if api_key:
      print("API key loaded successfully.")
    else:
      print("API key not found.")

if __name__ == "__main__":
    main()
