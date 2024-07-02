# GetDrinkResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `drink`                                                            | [Optional[components.Drink]](../../models/components/drink.md)     | :heavy_minus_sign:                                                 | A drink.                                                           |
| `error`                                                            | [Optional[components.Error]](../../models/components/error.md)     | :heavy_minus_sign:                                                 | An unknown error occurred interacting with the API.                |