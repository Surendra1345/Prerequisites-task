from Enums import Model
messages = [
    {"role": Model.User, "content": "Hello", "token_count": 10},
    {"role": Model.Assistant, "content": "Hi, how can I help?", "token_count": 15},
    {"role": Model.User, "content": "What is Python?", "token_count": 20},
    {"role": Model.Assistant, "content": "Python is a programming language.", "token_count": 18},
    {"role": Model.User, "content": "What is a list?", "token_count": 12},
    {"role": Model.Assistant, "content": "A list stores multiple values.", "token_count": 22},
    {"role": Model.User, "content": "What is a dictionary?", "token_count": 16},
    {"role": Model.Assistant, "content": "A dictionary stores key-value pairs.", "token_count": 25},
    {"role": Model.User, "content": "What is a function?", "token_count": 14},
    {"role": Model.Assistant, "content": "A function is reusable code.", "token_count": 30},
]
# print(messages)
# token_cost=0.00025
# total_cost = 0.0
# for i, message in enumerate(messages,start=1):
#     total_cost += message["token_count"] * token_cost


    # print(
    #     f"{i}. {message['content']} | "
    #     f"tokens={message['token_count']} | "
    #     f"cost=${token_cost:.6f}"
    # )
# print(f"Total token cost: ${total_cost}")

filter_loop=[]
for message in messages:
    if message["token_count"]>20:
        filter_loop.append(message)
# print(filter_loop)
filterd_comparison =[
    message 
    for message in messages
    if message["token_count"]>20
]
# print(filterd_comparison)

sorted_messages=sorted(
    messages,
    key=lambda message:message["token_count"],
    reverse=True
)
# print(sorted_messages)

from pathlib import Path

token_file=Path("task_count.txt")
lines=[token_file.read_text(encoding="utf-8").splitlines()]
print(lines)
token_count=[]
for value in token_file.read_text(encoding="utf-8").splitlines():
    try:
        token_count.append(int(value))
    except ValueError:
        print(f"Invalid value: {value}")


cost_per_token=0.00025
float=sum(
    massage["token_count"]*cost_per_token
    for massage in messages
)
print(f"Float Total token cost: ${float}")

from decimal import Decimal
decimal_cost=Decimal("0.00025")
decimal_total_cost=sum(
    Decimal(message["token_count"])*decimal_cost
    for message in messages
)   
print(f"Total token cost: ${decimal_total_cost}")

text = "నమస్కారం"
char_length = len(text)
utf8_bytes = text.encode("utf-8")
byte_length = len(utf8_bytes)

print(f"Character length: {char_length}")
print(f"Byte length: {byte_length}")
print(f"UTF-8 bytes: {utf8_bytes}")

first_list=[1,2,3,4]
second_list=first_list
first_list.append(5)
print(f"First list: {first_list}")
print(f"Second list: {second_list}")
print(first_list is second_list)  

from cost import total_token_cost
""" Calculate the total token cost for a list of messages"""

# print(f"Total token cost using function: ${total_token_cost(messages):4f}")

# P4 Task

class token_counter:
    def __init__(self, token_cost=0.0025):
      """Count the total token cost for a list of messages"""
      self.total_cost=0.0
      self.token_cost=token_cost
    def add(self,token_count):
        self.total_cost+=token_count
    def get_total_cost(self):
        return self.total_cost*self.token_cost

    
counter=token_counter()
counter.add(100)
counter.add(200)
counter.add(300)
print(f"Total cost:${counter.total_cost}")
print(f"Total token cost: ${counter.get_total_cost()}")

# Dataclasses

from dataclasses import dataclass

@dataclass
class Document:
    """A simple document class"""
    text:str
    page:int
    source:str

count=Document(
    text="This is a sample document.",
    page=5,
    source="Generated"
)

print(f"Document text: {count.text}")
print(f"Document page: {count.page}")
print(f"Document source: {count.source}")


class DocumentProcessor:
    def processor(self):
        raise NotImplementedError

class PDFProcessor(DocumentProcessor):
    def processor(self):
        # return "Processing PDF document"
         pass

class WordProcessor(DocumentProcessor):
    def processor(self):
        #  return "Processing Word document"
         pass

pdf=PDFProcessor()
word=WordProcessor()
print(f"PDF Processor: {pdf.processor()}")
print(f"Word Processor: {word.processor()}")


# Decarator

from functools import lru_cache
@lru_cache(maxsize=128)
def square(n):
    """Calculate the square of a number"""
    print(f"Calculating square of {n}")
    return n*n
print(square(4))
print(square(10))
