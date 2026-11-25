from __future__ import annotations
from collections.abc import Iterable
from decimal import Decimal, ROUND_HALF_UP


def _to_decimal(value: float | int | str | Decimal) -> Decimal:
    return Decimal(str(value))


def _round_currency(amount: Decimal) -> float:
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def subtotal(items: Iterable[float | int | str | Decimal]) -> float:
    """Calculate the subtotal from an iterable of item prices."""
    total = Decimal("0.00")
    for price in items:
        item_price = _to_decimal(price)
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        total += item_price
    return _round_currency(total)


def discount(total: float | int | str | Decimal) -> float:
    """Calculate discount amount based on total bill amount."""
    amount = _to_decimal(total)
    if amount < 0:
        raise ValueError("Total cannot be negative.")

    if amount >= Decimal("1000.00"):
        rate = Decimal("0.10")  # 10% discount
    elif amount >= Decimal("500.00"):
        rate = Decimal("0.05")   # 5% discount
    else:
        rate = Decimal("0.00")   # No discount

    return _round_currency(amount * rate)


if __name__ == "__main__":
    cart_items = [450.00, 350.00, 250.00]
    sub = subtotal(cart_items)
    disc = discount(sub)
    print(f"Subtotal: {sub:.2f}")
    print(f"Discount: {disc:.2f}")