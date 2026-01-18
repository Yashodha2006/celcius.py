from celcius import celsius_to_fahrenheit

def test_zero():
    assert celsius_to_fahrenheit() == 32

def test_positive():
    assert celsius_to_fahrenheit(100) == 212

def test_negative():
    assert celsius_to_fahrenheit(-40) == -40
