from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from crud.industry import industry_curd
from schemas.industry import (
    IndustryCreate,
    IndustryFullResponse,
    IndustryPaginatedResponse,
)
from services import industry as industry_service

router = APIRouter()


@router.get("/", response_model=IndustryPaginatedResponse)
async def read_industries(
    db: AsyncSession = Depends(get_async_db), skip: int = 0, limit: int = 20
):
    return await industry_curd.get_multi_with_total(
        db=db, skip=skip, limit=limit
    )


@router.get("/{industry_uid}/", response_model=IndustryFullResponse)
async def read_industry(
    industry_uid: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    if found_industry := await industry_curd.get_by_uid(
        db=db, uid=industry_uid
    ):
        return found_industry
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_idustry(
    industry: IndustryCreate,
    db: AsyncSession = Depends(get_async_db),
):
    try:
        return await industry_service.create(db=db, create_data=industry)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
