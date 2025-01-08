import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.router import api_router as organizations_service_router

app = FastAPI(
    title="OrganizationService",
    openapi_url="/organization_service/openapi.json",
    docs_url="/organization_service/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(organizations_service_router, prefix="/organization_service")
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
    )