"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, SecurityMetadata
from typing import Final, TypedDict
from typing_extensions import Annotated


class SchemeClientCredentialsTypedDict(TypedDict):
    client_id: str
    client_secret: str
    

class SchemeClientCredentials(BaseModel):
    client_id: Annotated[str, FieldMetadata(security=SecurityMetadata(field_name="clientID"))]
    client_secret: Annotated[str, FieldMetadata(security=SecurityMetadata(field_name="clientSecret"))]
    TOKEN_URL: Annotated[Final[str], pydantic.Field(alias="TokenURL")] = "https://speakeasy.bar/oauth2/token/" # type: ignore
    
