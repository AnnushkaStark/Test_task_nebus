import re
from typing import List

from schemas.phone import PhoneCreate


async def validate(schema: PhoneCreate) -> PhoneCreate:
    schema.number = schema.number.replace(" ", "")
    if re.match(r"^\+\d{11}$", schema.number):
        return schema
    raise Exception("Phone number is not valid")


async def validate_multi(schemas: List[PhoneCreate]) -> List[PhoneCreate]:
    valid_schemas = []
    try:
        for schema in schemas:
            valid_schema = await validate(schema=schema)
            valid_schemas.append(valid_schema)
    except Exception as e:
        raise Exception(str(e))
    return valid_schemas
