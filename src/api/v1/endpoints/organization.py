from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from api.filters.organization import OrganizationFilter
from crud.organization import organization_crud
from crud.search import search_organization_crud
from schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationsPaginatedResponse,
)
from services import organization as organization_service

router = APIRouter()


@router.get("/", response_model=OrganizationsPaginatedResponse)
async def serach_organizations(
    skip: int = 0,
    limit: int = 20,
    query: str = Query(min_length=2),
    db: AsyncSession = Depends(get_async_db),
):
    return await search_organization_crud.get_organizations_result(
        db=db, query=query, skip=skip, limit=limit
    )


@router.get("/all/", response_model=OrganizationsPaginatedResponse)
async def read_organizations(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_async_db),
    filter: OrganizationFilter = FilterDepends(OrganizationFilter),
):
    return await filter.filter(db=db, skip=skip, limit=limit)


@router.get("/{organization_uid}/", response_model=OrganizationResponse)
async def read_organization(
    organization_uid: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    return await organization_crud.get_by_uid(db=db, uid=organization_uid)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_organization(
    organization: OrganizationCreate,
    db: AsyncSession = Depends(get_async_db),
):
    try:
        await organization_service.create(db=db, create_schema=organization)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
