from celcius import celcius_to_fahrenheit


def test_zero():
    assert celcius_to_fahrenheit() == 32


def test_positive():
    assert celcius_to_fahrenheit(100) == 212


def test_negative():
    assert celcius_to_fahrenheit(-40) == -40
