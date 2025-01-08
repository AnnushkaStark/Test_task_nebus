from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from crud.industry import industry_curd
from crud.specialization import specialization_crud
from schemas.specialization import (
    SpecializationCreate,
    SpecializationPaginatedResponse,
    SpecializationResponse,
)
from services import specialization as specialization_service

router = APIRouter()


@router.get(
    "/specializations/{industry_uid}/",
    response_model=SpecializationPaginatedResponse,
)
async def read_specializations(
    industry_uid: UUID,
    db: AsyncSession = Depends(get_async_db),
    skip: int = 0,
    limit: int = 20,
):
    if found_industry := await industry_curd.get_by_uid(
        db=db, uid=industry_uid
    ):
        return await specialization_crud.get_mullti_with_total_by_industry_id(
            db=db, industry_id=found_industry.id, skip=skip, limit=limit
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
    )


@router.get("/{specialization_uid}/", response_model=SpecializationResponse)
async def read_specialization(
    specialization_uid: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    if found_specialization := await specialization_crud.get_by_uid(
        db=db, uid=specialization_uid
    ):
        return found_specialization
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
    )


@router.post("/{industry_uid}/", status_code=status.HTTP_201_CREATED)
async def create_specialization(
    industry_uid: UUID,
    specialization: SpecializationCreate,
    db: AsyncSession = Depends(get_async_db),
):
    if found_industry := await industry_curd.get_by_uid(
        db=db, uid=industry_uid
    ):
        try:
            return await specialization_service.create(
                db=db, create_schema=specialization
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
    )
