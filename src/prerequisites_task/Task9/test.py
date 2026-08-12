import pytest
from pydantic import BaseModel, ValidationError
import re
from decimal import Decimal
import json


class Message(BaseModel):
    role: str
    content: str
    token_count: int


def test_valid_message():
    message = Message(
        role="user",
        content="Hello",
        token_count=20,
    )

    assert message.role == "user"
    assert message.content == "Hello"
    assert message.token_count == 20

def test_invalid_message():
    with pytest.raises(ValidationError):
        message=Message(
            role="user",
            content="Hello",
            token_count="wrong",
        )

        import pytest
from pydantic import BaseModel, ValidationError


class Message(BaseModel):
    role: str
    content: str
    token_count: int


def test_valid_message():
    message = Message(
        role="user",
        content="Hello",
        token_count=20,
    )

    assert message.role == "user"
    assert message.content == "Hello"
    assert message.token_count == 20

def test_invalid_message():
    with pytest.raises(ValidationError):
        message = Message(
            role="user",
            content="Hello",
            token_count="wrong",
        )


# regex test

def test():
    text="this is my phone number 6303023283"
    result=re.sub(r"\d{10}","[PHONE]",text)
    assert result=="this is my phone number [PHONE]"



def test_cost_calculation():
    token_count = 20
    token_cost = Decimal("0.00025")
    total_cost = Decimal(token_count) * token_cost
    assert total_cost == Decimal("0.00500")



def test_json_loading(tmp_path):
    data = [
        {
            "role": "user",
            "content": "Hello",
            "token_count": 20,
        }
    ]

    file_path = tmp_path / "test_data.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file)

    with file_path.open("r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    assert loaded_data == data

def test_multiple_phone_numbers():
    text = "Call 6303023283 or 9876543210"

    result = re.sub(r"\d{10}", "[PHONE]", text)

    assert result == "Call [PHONE] or [PHONE]"