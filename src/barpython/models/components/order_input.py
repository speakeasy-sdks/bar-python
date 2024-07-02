"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .ordertype import OrderType
from barpython import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrderInput:
    r"""An order for a drink or ingredient."""
    type: OrderType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of order."""
    product_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode') }})
    r"""The product code of the drink or ingredient."""
    quantity: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""The number of units of the drink or ingredient to order."""
    

