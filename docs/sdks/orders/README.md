# Orders
(*orders*)

## Overview

The orders endpoints.

### Available Operations

* [create_order](#create_order) - Create an order.

## create_order

Create an order for a drink.

### Example Usage

```python
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

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request_body`                                                       | List[[components.OrderInput](../../models/components/orderinput.md)] | :heavy_check_mark:                                                   | N/A                                                                  |
| `callback_url`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The url to call when the order is updated.                           |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
