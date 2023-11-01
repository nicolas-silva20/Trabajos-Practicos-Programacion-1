import pytest
import sys
sys.path.append("D:/Facultad/Programacion/TP y Ejercicios en Clase")
from funciones import is_multiple

@pytest.mark.parametrize('first_number, second_number, res',[
    (2, 4, True),
    (1, 3, False),
    (5, 10, True),
    (3, 7, False)
])

def test_is_multiple(first_number, second_number, res):
    assert is_multiple(first_number, second_number) == res or is_multiple(second_number, first_number) == res