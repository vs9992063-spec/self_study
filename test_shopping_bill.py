import pytest
from shopping_bill import subtotal, discount, final_bill


def test_subtotal_success():
    assert subtotal([100, 250.50, 149.50]) == 500.00
    assert subtotal([]) == 0.00


def test_subtotal_negative_item():
    with pytest.raises(ValueError, match="cannot be negative"):
        subtotal([200, -50])


def test_discount_tiers():
    assert discount(300) == 0.00
    assert discount(500) == 25.00
    assert discount(1050) == 105.00


def test_discount_negative():
    with pytest.raises(ValueError, match="cannot be negative"):
        discount(-100)


def test_final_bill_success():
    assert final_bill([200, 150]) == 350.00          # < 500 -> 0% off
    assert final_bill([300, 300]) == 570.00          # 600 -> 5% off (30)
    assert final_bill([450.00, 350.00, 250.00]) == 945.00  # 1050 -> 10% off (105)