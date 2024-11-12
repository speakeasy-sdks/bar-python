"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_bar_py.models.components import (
    error as components_error,
    httpmetadata as components_httpmetadata,
    order as components_order,
    order_input as components_order_input,
)
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateOrderRequestTypedDict(TypedDict):
    request_body: List[components_order_input.OrderInputTypedDict]
    callback_url: NotRequired[str]
    r"""The url to call when the order is updated."""


class CreateOrderRequest(BaseModel):
    request_body: Annotated[
        List[components_order_input.OrderInput],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    callback_url: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The url to call when the order is updated."""


class CreateOrderResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    order: NotRequired[components_order.OrderTypedDict]
    r"""The order was created successfully."""
    error: NotRequired[components_error.ErrorTypedDict]
    r"""An unknown error occurred interacting with the API."""


class CreateOrderResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    order: Optional[components_order.Order] = None
    r"""The order was created successfully."""

    error: Optional[components_error.Error] = None
    r"""An unknown error occurred interacting with the API."""
