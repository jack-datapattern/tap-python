
import pandas as pd
import pytest
import os

def validate_price(price):
    return price > 0


class SchemaError(Exception):
    pass


def check_schema(df, required_columns):

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise SchemaError(f"Missing columns: {missing_columns}")

    return True


def load_csv(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    return pd.read_csv(file_path)


def test_valid_price():
    assert validate_price(100) is True


def test_invalid_price():
    assert validate_price(0) is False


def test_schema_valid():
    df = pd.DataFrame({"order_id": [1], "customer_id": [2]})

    assert check_schema(df, ["order_id", "customer_id"]) is True


def test_schema_missing_column():
    df = pd.DataFrame({"order_id": [1]})

    with pytest.raises(SchemaError):
        check_schema(df, ["order_id", "customer_id"])


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_csv("missing_file.csv")
