import pytest
from seasons import date_flow

def test_date_flow_iso_format():
    assert date_flow("2023-05-23") == "Five hundred thirty-four thousand, two hundred forty minutes"


def test_invalid_date_format():
    with pytest.raises(SystemExit):
        date_flow("January 1, 1999")
