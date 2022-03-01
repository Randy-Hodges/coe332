#!/usr/bin/python3

import pytest 
import math
from ml_data_analysis import compute_average_mass, check_hemisphere, count_classes


def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True


def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                               # send an empty list
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')             # dictionaries not uniform
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')           # value not a float
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')             # key not in dicts


def test_check_hemisphere():
    assert check_hemisphere(56.5, 50) == 'Northern & Eastern'
    assert check_hemisphere(-56.5, 50) == 'Southern & Eastern'
    assert check_hemisphere(56.5, -5) == 'Northern & Western'
    with pytest.raises(ValueError):
        check_hemisphere(0, 0) 
    with pytest.raises(TypeError):
        check_hemisphere(1.23, 'asdf') 

def test_count_classes():
    assert count_classes({}, 'red') == {}
    assert count_classes([{'red': 'cool'}, {'red': 'cool', 'blue': 'cooler'}], 'red') == {'cool': 2}
    assert isinstance(count_classes([{'red': 1}, {'red': 3, 'blue': 20}], 'red'), dict) == True
    with pytest.raises(TypeError):
        count_classes('red', 'blue')
    with pytest.raises(TypeError):
        count_classes() 