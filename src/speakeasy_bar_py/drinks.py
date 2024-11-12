"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from speakeasy_bar_py import utils
from speakeasy_bar_py._hooks import HookContext
from speakeasy_bar_py.models import components, errors, operations
from speakeasy_bar_py.types import OptionalNullable, UNSET
from typing import Any, List, Optional


class Drinks(BaseSDK):
    r"""The drinks endpoints."""

    def list_drinks(
        self,
        *,
        drink_type: Optional[components.DrinkType] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.ListDrinksResponse:
        r"""Get a list of drinks.

        Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param drink_type: The type of drink to filter by. If not provided all drinks will be returned.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

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
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="listDrinks",
                oauth2_scopes=["read:basic", "read:drinks"],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListDrinksResponse(
                drinks=utils.unmarshal_json(
                    http_res.text, Optional[List[components.Drink]]
                ),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.ListDrinksResponse(
                error=utils.unmarshal_json(http_res.text, Optional[components.Error]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_drinks_async(
        self,
        *,
        drink_type: Optional[components.DrinkType] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.ListDrinksResponse:
        r"""Get a list of drinks.

        Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param drink_type: The type of drink to filter by. If not provided all drinks will be returned.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.ListDrinksRequest(
            drink_type=drink_type,
        )

        req = self.build_request_async(
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
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="listDrinks",
                oauth2_scopes=["read:basic", "read:drinks"],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListDrinksResponse(
                drinks=utils.unmarshal_json(
                    http_res.text, Optional[List[components.Drink]]
                ),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.ListDrinksResponse(
                error=utils.unmarshal_json(http_res.text, Optional[components.Error]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_drink(
        self,
        *,
        name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetDrinkResponse:
        r"""Get a drink.

        Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param name:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

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
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getDrink",
                oauth2_scopes=["read:basic"],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetDrinkResponse(
                drink=utils.unmarshal_json(http_res.text, Optional[components.Drink]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GetDrinkResponse(
                error=utils.unmarshal_json(http_res.text, Optional[components.Error]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_drink_async(
        self,
        *,
        name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetDrinkResponse:
        r"""Get a drink.

        Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

        :param name:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetDrinkRequest(
            name=name,
        )

        req = self.build_request_async(
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
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getDrink",
                oauth2_scopes=["read:basic"],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetDrinkResponse(
                drink=utils.unmarshal_json(http_res.text, Optional[components.Drink]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.APIErrorData)
            raise errors.APIError(data=data)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.GetDrinkResponse(
                error=utils.unmarshal_json(http_res.text, Optional[components.Error]),
                http_meta=components.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
