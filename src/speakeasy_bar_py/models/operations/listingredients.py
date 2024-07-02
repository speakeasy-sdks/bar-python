"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_bar_py.models.components import error as components_error, httpmetadata as components_httpmetadata
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListIngredientsRequestTypedDict(TypedDict):
    page: int
    ingredients: NotRequired[List[str]]
    r"""A list of ingredients to filter by. If not provided all ingredients will be returned."""
    

class ListIngredientsRequest(BaseModel):
    page: Annotated[int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    ingredients: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=False))] = None
    r"""A list of ingredients to filter by. If not provided all ingredients will be returned."""
    

class DataTypedDict(TypedDict):
    result_array: List[int]
    

class Data(BaseModel):
    result_array: Annotated[List[int], pydantic.Field(alias="resultArray")]
    

class ListIngredientsResponseBodyTypedDict(TypedDict):
    r"""A list of ingredients."""
    
    data: NotRequired[DataTypedDict]
    

class ListIngredientsResponseBody(BaseModel):
    r"""A list of ingredients."""
    
    data: Optional[Data] = None
    

class ListIngredientsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    object: NotRequired[ListIngredientsResponseBodyTypedDict]
    r"""A list of ingredients."""
    error: NotRequired[components_error.ErrorTypedDict]
    r"""An unknown error occurred interacting with the API."""
    

class ListIngredientsResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    object: Optional[ListIngredientsResponseBody] = None
    r"""A list of ingredients."""
    error: Optional[components_error.Error] = None
    r"""An unknown error occurred interacting with the API."""
    
