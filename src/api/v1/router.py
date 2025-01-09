from fastapi import APIRouter

from api.v1.endpoints.industry import router as industry_router
from api.v1.endpoints.organization import router as organization_router
from api.v1.endpoints.specialization import router as specialization_router
from api.v1.endpoints.test_data import router as test_data_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(
    test_data_router, prefix="/test_data", tags=["TestData"]
)
api_router.include_router(
    industry_router, prefix="/industry", tags=["Industry"]
)
api_router.include_router(
    specialization_router, prefix="/specialization", tags=["Specialization"]
)
api_router.include_router(
    organization_router, prefix="/organization", tags=["Organization"]
)
