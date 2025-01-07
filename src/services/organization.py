from sqlalchemy.ext.asyncio import AsyncSession

from crud.organization import organization_crud
from models import Organization
from schemas.organization import OrganizationCreate, OrganizationCreateDB
from services import address as address_service
from services import phone as phone_service
from utilities.indistry import check_industry
from utilities.specialization import check_specializations


async def create(
    db: AsyncSession, create_schema: OrganizationCreate
) -> Organization:
    try:
        address_schema = create_schema.address
        phone_schemas = create_schema.phone_numbers
        del create_schema.address
        del create_schema.phone_numbers
        create_schema.industry_id = await check_industry(
            db=db, industry_id=create_schema.industry_id
        )
        specializations = await check_specializations(
            db=db,
            specializarions_ids=create_schema.specializations_ids,
            industry_id=create_schema.industry_id,
        )
        del create_schema.specializations_ids
        create_data = OrganizationCreateDB(
            **create_schema.model_dump(exclude_unset=True)
        )
        organozation = await organization_crud.create(
            db=db, create_schema=create_data, commit=False
        )
        await address_service.create(
            db=db, create_data=address_schema, organization_id=organozation.id
        )
        await phone_service.create_multi(
            db=db, schemas=phone_schemas, organization_id=organozation.id
        )
        organozation.specializations = specializations
        await db.commit()
        return organozation
    except Exception as e:
        await db.rollback()
        raise e
