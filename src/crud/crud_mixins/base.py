from typing import Generic, Type

from constants.crud_types import ModelType


class BaseCRUD(Generic[ModelType]):
    """
    Base CRUD object
    **Parameters**
    * `model`: A SQLAlchemy model class
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model
