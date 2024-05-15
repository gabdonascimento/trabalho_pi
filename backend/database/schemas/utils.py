from typing import Any
from pydantic import BaseModel


class OptionalModel(BaseModel):
    """
    A Pydantic model that sets default values for all fields to None.

    This model is useful when you want to define a Pydantic model with optional fields,
    where the default value for each field is None.

    Example usage:
    ```
    class PartialUser(User, OptionalModel):
        pass
    ```
    """

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        super().__pydantic_init_subclass__(**kwargs)

        for field in cls.model_fields.values():
            field.default = None

        cls.model_rebuild(force=True)
