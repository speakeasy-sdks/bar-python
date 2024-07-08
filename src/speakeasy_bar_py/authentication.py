"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from speakeasy_bar_py._hooks import HookContext
from speakeasy_bar_py.models import components, errors, operations
from speakeasy_bar_py.types import BaseModel, Nullable, UNSET
import speakeasy_bar_py.utils as utils
from typing import Optional, Union

class Authentication(BaseSDK):
    r"""The authentication endpoints."""
    
    
    def authenticate(
        self, *,
        request: Union[operations.AuthenticateRequestBody, operations.AuthenticateRequestBodyTypedDict],
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.AuthenticateResponse:
        r"""Authenticate with the API by providing a username and password.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.AuthenticateRequestBody)
        
        req = self.build_request(
            method="POST",
            path="/authenticate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", operations.AuthenticateRequestBody),
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "5XX"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="authenticate", oauth2_scopes=["read:basic"], security_source=None),
            request=req,
            error_status_codes=["401","4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.AuthenticateResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.object = utils.unmarshal_json(http_res.text, Optional[operations.AuthenticateResponseBody])
        elif utils.match_response(http_res, ["401","4XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[components.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
    
    async def authenticate_async(
        self, *,
        request: Union[operations.AuthenticateRequestBody, operations.AuthenticateRequestBodyTypedDict],
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.AuthenticateResponse:
        r"""Authenticate with the API by providing a username and password.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.AuthenticateRequestBody)
        
        req = self.build_request(
            method="POST",
            path="/authenticate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", operations.AuthenticateRequestBody),
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "5XX"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="authenticate", oauth2_scopes=["read:basic"], security_source=None),
            request=req,
            error_status_codes=["401","4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.AuthenticateResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.object = utils.unmarshal_json(http_res.text, Optional[operations.AuthenticateResponseBody])
        elif utils.match_response(http_res, ["401","4XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        elif utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        elif utils.match_response(http_res, "default", "application/json"):
            res.error = utils.unmarshal_json(http_res.text, Optional[components.Error])
        else:
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

        return res
    
