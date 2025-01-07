from sqlalchemy.ext.asyncio import AsyncSession

from crud.address import address_crud
from models import Address
from schemas.address import AddressCreate, AddressCreateDB
from utilities.validators.adress import validate


async def create(
    db: AsyncSession, create_data: AddressCreate, organization_id: int
) -> Address:
    try:
        valid_schema = await validate(schema=create_data)
    except Exception as e:
        raise Exception(str(e))
    create_schema = AddressCreateDB(
        **valid_schema.model_dump(exclude_unset=True),
        organization_id=organization_id
    )
    return await address_crud.create(db=db, create_schema=create_schema)
