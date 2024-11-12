"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_bar_py.models.components import (
    drink as components_drink,
    error as components_error,
    httpmetadata as components_httpmetadata,
)
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDrinkRequestTypedDict(TypedDict):
    name: str


class GetDrinkRequest(BaseModel):
    name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetDrinkResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    drink: NotRequired[components_drink.DrinkTypedDict]
    r"""A drink."""
    error: NotRequired[components_error.ErrorTypedDict]
    r"""An unknown error occurred interacting with the API."""


class GetDrinkResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    drink: Optional[components_drink.Drink] = None
    r"""A drink."""

    error: Optional[components_error.Error] = None
    r"""An unknown error occurred interacting with the API."""
