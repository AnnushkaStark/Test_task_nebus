from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from utilities.test_data.industry import create_test_industryies
from utilities.test_data.organization import create_test_organizations
from utilities.test_data.specialization import create_test_specializations

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def create_test_data_industry(db: AsyncSession = Depends(get_async_db)):
    try:
        await create_test_industryies(db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/specializations/", status_code=status.HTTP_200_OK)
async def create_test_data_specializations(
    db: AsyncSession = Depends(get_async_db),
):
    try:
        await create_test_specializations(db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/test_data/organizations/", status_code=status.HTTP_200_OK)
async def create_test_data_organizations(
    db: AsyncSession = Depends(get_async_db),
):
    try:
        await create_test_organizations(db=db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
