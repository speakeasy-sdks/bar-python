"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .schemeclientcredentials import SchemeClientCredentials, SchemeClientCredentialsTypedDict
from speakeasy_bar_py.types import BaseModel
from speakeasy_bar_py.utils import FieldMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SecurityTypedDict(TypedDict):
    api_key: NotRequired[str]
    client_credentials: NotRequired[SchemeClientCredentialsTypedDict]
    

class Security(BaseModel):
    api_key: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="apiKey", sub_type="header", field_name="Authorization"))] = None
    client_credentials: Annotated[Optional[SchemeClientCredentials], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="oauth2", sub_type="client_credentials"))] = None
    