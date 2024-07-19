# speakeasy-bar-py

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+<UNSET>.git
```

Poetry
```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example 1

```python
# Synchronous Example
import os
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

s = BarPython(
    security=components.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.drinks.list_drinks()

if res.drinks is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

async def main():
    s = BarPython(
        security=components.Security(
            api_key=os.getenv("API_KEY", ""),
        ),
    )
    res = await s.drinks.list_drinks_async()
    if res.drinks is not None:
        # handle response
        pass

asyncio.run(main())
```

### Example 2

```python
# Synchronous Example
import os
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

s = BarPython(
    security=components.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.orders.create_order(request_body=[
    {
        "type": components.OrderType.INGREDIENT,
        "product_code": "AC-A2DF3",
        "quantity": 138554,
    },
])

if res.order is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

async def main():
    s = BarPython(
        security=components.Security(
            api_key=os.getenv("API_KEY", ""),
        ),
    )
    res = await s.orders.create_order_async(request_body=[
        {
            "type": components.OrderType.DRINK,
            "product_code": "NAC-3F2D1",
            "quantity": 547214,
        },
    ])
    if res.order is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [authentication](docs/sdks/authentication/README.md)

* [authenticate](docs/sdks/authentication/README.md#authenticate) - Authenticate with the API by providing a username and password.

### [drinks](docs/sdks/drinks/README.md)

* [list_drinks](docs/sdks/drinks/README.md#list_drinks) - Get a list of drinks.
* [get_drink](docs/sdks/drinks/README.md#get_drink) - Get a drink.

### [ingredients](docs/sdks/ingredients/README.md)

* [list_ingredients](docs/sdks/ingredients/README.md#list_ingredients) - Get a list of ingredients.

### [orders](docs/sdks/orders/README.md)

* [create_order](docs/sdks/orders/README.md#create_order) - Create an order.

### [config](docs/sdks/config/README.md)

* [subscribe_to_webhooks](docs/sdks/config/README.md#subscribe_to_webhooks) - Subscribe to webhooks.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from barpython.utils import BackoffStrategy, RetryConfig
from speakeasy_bar_py import BarPython

s = BarPython()


res = s.authentication.authenticate(request={},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res.object is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from barpython.utils import BackoffStrategy, RetryConfig
from speakeasy_bar_py import BarPython

s = BarPython(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
)


res = s.authentication.authenticate(request={})

if res.object is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

### Example

```python
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import errors

s = BarPython()

res = None
try:
    res = s.authentication.authenticate(request={})

except errors.APIError as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `prod` | `https://speakeasy.bar` | None |
| `staging` | `https://staging.speakeasy.bar` | None |
| `customer` | `https://{organization}.{environment}.speakeasy.bar` | `organization` (default is `api`), `environment` (default is `prod`) |

#### Example

```python
from speakeasy_bar_py import BarPython

s = BarPython(
    server="customer",
)


res = s.authentication.authenticate(request={})

if res.object is not None:
    # handle response
    pass

```

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `organization: str`
 * `environment: models.ServerEnvironment`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from speakeasy_bar_py import BarPython

s = BarPython(
    server_url="https://speakeasy.bar",
)


res = s.authentication.authenticate(request={})

if res.object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from speakeasy_bar_py import BarPython
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = BarPython(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = BarPython(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                 | Type                 | Scheme               |
| -------------------- | -------------------- | -------------------- |
| `api_key`            | apiKey               | API key              |
| `client_credentials` | oauth2               | OAuth2 token         |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import os
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

s = BarPython(
    security=components.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.authentication.authenticate(request={})

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
