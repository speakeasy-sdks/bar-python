"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .drinktype import DrinkType
import pydantic
from speakeasy_bar_py.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DrinkTypedDict(TypedDict):
    name: str
    r"""The name of the drink."""
    price: float
    r"""The price of one unit of the drink in US cents."""
    type: NotRequired[DrinkType]
    r"""The type of drink."""
    stock: NotRequired[int]
    r"""The number of units of the drink in stock, only available when authenticated."""
    product_code: NotRequired[str]
    r"""The product code of the drink, only available when authenticated."""


class Drink(BaseModel):
    name: str
    r"""The name of the drink."""

    price: float
    r"""The price of one unit of the drink in US cents."""

    type: Optional[DrinkType] = None
    r"""The type of drink."""

    stock: Optional[int] = None
    r"""The number of units of the drink in stock, only available when authenticated."""

    product_code: Annotated[Optional[str], pydantic.Field(alias="productCode")] = None
    r"""The product code of the drink, only available when authenticated."""
