from sqlalchemy.ext.asyncio import AsyncSession

from schemas.specialization import SpecializationCreate
from services import specialization as specialization_service


async def create_test_specializations(db: AsyncSession) -> None:
    specializations = [
        SpecializationCreate(name="Конструирование одежд", industry_id=2),
        SpecializationCreate(name="Изготовление лекал", industry_id=2),
        SpecializationCreate(name="Пошив одежды", industry_id=2),
        SpecializationCreate(
            name="Управление кухней и разработка блюд", industry_id=1
        ),
        SpecializationCreate(name="Обучение кулинарии", industry_id=1),
        SpecializationCreate(
            name="Приготовление различных видов хлебобулочных изделий",
            industry_id=1,
        ),
        SpecializationCreate(name="Графический дизайн", industry_id=3),
        SpecializationCreate(name="Промышленный дизайн", industry_id=3),
        SpecializationCreate(name="Продуктовый дизайн", industry_id=3),
    ]
    try:
        for specialization in specializations:
            await specialization_service.create(
                db=db, create_schema=specialization
            )
    except Exception as e:
        raise Exception(str(e))
