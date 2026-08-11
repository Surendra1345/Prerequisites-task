import re

def strip_code_fence(text):
    pattern = r"```\s*(?:json)?\s*(.*?)\s*```"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1)

    return text
# with the fence
# text= """```json
# {
#     "role": "user",
#     "content": "Hello, how are you?"
#     }
#     ```"""

# without the fence
text= """json
{
    "role": "user",
    "content": "Hello, how are you?"
    }
    """


result=strip_code_fence(text)
print(result)

# finding the phone numbers in the text 
text = " i have two phone numbers 6303023283 and 9812713822"
result=re.findall(r"\d{10}",text)
print(result)

# replacing the phone number with [PHONE]

result=re.sub(r"\d{10}","[PHONE]",text)
print(result)


# finding the ABC-1234 pattern in the text


text="The car's license plate is ABC-1234, and the truck's license plate is XY-5678."
result=re.findall(r"[A-Z]{3}-\d{4}",text)
print(result)


# testing all three together

text = """```json
{
    "role": "user"
}
```"""

print(strip_code_fence(text))

text = """{
    "role": "user"
}"""

print(strip_code_fence(text))

text = """Here is the JSON:

```json
{
    "role": "user"
}
```"""

print(strip_code_fence(text))

text = """
Call me at 9876543210.
My second number is 8123456789.
This is invalid: 12345.
This is also invalid: 12345678901.
"""
numbers = re.findall(r"\b\d{10}\b", text)
print(numbers)

valid_ids = [
    "ABC-1234",
]

invalid_ids = [
    "abc-1234",
    "ABC-123",
    "ABC1234",
    "ABC-12345",
]

for test_id in valid_ids + invalid_ids:
    if re.match(r"^[A-Z]{3}-\d{4}$", test_id):
        print(f"{test_id} is valid")
    else:
        print(f"{test_id} is invalid")


text = "నా ఫోన్ నంబర్ 9876543210."
result = re.sub(r"\d{10}", "[PHONE]", text)
print(result)