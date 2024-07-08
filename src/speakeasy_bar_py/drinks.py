"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from speakeasy_bar_py._hooks import HookContext
from speakeasy_bar_py.models import components, errors, operations
from speakeasy_bar_py.types import Nullable, UNSET
import speakeasy_bar_py.utils as utils
from typing import List, Optional

class Drinks(BaseSDK):
    r"""The drinks endpoints."""
    
    
    def list_drinks(
        self, *,
        drink_type: Optional[components.DrinkType] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.ListDrinksResponse:
        r"""Get a list of drinks.

        Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param drink_type: The type of drink to filter by. If not provided all drinks will be returned.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = operations.ListDrinksRequest(
            drink_type=drink_type,
        )
        
        req = self.build_request(
            method="GET",
            path="/drinks",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="listDrinks", oauth2_scopes=["read:basic","read:drinks"], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.ListDrinksResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.drinks = utils.unmarshal_json(http_res.text, Optional[List[components.Drink]])
        elif utils.match_response(http_res, "4XX", "*"):
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
    
    
    async def list_drinks_async(
        self, *,
        drink_type: Optional[components.DrinkType] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.ListDrinksResponse:
        r"""Get a list of drinks.

        Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param drink_type: The type of drink to filter by. If not provided all drinks will be returned.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = operations.ListDrinksRequest(
            drink_type=drink_type,
        )
        
        req = self.build_request(
            method="GET",
            path="/drinks",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="listDrinks", oauth2_scopes=["read:basic","read:drinks"], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.ListDrinksResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.drinks = utils.unmarshal_json(http_res.text, Optional[List[components.Drink]])
        elif utils.match_response(http_res, "4XX", "*"):
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
    
    
    def get_drink(
        self, *,
        name: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.GetDrinkResponse:
        r"""Get a drink.

        Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param name: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = operations.GetDrinkRequest(
            name=name,
        )
        
        req = self.build_request(
            method="GET",
            path="/drink/{name}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="getDrink", oauth2_scopes=["read:basic"], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.GetDrinkResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.drink = utils.unmarshal_json(http_res.text, Optional[components.Drink])
        elif utils.match_response(http_res, "4XX", "*"):
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
    
    
    async def get_drink_async(
        self, *,
        name: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
    ) -> operations.GetDrinkResponse:
        r"""Get a drink.

        Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param name: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = operations.GetDrinkRequest(
            name=name,
        )
        
        req = self.build_request(
            method="GET",
            path="/drink/{name}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="getDrink", oauth2_scopes=["read:basic"], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        res = operations.GetDrinkResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if utils.match_response(http_res, "200", "application/json"):
            res.drink = utils.unmarshal_json(http_res.text, Optional[components.Drink])
        elif utils.match_response(http_res, "4XX", "*"):
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
    
