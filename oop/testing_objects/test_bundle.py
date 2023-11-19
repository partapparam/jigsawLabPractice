
import pytest
from bundle import *

def test_bundle():
    bundle = Bundle()
    assert type(bundle) == Bundle


def test_min_price_is_ten():
    bundle = Bundle()
    bundle.weight = 3
    assert bundle.price() == 10

def test_additional_one_point_if_over_five_points():
    bundle = Bundle()
    bundle.weight = 7
    assert bundle.price() == 13
    