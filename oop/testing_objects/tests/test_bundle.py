
import pytest
from src.bundle import *

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
    
def test_processingDays():
    bundle = Bundle()
    bundle.dropoff_month = 5
    bundle.dropoff_day = 29
    bundle.ready_month = 6
    bundle.ready_day = 2
    assert bundle.processingDays() == 3

def test_holdingDays():
    bundle = Bundle()
    bundle.dropoff_month = 5
    bundle.dropoff_day = 29
    bundle.pickup_month = 6
    bundle.pickup_day = 5
    assert bundle.holdingDays() == 7
    

