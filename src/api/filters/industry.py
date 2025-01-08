from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from models import Industry


class IndustryFilter(Filter):
    name: Optional[str] = None

    class Constants(Filter.Constants):
        model = Industry
