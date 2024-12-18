"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, SecurityMetadata
from typing_extensions import Annotated, TypedDict


class SchemeClientCredentialsTypedDict(TypedDict):
    client_id: str
    client_secret: str
    token_url: str


class SchemeClientCredentials(BaseModel):
    client_id: Annotated[
        str, FieldMetadata(security=SecurityMetadata(field_name="clientID"))
    ]

    client_secret: Annotated[
        str, FieldMetadata(security=SecurityMetadata(field_name="clientSecret"))
    ]

    token_url: str = "https://speakeasy.bar/oauth2/token/"
