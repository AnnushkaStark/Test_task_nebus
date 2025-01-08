from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from crud.phone import phone_crud
from schemas.phone import PhoneCreate, PhoneCreateDB
from utilities.validators.phone import validate_multi


async def create_multi(
    db: AsyncSession, schemas: List[PhoneCreate], organization_id: int
) -> None:
    try:
        valid_schemas = await validate_multi(schemas=schemas, db=db)
    except Exception as e:
        raise Exception(str(e))
    if len(valid_schemas) != len(schemas):
        raise Exception("Not all phone numbers is valid")
    list_create_data = [
        PhoneCreateDB(
            **schema.model_dump(exclude_unset=True),
            organization_id=organization_id
        )
        for schema in valid_schemas
    ]
    return await phone_crud.create_bulk(db=db, create_schemas=list_create_data)
