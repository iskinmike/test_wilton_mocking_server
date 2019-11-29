import uuid

from yandex_checkout import Configuration, Payment

idemp_key = uuid.uuid4()

print (idemp_key)

Configuration.account_id = 'test_656330'
Configuration.secret_key = 'test_iGJ8jf2z8j8tWXgb8VKuwWZ3UD_69xrKiX7iqDHIcEc'

payment = Payment.create({
    "amount": {
        "value": "100.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.merchant-website.com/return_url"
    },
    "capture": True,
    "description": "Заказ №1"
}, idemp_key)
