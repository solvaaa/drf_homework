from math import ceil

import stripe
from stripe.error import InvalidRequestError

from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_stripe_product(product):
    return stripe.Product.create(
        id=str(product.id),
        name=product.name
    )


def get_stripe_product(product):
    try:
        stripe_product = stripe.Product.retrieve(str(product.id))
    except InvalidRequestError:
        stripe_product = create_stripe_product(product)
    return stripe_product


def create_stripe_price(product):
    return stripe.Price.create(
        unit_amount=int(product.price * 100),
        currency="usd",
        product=str(product.id),
    )


def get_stripe_price(product):
    prices_list = stripe.Price.list(type="one_time", product=product.id, currency="usd")
    for price in prices_list["data"]:
        if int(product.price * 100) == price["unit_amount"]:
            return price
    return create_stripe_price(product)


def create_session(price, product=None):
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price["id"],
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return session
