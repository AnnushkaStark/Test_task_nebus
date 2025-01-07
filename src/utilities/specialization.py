from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from crud.specialization import specialization_crud
from models import Specialization


async def check_specializations(
    db: AsyncSession, specializarions_ids: List[int], industry_id: int
) -> List[Specialization]:
    found_specializations = []
    for id in specializarions_ids:
        found_specialization = (
            await specialization_crud.get_by_id_and_industry_id(
                db=db, industry_id=industry_id, obj_id=id
            )
        )
        if not found_specialization:
            raise Exception("Specialization not found in this industry!")
        if found_specialization in found_specializations:
            raise Exception(
                f"Specialization {found_specialization.name} alredy added"
            )
        found_specializations.append(found_specialization)
    return found_specializations
