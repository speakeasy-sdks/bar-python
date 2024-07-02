<!-- Start SDK Example Usage [usage] -->
```python
import barpython
from barpython.models import components

s = barpython.BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.drinks.list_drinks(drink_type=components.DrinkType.SPIRIT)

if res.drinks is not None:
    # handle response
    pass

```

```python
import barpython
from barpython.models import components

s = barpython.BarPython(
    security=components.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.orders.create_order(request_body=[
    components.OrderInput(
        type=components.OrderType.INGREDIENT,
        product_code='AC-A2DF3',
        quantity=138554,
    ),
], callback_url='<value>')

if res.order is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->