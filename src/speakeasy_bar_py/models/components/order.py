"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .ordertype import OrderType
from enum import Enum
import pydantic
from speakeasy_bar_py.types import BaseModel
from typing import TypedDict
from typing_extensions import Annotated


class Status(str, Enum):
    r"""The status of the order."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETE = "complete"

class OrderTypedDict(TypedDict):
    r"""An order for a drink or ingredient."""
    
    type: OrderType
    r"""The type of order."""
    product_code: str
    r"""The product code of the drink or ingredient."""
    quantity: int
    r"""The number of units of the drink or ingredient to order."""
    status: Status
    r"""The status of the order."""
    

class Order(BaseModel):
    r"""An order for a drink or ingredient."""
    
    type: OrderType
    r"""The type of order."""
    product_code: Annotated[str, pydantic.Field(alias="productCode")]
    r"""The product code of the drink or ingredient."""
    quantity: int
    r"""The number of units of the drink or ingredient to order."""
    status: Status
    r"""The status of the order."""
    
