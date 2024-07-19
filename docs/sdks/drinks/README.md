# Drinks
(*drinks*)

## Overview

The drinks endpoints.

### Available Operations

* [list_drinks](#list_drinks) - Get a list of drinks.
* [get_drink](#get_drink) - Get a drink.

## list_drinks

Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

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


res = s.drinks.list_drinks()

if res.drinks is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `drink_type`                                                                 | [Optional[components.DrinkType]](../../models/components/drinktype.md)       | :heavy_minus_sign:                                                           | The type of drink to filter by. If not provided all drinks will be returned. |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.ListDrinksResponse](../../models/operations/listdrinksresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_drink

Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

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


res = s.drinks.get_drink(name="<value>")

if res.drink is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetDrinkResponse](../../models/operations/getdrinkresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
