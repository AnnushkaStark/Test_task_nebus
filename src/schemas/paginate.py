from pydantic import BaseModel


class PaginatedResponseBase(BaseModel):
    limit: int
    offset: int
    total: int
