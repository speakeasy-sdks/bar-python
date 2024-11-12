<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

s = BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
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
from speakeasy_bar_py import BarPython
from speakeasy_bar_py.models import components

async def main():
    s = BarPython(
        security=components.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    )
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

s = BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.orders.create_order(request_body=[
    {
        "type": components.OrderType.DRINK,
        "product_code": "NAC-3F2D1",
        "quantity": 837978,
    },
    {
        "type": components.OrderType.DRINK,
        "product_code": "NAC-3F2D1",
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
    s = BarPython(
        security=components.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    )
    res = await s.orders.create_order_async(request_body=[
        {
            "type": components.OrderType.DRINK,
            "product_code": "NAC-3F2D1",
            "quantity": 837978,
        },
        {
            "type": components.OrderType.DRINK,
            "product_code": "NAC-3F2D1",
            "quantity": 589796,
        },
    ])
    if res.order is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->