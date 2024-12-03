<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

with BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as s:
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
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

async def main():
    async with BarPython(
        security=components.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as s:
        res = await s.drinks.list_drinks_async()

        if res.drinks is not None:
            # handle response
            pass

asyncio.run(main())
```

```python
# Synchronous Example
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

with BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as s:
    res = s.orders.create_order(request_body=[
        {
            "type": components.OrderType.DRINK,
            "product_code": "APM-1F2D3",
            "quantity": 837978,
        },
        {
            "type": components.OrderType.DRINK,
            "product_code": "AC-A2DF3",
            "quantity": 589796,
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
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

async def main():
    async with BarPython(
        security=components.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as s:
        res = await s.orders.create_order_async(request_body=[
            {
                "type": components.OrderType.DRINK,
                "product_code": "APM-1F2D3",
                "quantity": 837978,
            },
            {
                "type": components.OrderType.DRINK,
                "product_code": "AC-A2DF3",
                "quantity": 589796,
            },
        ])

        if res.order is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->