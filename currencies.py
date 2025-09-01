# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
    "CNYEUR": 0.13,
    "EURUSD": 1.18
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    amount_value, source_currency = amount
    if source_currency == currency:
        return round(amount_value)
    rate_key = source_currency + currency
    if rate_key in RATES:
        converted_amount = amount_value * RATES[rate_key]
        return round(converted_amount)

    return None
