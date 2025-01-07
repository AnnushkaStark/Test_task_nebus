import re


async def validate(number: str) -> str:
    number = number.replace(" ", "")
    if re.match(r"^\+\d{11}$", number):
        return number
    raise Exception("Phone number is not valid")
