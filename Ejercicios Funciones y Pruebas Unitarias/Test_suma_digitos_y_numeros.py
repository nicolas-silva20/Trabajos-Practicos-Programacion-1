import pytest
from funciones import*

@pytest.mark.parametrize('number,add',[
    (123, 6),
    (541, 10),
    (777, 21),
])

def test_add_digits(number):
    assert add_digits(number)