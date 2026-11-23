from reader import read_csv
from validator import valid
from transformer import convert_prices


def test_read_csv():
    result = read_csv("../olist_order_items_dataset.csv")

    assert isinstance(result, list)
    assert len(result) > 0

def test_valid():
    result = valid("../olist_orders_dataset.csv")

    assert result is not None

def test_convert_prices():
    result = convert_prices("../olist_order_items_dataset.csv")

    assert result is not None