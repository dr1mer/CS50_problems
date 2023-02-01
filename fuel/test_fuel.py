import pytest
from fuel import convert, gauge


def main():
    test_quorter()
    test_empty()
    test_full()
    test_zero_division()
    test_value()



def test_quorter():
    assert convert('1/4')==25 and gauge(25)=="25%"

def test_empty():
    assert convert('1/100')==1 and gauge(1)=="E"

def test_full():
    assert convert('99/100')==99 and gauge(99)=="F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('br/sd')


if __name__ == "__main__":
    main()
